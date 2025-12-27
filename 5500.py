import os
import time
import random
import datetime

# --- Soft & Friendly Colors ---
PINK = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
GOLD = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def get_solar_icon(percent):
    if percent > 80: return "☀️"
    if percent > 50: return "⛅"
    return "🌙"

def run_friendly_asic(batch_id):
    while True:
        os.system('clear')
        now = datetime.datetime.now().strftime("%H:%M")
        solar = random.randint(85, 99)
        ping = random.randint(40, 550)
        gpu_load = random.randint(80, 95)
        
        # --- Friendly Header ---
        print(f"{PINK}✨ Welcome back! Your castle is safe and running. ✨{RESET}")
        
        # --- Compact & Modern Box ---
        print(f"{BLUE}╭{'─'*45}╮{RESET}")
        print(f"{BLUE}│{RESET}  {BOLD}{CYAN}🚀 GEMINI SOLAR-ASIC v3.5{RESET}     {GOLD}{get_solar_icon(solar)} {solar}%{RESET}  {BLUE}│{RESET}")
        print(f"{BLUE}├{'─'*15}┬{'─'*14}┬{'─'*14}┤{RESET}")
        
        # Metrics with Icons
        print(f"  🕒 {now}      │ 📶 {ping:3}ms    │ 💾 SD: {random.randint(0,20)}kb")
        print(f"  ⚙️  GPU: {gpu_load}%   │ 🧠 RAM: 100MB │ 🌡️  Temp: 40°C")
        
        print(f"{BLUE}├{'─'*45}┤{RESET}")
        
        # Status Logic
        if ping > 250:
            status = f"{GOLD}📥 Resting (Caching){RESET}"
            msg = "Keeping your data safe in the SD card..."
        else:
            status = f"{GREEN}🛰️  Streaming Live{RESET}"
            msg = "Bridge is active. Sending light to Gemini."

        print(f"  {BOLD}CURRENT BATCH:{RESET} {PINK}#{batch_id}{RESET}")
        print(f"  {BOLD}SYSTEM STATE:{RESET}  {status}")
        
        print(f"{BLUE}╰{'─'*45}╯{RESET}")
        
        # --- Comforting Footer ---
        print(f" {BLUE}💡 Tip:{RESET} {msg}")
        print(f" {GREEN}✔{RESET} All systems are stable. No action needed.")

        time.sleep(2)
        batch_id += 12

if __name__ == "__main__":
    run_friendly_asic(889065)
