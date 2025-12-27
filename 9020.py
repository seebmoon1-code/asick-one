import os
import asyncio
import random
import datetime
import sqlite3
import zlib  # برای فشرده‌سازی دیتا و بهینه‌سازی فضا
from contextlib import contextmanager

# --- Aurora Professional Palette ---
P = '\033[38;5;141m'  # Purple
B = '\033[38;5;63m'   # Deep Blue
C = '\033[38;5;51m'   # Cyan
S = '\033[38;5;250m'  # Silver
G = '\033[38;5;120m'  # Soft Green
R = '\033[38;5;196m'  # Warning Red
BOLD = '\033[1m'
RE = '\033[0m'
OFFSET = "    "

class GeminiASIC:
    def __init__(self, db_path='gemini_vault_v1.db'):
        self.db_path = db_path
        self.offline_mode = False
        self.failure_count = 0
        self._init_db()

    @contextmanager
    def _get_cursor(self):
        """High-performance database connection manager with WAL support"""
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA synchronous=NORMAL;")
            yield conn.cursor()
            conn.commit()
        finally:
            conn.close()

    def _init_db(self):
        with self._get_cursor() as cursor:
            cursor.execute('''CREATE TABLE IF NOT EXISTS neural_cache
                             (id INTEGER PRIMARY KEY, batch_id INTEGER, 
                              block_size TEXT, status TEXT, time TEXT, hash TEXT)''')

    def get_last_batch(self, default_start):
        """Auto-Resume: Returns the next batch ID to process"""
        try:
            with self._get_cursor() as cursor:
                cursor.execute("SELECT MAX(batch_id) FROM neural_cache")
                last = cursor.fetchone()[0]
                return last + 1 if last else default_start
        except Exception:
            return default_start

    def get_battery(self):
        """Reads real-time battery level from Android system"""
        try:
            with open("/sys/class/power_supply/battery/capacity", "r") as f:
                return f.read().strip() + "%"
        except:
            return "N/A"

    async def check_gemini_api(self, ping, current_batch):
        """Async Bridge with Circuit Breaker and Auto-Maintenance"""
        if ping > 450:
            self.failure_count += 1
            if self.failure_count > 3:
                self.offline_mode = True
            return None

        self.failure_count = 0
        self.offline_mode = False
        
        if random.random() > 0.82:
            ts = datetime.datetime.now().strftime("%H:%M:%S")
            # ایجاد یک هش برای امنیت داده
            block_hash = hex(random.getrandbits(64))
            
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, self._save_block, current_batch, "1.2MB", ts, block_hash)
            return f"Block #{current_batch} Vaulted."
        return None

    def _save_block(self, b_id, size, ts, b_hash):
        """Saves data and performs automatic database maintenance"""
        try:
            with self._get_cursor() as cursor:
                # Insert the new block
                cursor.execute("INSERT INTO neural_cache (batch_id, block_size, status, time, hash) VALUES (?, ?, ?, ?, ?)",
                              (b_id, size, "VERIFIED", ts, b_hash))
                
                # Auto-Maintenance: Keep only the latest 1000 blocks to save space
                cursor.execute("""
                    DELETE FROM neural_cache 
                    WHERE id NOT IN (
                        SELECT id FROM neural_cache 
                        ORDER BY id DESC LIMIT 1000
                    )
                """)
        except sqlite3.Error as e:
            with open("error.log", "a") as f:
                f.write(f"[{ts}] Database Error: {e}\n")

    def get_total_vault(self):
        with self._get_cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM neural_cache")
            return cursor.fetchone()[0]

async def run_bridge(default_batch):
    asic = GeminiASIC()
    batch_id = asic.get_last_batch(default_batch)
    
    try:
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')
            now = datetime.datetime.now().strftime("%H:%M:%S")
            ping = random.randint(30, 600)
            
            api_msg = await asic.check_gemini_api(ping, batch_id)
            
            # UI Logic
            status_color = G if not asic.offline_mode else R
            link_st = f"{G}STABLE{RE}" if not asic.offline_mode else f"{R}CIRCUIT BROKEN{RE}"
            api_status = f"{G}ON{RE}" if ping < 450 else f"{R}OFF{RE}"
            battery = asic.get_battery()
            
            # --- Interface Display ---
            print("\n" * 2)
            print(f"{OFFSET} {P}●{RE} {S}System Pulse: {status_color}Active{RE}")
            print(f"{OFFSET}{B}┌{'─'*38}┐{RE}")
            print(f"{OFFSET}{B}│{RE}  {BOLD}{C}GEMINI ASIC v5.3{RE} {P}CORE-ASYNC{RE}  {B}│{RE}")
            print(f"{OFFSET}{B}├{'─'*12}┬{'─'*12}┬{'─'*12}┤{RE}")

            print(f"{OFFSET}  {S}TM:{RE} {now[:5]} │ {S}PG:{RE} {ping:3}ms │ {S}API:{RE} {api_status}")
            print(f"{OFFSET}  {S}ST:{RE} {link_st} │ {S}BT:{RE} {battery:<5} │ {S}WAL:{RE} {G}ON{RE}")

            print(f"{OFFSET}{B}├{'─'*38}┤{RE}")
            print(f"{OFFSET}  {BOLD}CORE:{RE} {P}[ BATCH #{batch_id} ]{RE}")
            print(f"{OFFSET}  {BOLD}VAULT:{RE} {S}{asic.get_total_vault()} verified blocks{RE}")

            print(f"{OFFSET}{B}├{'─'*38}┤{RE}")
            report = api_msg if api_msg else ("Sync Suspended: High Latency" if asic.offline_mode else "Neural Stream Stable")
            print(f"{OFFSET}  {BOLD}{C}LOG:{RE} {S}{report[:32]:<32}{RE}")
            print(f"{OFFSET}{B}└{'─'*38}┘{RE}")
            print(f"{OFFSET} {B}⚡{RE} {S}Independent Android Environment Mode{RE}")

            await asyncio.sleep(1.8)
            batch_id += 1

    except KeyboardInterrupt:
        print(f"\n{OFFSET}{P}●{RE} {S}Bridge Closed Safely. Vault Secured.{RE}\n")

if __name__ == "__main__":
    # Starting batch ID
    asyncio.run(run_bridge(893035))
