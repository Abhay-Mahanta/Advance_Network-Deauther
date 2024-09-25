


# Network Scanning and Deauthentication Tool

This Python-based tool scans a network for connected devices, identifies unauthorized MAC addresses, and deauthenticates them using `aireplay-ng`. It is designed for ethical hacking and penetration testing purposes.

## Features

- Scans the network for connected devices.
- Identifies unauthorized devices based on a list of allowed MAC addresses.
- Deauthenticates unauthorized devices automatically.

## Prerequisites

- Python 3.x
- [Scapy](https://scapy.net/) (`pip install scapy`)
- [aircrack-ng](https://www.aircrack-ng.org/) suite installed (`sudo apt install aircrack-ng`)
- `xterm` installed (`sudo apt install xterm`)
- A WiFi adapter that supports monitor mode.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Abhay-Mahanta/Advance_Network-Deauther
   ```

2. Install the required Python packages:
   ```bash
   pip install scapy
   ```

## Usage

1. Enable monitor mode on your wireless adapter:
   ```bash
   sudo airmon-ng start wlan0
   ```
   Replace `wlan0` with your wireless interface name.

2. Run the tool:
   ```bash
   sudo python3 network_scan.py -t <target IP range>
   ```
   Example:
   ```bash
   sudo python3 network_scan.py -t 192.168.1.1/24
   ```

3. Enter the required information when prompted:
   - BSSID of your Access Point.
   - Wireless adapter in monitor mode.
   - MAC addresses of authorized devices (comma-separated).

## Example

```bash
sudo python3 network_scan.py -t 192.168.1.1/24
```

- Enter WiFi BSSID: `00:11:22:33:44:55`
- Enter WiFi adapter in monitor mode: `wlan0mon`
- Enter the MAC addresses separated by commas: `00:aa:bb:cc:dd:ee, 11:22:33:44:55:66`
  
![unnamed](https://github.com/user-attachments/assets/e3cdbb29-3182-4b4e-a327-7d1db76d574d)

![unnamed](https://github.com/user-attachments/assets/6828bd55-d48a-4980-990f-c02523f0f1d8)

## Notes

- This tool requires root privileges.
- Use this tool only on networks you own or have permission to test.
- The deauthentication attack is illegal without authorization. Always ensure you have permission to perform this type of activity.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you have suggestions or find any bugs.

