# Simple Port Scanner

A lightweight Python TCP port scanner built as a cybersecurity learning project. It checks a selected target against a set of commonly used TCP ports and reports which ports are open.

## Features

- Scans common TCP ports
- Accepts an IP address or resolvable hostname
- Uses Python's built-in `socket` library
- Handles invalid hosts and connection errors
- Requires no external Python packages

## Requirements

- Python 3.x

## Usage

```bash
python port_scanner.py <target>
```

Example:

```bash
python port_scanner.py 192.168.1.10
```

The scanner currently checks these ports:

`21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389`

## How It Works

The script attempts a TCP connection to each configured port using `socket.connect_ex()`. A successful connection indicates that the port is accepting TCP connections.

## Limitations

- It scans a predefined port list rather than the full TCP range.
- It does not perform service/version detection.
- It does not attempt vulnerability detection.
- Results may be affected by firewalls, filtering, or network latency.

## Future Improvements

- Custom port ranges
- Concurrent scanning for improved speed
- Service identification
- Exportable scan results
- Configurable timeouts

## Responsible Use

This project is intended for learning, lab work, and authorized security testing. Only scan systems and networks you own or have explicit permission to test.
