# ShadowScrape - Advanced Python Web Scraper with GUI

```
  ██████  ██░ ██  ▄▄▄      ▓█████▄  ▒█████   █     █░  ██████  ▄████▄   ██▀███   ▄▄▄       ██▓███  ▓█████ 
▒██    ▒ ▓██░ ██▒▒████▄    ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░▒██    ▒ ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▓██░  ██▒▓█   ▀ 
░ ▓██▄   ▒██▀▀██░▒██  ▀█▄  ░██   █▌▒██░  ██▒▒█░ █ ░█ ░ ▓██▄   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▒███   
  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██ ░▓█▄   ▌▒██   ██░░█░ █ ░█   ▒   ██▒▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ 
▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒░▒████▓ ░ ████▓▒░░░██▒██▓ ▒██████▒▒▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░░▒████▒
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░
░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░ ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░  ░ ░▒  ░ ░  ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░      ░ ░  ░
░  ░  ░   ░  ░░ ░  ░   ▒    ░ ░  ░ ░ ░ ░ ▒    ░   ░  ░  ░  ░  ░          ░░   ░   ░   ▒   ░░          ░   
      ░   ░  ░  ░      ░  ░   ░        ░ ░      ░          ░  ░ ░         ░           ░  ░            ░  ░
                            ░                                 ░                                           
```

## Overview

ShadowScrape is a Python-based advanced web scraper with a clean GUI built on CustomTkinter. It supports asynchronous scraping, rate limiting, ban detection, proxy & user-agent rotation, and optional image downloading.

## Features

- Headless scraping with Playwright  
- Modular site parsers (example: Hacker News)  
- Rate limiting to avoid bans  
- Ban detection based on HTTP status & content  
- Random User-Agent rotation  
- Optional image scraping  
- Export data as JSON or CSV  
- Beautiful, responsive GUI with live logs  

## Requirements

- Python 3.9 or higher  
- pip package manager  

## Installation

### Manual Setup (Linux/macOS)

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install playwright beautifulsoup4 customtkinter pandas fake-useragent aiolimiter aiofiles

# Install Playwright browsers
playwright install
```

### Windows Setup

```powershell
# Create and activate virtual environment
python -m venv venv
.env\Scriptsctivate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install playwright beautifulsoup4 customtkinter pandas fake-useragent aiolimiter aiofiles

# Install Playwright browsers
playwright install
```

Alternatively, run the provided `setup.sh` (Linux/macOS) or ask for a Windows batch script.

## Usage

1. Activate your virtual environment if not already active:
```bash
source venv/bin/activate  # Linux/macOS
.env\Scriptsctivate   # Windows
```

2. Run the GUI app:
```bash
python main.py
```

3. Paste URLs into the input box (one per line).  
4. Optionally enable image scraping.  
5. Click **Start Scrape** and watch logs live.  
6. Export results to JSON or CSV using the buttons.

## Adding Parsers

- Parsers live in the `parsers/` folder.  
- Add a new Python module with an async `scrape_<sitename>(urls, download_images=False)` function.  
- Call this from `main.py` or extend GUI options.

## Security & Best Practices

- Never run the scraper as root.  
- Use virtual environments to avoid polluting system Python.  
- Handle data securely; sanitize inputs when expanding parsers.  
- Avoid hardcoded credentials or proxies.

## License

MIT License © 2025

---

Enjoy scraping! 🚀
