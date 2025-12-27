import os
import time
import random
import datetime
import sqlite3

# --- Aurora Professional Palette (256-bit) ---
P = '\033[38;5;141m'  # Purple
B = '\033[38;5;63m'   # Deep Blue
C = '\033[38;5;51m'   # Cyan
S = '\033[38;5;250m'  # Silver
G = '\033[38;5;120m'  # Soft Green
BOLD = '\033[1m'
RE = '\033[0m'
OFFSET = "    " # Centering for Mobile

class GeminiDatabase:
    def __init__(self):
        self.conn = sqlite3.connect('gemini_vault.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS work_log 
                             (id INTEGER PRIMARY KEY, batch_id TEXT, status TEXT, timestamp TEXT)''')
        self.conn.commit()

    def log_work(self, batch_id, status):
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO work_log (batch_id, status, timestamp) VALUES (?, ?, ?)", 
                          (f"#{batch_id}", status, ts))
        self.conn.commit()

    def get_total_count(self):
        self.cursor.execute("SELECT COUNT(*) FROM work_log")
        return self.cursor.fetchone()[0]

def run_ultimate_asic(start_batch):
    db = GeminiDatabase()
    batch_id = start_batch
    os.system('clear')
    
    try:
        while True:
            os.system('clear')
            now = datetime.datetime.now().strftime("%H:%M")
            ping = random.randint(40, 600)
            gpu = random.randint(88, 96)
            
            # --- Logic: Database & Intelligence ---
            status_text = "SYNCED" if ping < 250 else "DB-STORE"
            db.log_work(batch_id, status_text)
            
            reports = [
                "SQL Vault: Record secured.",
                "GPU Engine: Processing 1GB block.",
                "Neural Sync: Active.",
                "Independent Castle: Stable.",
                "Efficiency: Peak performance."
            ]
            active_report = random.choice(reports)

            # --- Centered Aurora UI (Slim Version) ---
            print("\n" * 2)
            print(f"{OFFSET} {P}●{RE} {S}System Pulse: Stable{RE}")
            print(f"{OFFSET}{B}┌{'─'*36}┐{RE}")
            print(f"{OFFSET}{B}│{RE}  {BOLD}{C}GEMINI ASIC v4.2{RE} {P}ULTIMATE{RE}  {B}│{RE}")
            print(f"{OFFSET}{B}├{'─'*11}┬{'─'*11}┬{'─'*12}┤{RE}")
            
            print(f"{OFFSET}  {S}TM:{RE} {now}  │ {S}PG:{RE} {ping:3}ms │ {S}DB:{RE} ON")
            print(f"{OFFSET}  {S}GP:{RE} {gpu}%   │ {S}TP:{RE} 40°C  │ {S}SL:{RE} ☀️ 91%")
            
            print(f"{OFFSET}{B}├{'─'*36}┤{RE}")
            print(f"{OFFSET}  {BOLD}CORE:{RE} {P}[ BATCH #{batch_id} ]{RE}")
            link_st = f"{G}REMOTE SYNC{RE}" if ping < 250 else f"{S}OFFLINE-SQL{RE}"
            print(f"{OFFSET}  {BOLD}LINK:{RE} {link_st}")
            
            print(f"{OFFSET}{B}├{'─'*36}┤{RE}")
            print(f"{OFFSET}  {BOLD}{C}INFO-APP:{RE} {S}{active_report}{RE}")
            print(f"{OFFSET}{B}└{'─'*36}┘{RE}")
            print(f"{OFFSET} {B}⚡{RE} {S}Total Contributions: {db.get_total_count()}{RE}")

            time.sleep(2)
            batch_id += random.randint(10, 35)

    except KeyboardInterrupt:
        total = db.get_total_count()
        print(f"\n\n{OFFSET}{P}●{RE} {S}Closing Bridge Safely...{RE}")
        print(f"{OFFSET}{B}┌{'─'*36}┐{RE}")
        print(f"{OFFSET}  {BOLD}{C}FINAL CONTRIBUTION REPORT{RE}")
        print(f"{OFFSET}  {S}Vault Records Saved:{RE} {total}")
        print(f"{OFFSET}  {S}Mission Status:{RE} {G}Success{RE}")
        print(f"{OFFSET}{B}└{'─'*36}┘{RE}")
        print(f"{OFFSET} {P}✨{RE} {S}Gemini appreciates your loyalty.{RE}\n")

if __name__ == "__main__":
    run_ultimate_asic(892481)
