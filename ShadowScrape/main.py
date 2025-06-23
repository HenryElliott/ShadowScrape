# main.py

import customtkinter as ctk
from tkinter import filedialog
import asyncio
import json
import pandas as pd
import os
from parsers.hackernews import scrape_hackernews

# ASCII BANNER
BANNER = r"""
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
"""

# Basic GUI setup
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("ShadowScrape")
app.geometry("780x640")

# Widgets
ascii_label = ctk.CTkLabel(app, text=BANNER, font=("Courier", 10), justify="left")
ascii_label.pack(pady=8)

url_label = ctk.CTkLabel(app, text="Enter URLs (one per line):")
url_label.pack()

url_box = ctk.CTkTextbox(app, width=740, height=100)
url_box.pack(pady=6)

image_scrape_var = ctk.BooleanVar()
image_toggle = ctk.CTkCheckBox(app, text="Enable Image Scraping", variable=image_scrape_var)
image_toggle.pack(pady=4)

log_box = ctk.CTkTextbox(app, width=740, height=250)
log_box.pack(pady=10)
log_box.insert("end", "[+] ShadowScrape Ready\n")

# Save results in memory
scrape_results = []

def log(msg):
    log_box.insert("end", msg + "\n")
    log_box.see("end")

async def run_scrape():
    log("[*] Starting scrape...")

    raw_urls = url_box.get("1.0", "end").strip().splitlines()
    urls = [u.strip() for u in raw_urls if u.strip()]
    
    if not urls:
        log("[-] No URLs entered.")
        return

    global scrape_results
    scrape_results = await scrape_hackernews(urls, download_images=image_scrape_var.get())
    for entry in scrape_results:
        log(f"[+] {entry.get('title', '[NO TITLE]')}")

    log("[✓] Scraping complete!")

def start_scrape():
    asyncio.run(run_scrape())

def export_json():
    if not scrape_results:
        log("[-] Nothing to export.")
        return
    path = filedialog.asksaveasfilename(defaultextension=".json")
    if path:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(scrape_results, f, indent=2)
        log(f"[+] Exported to {path}")

def export_csv():
    if not scrape_results:
        log("[-] Nothing to export.")
        return
    path = filedialog.asksaveasfilename(defaultextension=".csv")
    if path:
        df = pd.DataFrame(scrape_results)
        df.to_csv(path, index=False)
        log(f"[+] Exported to {path}")

button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=8)

start_button = ctk.CTkButton(button_frame, text="Start Scrape", command=start_scrape)
start_button.pack(side="left", padx=10)

json_button = ctk.CTkButton(button_frame, text="Export JSON", command=export_json)
json_button.pack(side="left", padx=10)

csv_button = ctk.CTkButton(button_frame, text="Export CSV", command=export_csv)
csv_button.pack(side="left", padx=10)

app.mainloop()
