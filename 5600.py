import os
import time
import random
import datetime

# --- Aurora Professional Palette ---
P = '\033[38;5;141m'  # Purple
B = '\033[38;5;63m'   # Deep Blue
C = '\033[38;5;51m'   # Cyan
S = '\033[38;5;250m'  # Silver
G = '\033[38;5;120m'  # Soft Green
BOLD = '\033[1m'
RE = '\033[0m'
OFFSET = "    " # برای آوردن برنامه به مرکز صفحه

def run_centric_asic(batch_id):
    while True:
        os.system('clear')
        now = datetime.datetime.now().strftime("%H:%M")
        ping = random.randint(40, 500)
        
        reports = [
            "Neural patterns analyzed.",
            "Solar intake stable.",
            "Bridge synchronized.",
            "GPU Engines: Optimal.",
            "Local buffer encrypted."
        ]
        active_report = random.choice(reports)

        # --- Aurora UI Design (Slim & Centered) ---
        print("\n" * 2) # فاصله از بالای صفحه
        print(f"{OFFSET} {P}●{RE} {S}System Pulse: Stable{RE}")
        print(f"{OFFSET}{B}┌{'─'*36}┐{RE}")
        print(f"{OFFSET}{B}│{RE}  {BOLD}{C}GEMINI ASIC v4.1{RE} {P}AURORA{RE}   {B}│{RE}")
        print(f"{OFFSET}{B}├{'─'*11}┬{'─'*11}┬{'─'*12}┤{RE}")
        
        # Metrics - Slim Version
        print(f"{OFFSET}  {S}TM:{RE} {now}  │ {S}PG:{RE} {ping:3}ms │ {S}CH:{RE} 16kb")
        print(f"{OFFSET}  {S}GP:{RE} 92%   │ {S}TP:{RE} 40°C  │ {S}SL:{RE} ☀️ 91%")
        
        print(f"{OFFSET}{B}├{'─'*36}┤{RE}")
        
        # Central Work Section
        print(f"{OFFSET}  {BOLD}CORE:{RE} {P}[ BATCH #{batch_id} ]{RE}")
        status = f"{G}ACTIVE SYNC{RE}" if ping < 200 else f"{S}LOCAL CACHE{RE}"
        print(f"{OFFSET}  {BOLD}LINK:{RE} {status}")
        
        print(f"{OFFSET}{B}├{'─'*36}┤{RE}")
        
        # --- INFO-APP REPORT ---
        print(f"{OFFSET}  {BOLD}{C}INFO-APP:{RE} {S}{active_report}{RE}")
        
        print(f"{OFFSET}{B}└{'─'*36}┘{RE}")
        print(f"{OFFSET} {B}⚡{RE} {S}Efficiency: +22%{RE}")

        time.sleep(2.5)
        batch_id += random.randint(10, 30)

if __name__ == "__main__":
    run_centric_asic(889389)
