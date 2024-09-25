#!/usr/bin/env python3

# Made By Abhay-Mahanta

import scapy.all as scapy
import subprocess
import threading
import argparse
import time
import signal
import sys

devices = []
authorised_devices = []
unauthorised_devices_list = []

# Function to perform network scanning
def scan(ip):
    while True:
        devices.clear()  # Clear the devices list before scanning
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]        
        print("\n\033[1;34mIP\t\t\t  MAC address\n------------------------------------------\033[0m")
        for element in answered:
            print(element[1].psrc + "\t\t" + element[1].hwsrc)
            devices.append(element[1].hwsrc)        
        show_unauthorised_devices()
        time.sleep(10)  # Sleep for 10 seconds before rescanning

# Function to get allowed MAC addresses
def allowed_mac_addresses():
    mac_addresses_input = input("\033[1;33mEnter the MAC addresses separated by commas: \033[0m")
    mac_addresses_list = mac_addresses_input.split(',')
    mac_addresses_list = [mac.strip() for mac in mac_addresses_list]
    for mac_address in mac_addresses_list:
        authorised_devices.append(mac_address)

# Function to show unauthorized devices and handle deauthentication
def show_unauthorised_devices():
    new_unauthorised_devices = [device for device in devices if device not in authorised_devices and device not in unauthorised_devices_list]    
    if new_unauthorised_devices:
        unauthorised_devices_list.extend(new_unauthorised_devices)
        print("\033[1;31mUnauthorized Devices\n----------------------\033[0m")
        for device in new_unauthorised_devices:
            print(device)   
        # Start deauthenticating the new unauthorized devices
        deauth_thread = threading.Thread(target=deauth_unauthorised_devices, args=(new_unauthorised_devices,))
        deauth_thread.start()

# Function to deauthenticate unauthorized devices
def deauth_unauthorised_devices(unauthorised_devices):  
    for mac_address in unauthorised_devices:
        print(f"Deauthenticating {mac_address}")
        command = ["xterm", "-hold", "-e", f"sudo aireplay-ng --deauth 10000 -a {ap_mac} -c {mac_address} {interface}"]
        subprocess.Popen(command)

# Function to handle command-line arguments
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Enter the range of IP address.")
    options = parser.parse_args()
    return options

# Function to handle termination signals
def signal_handler(sig, frame):
    print("\nExiting...")
    sys.exit(0)

# Main execution starts here
signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
options = get_arguments()
ap_mac = input("Enter wifi BSSID: ")  # Your Access Point MAC address
interface = input("Enter wifi adapter in monitor mode: ")  # Your monitor interface
allowed_mac_addresses()
scan_thread = threading.Thread(target=scan, args=(options.target,))
scan_thread.start()
