````markdown
# Simple Port Scanner

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)]()

A minimal TCP port scanner written in Python that checks a target host (or multiple hosts) for open TCP ports in a given port range. This script is intended for **educational and defensive** use (lab testing, authorized pentests) only.

---

## Features
- Scan ports from `1` up to a user-specified maximum port.
- Supports scanning multiple comma-separated targets in one run.
- Simple, dependency-light implementation using the Python `socket` module.
- Colored terminal output for clear results (`termcolor`).

---

## Requirements
- Python 3.6+
- `termcolor` (for colored terminal output)

Install dependency:
```bash
pip install termcolor
````

---

## Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Port-Scanner.git
cd Port-Scanner
```

2. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows
```

3. Install the requirement:

```bash
pip install -r requirements.txt
```

Or install `termcolor` directly:

```bash
pip install termcolor
```

> If you don't have `requirements.txt`, create one with:
>
> ```
> termcolor
> ```

---

## Usage

This script is interactive. Run it with Python and follow the prompts:

```bash
python3 port_scanner.py
```

You will be prompted to enter:

* `target(s)`: single IP/hostname or multiple comma-separated (e.g. `192.168.1.10, example.com`)
* `number of ports to scan`: an integer (e.g. `1024`)

### Example session

```
$ python3 port_scanner.py
Enter target(s) to scan (comma-separated for multiple): 192.168.1.5, 10.0.0.7
Enter the number of ports to scan: 1024

Starting scan for 192.168.1.5...
[+] Port 22 is open
[+] Port 80 is open

Starting scan for 10.0.0.7...
[-] Error scanning port 21: [Errno 111] Connection refused
```

---

## Sample Output (JSON / CSV)

This script prints results to the console. If you want structured outputs (CSV/JSON), consider extending the script to save results to a file (examples given in the "Suggested Improvements" section).

---

## Limitations & Notes

* This scanner only performs **TCP connect** checks (`socket.connect_ex`) — no UDP scanning.
* Scanning speed: single-threaded and scans sequentially; large port ranges will be slow.
* Timeout is set to 1 second by default — may need adjustment for high-latency targets.
* Banner grabbing / service detection is not implemented (no detailed fingerprinting).
* This scanner does not perform stealth techniques — it is a basic educational tool.

---

## Ethics & Legal

**IMPORTANT:** Only scan systems and networks for which you have explicit permission. Unauthorized scanning may be illegal and can be treated as malicious activity. Use this tool only in controlled lab environments, on your own infrastructure, or when you have written authorization.

---

## Suggested Improvements (ideas you can implement)

* Add command-line arguments with `argparse` to support non-interactive usage (e.g., `--targets`, `--ports`, `--threads`, `--timeout`).
* Multi-threading or multiprocessing to speed up scans (`concurrent.futures.ThreadPoolExecutor`).
* Port range parsing (e.g., `1-1024`) and common-port presets.
* Output options: CSV / JSON / verbose logs.
* Service banner grabbing for basic service identification.
* Integrate `python-nmap` for richer scanning features (requires nmap installed).
* Add retries/backoff and rate limiting to avoid overloading targets.
* Add unit tests and CI (GitHub Actions) for basic code checks.

---

## How to Contribute

Contributions, bug reports, and feature requests are welcome. Please open an issue or submit a pull request with a clear description and tests/examples for new features.

---

## License

This project is released under the **MIT License**. See the `LICENSE` file for details.

---

## Author / Contact

**Somesh Ambre**
GitHub: [https://github.com/someshambre07](https://github.com/someshambre07)
Email: [someshambre25@gmail.com](mailto:someshambre25@gmail.com) (optional)

```

---

### Extra helpful steps
- Add a `requirements.txt` containing:
```

termcolor

```
then commit it.
- Add an MIT `LICENSE` file (GitHub has a button “Add file → Create new file → Choose a license template”).
- If you want a non-interactive version, I can update your script to accept `argparse` options and produce CSV/JSON output — I can provide that code now if you want.

Would you like me to:
1. Create a `requirements.txt` and `LICENSE` text for you, or  
2. Convert your script to a CLI (argparse) + CSV output version?
::contentReference[oaicite:0]{index=0}
```

