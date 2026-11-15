# NetCrack

**A Python-based Wi-Fi password auditing tool for Windows.**

NetCrack is a lightweight Python script designed to test passwords against a specified WPA2 Wi-Fi network using a local wordlist.

It automates the connection process through Windows' built-in `netsh` utility and checks whether an internet connection is available after each attempt.

## Features

- **Automated password testing** — Processes passwords from a local wordlist.
- **Windows integration** — Uses the native Windows `netsh` WLAN utility.
- **WPA2 support** — Generates WLAN profiles configured for WPA2-PSK with AES encryption.
- **Connectivity verification** — Uses Google's DNS server (`8.8.8.8`) to check internet connectivity.
- **Automatic wordlist management** — Removes tested passwords from the wordlist.
- **Configurable delay** — Allows customization of the waiting time between connection attempts.
- **Lightweight** — Built entirely with Python's standard library.

## Requirements

- Windows operating system
- Python 3.x
- A wireless network adapter
- A local password wordlist

No external Python packages are required.

## Configuration

The script includes three main configuration variables:

| Variable | Description |
|---|---|
| `SSID` | Target Wi-Fi network name |
| `WORDLIST` | Path to the local wordlist |
| `DELAY` | Waiting time between connection attempts |

## How It Works

1. Loads the password wordlist.
2. Reads the first available password.
3. Generates a Windows WLAN profile.
4. Attempts to establish a connection.
5. Checks internet connectivity.
6. If unsuccessful, removes the tested entry from the wordlist.
7. Repeats the process until a successful connection or an error occurs.

## Technical Details

| Component | Technology |
|---|---|
| Language | Python |
| Network management | Windows `netsh` |
| Connectivity check | ICMP Ping |
| Wi-Fi security | WPA2-PSK / AES |
| Dependencies | Python Standard Library |

## Limitations

- Designed specifically for Windows.
- Currently configured for WPA2-PSK networks.
- Requires a compatible wireless adapter.
- Internet connectivity is used as the success indicator.
- A successful Wi-Fi connection without internet access may be incorrectly identified as a failed attempt.
- The script modifies the local Windows WLAN profile and the wordlist file.

## Legal Disclaimer

NetCrack is intended exclusively for authorized security testing on networks you own or have explicit permission to audit.

**Unauthorized access to wireless networks is illegal.**

The author is not responsible for misuse, unauthorized access, or any damage resulting from the use of this software.
