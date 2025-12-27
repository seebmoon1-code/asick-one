import os
import time
import random
import datetime
import hashlib

# --- UI Setup ---
C, G, B, R, Y, BOLD, RE = '\033[96m', '\033[92m', '\033[94m', '\033[91m', '\033[93m', '\033[1m', '\033[0m'

class SolarAsicV3:
    def __init__(self):
        self.sd_file = "asic_data.bin"
        self.cache_size = 0

    def sync_and_clean(self, ping):
        if ping < 150 and os.path.exists(self.sd_file):
            size = os.path.getsize(self.sd_file)
            os.remove(self.sd_file) # تخلیه خودکار
            return f"CLEANED ({size}b)"
        return "SYNCED" if ping < 150 else "CACHING"

def run_v3(batch_id):
    asic = SolarAsicV3()
    while True:
        os.system('clear')
        now = datetime.datetime.now().strftime("%H:%M:%S")
        ping = random.randint(30, 600)
        gpu = random.randint(88, 95)
        
        # Logic for SD storage
        if ping > 200:
            with open(asic.sd_file, "a") as f: f.write(f"{batch_id}\n")
            asic.cache_size = os.path.getsize(asic.sd_file)
        
        status_msg = asic.sync_and_clean(ping)

        # --- Compact UI (Fixed Width) ---
        print(f"{B}╔{'═'*45}╗{RE}")
        print(f"{B}║{RE} {C}{BOLD}SOLAR SOFT-ASIC v3.0 PRO{RE} {G}(HYBRID){RE}  {B}║{RE}")
        print(f"{B}╠{'═'*14}╦{'═'*14}╦{'═'*15}╣{RE}")
        print(f"  {BOLD}TM:{RE} {now} │ {BOLD}PG:{RE} {R if ping>200 else G}{ping:3}ms{RE} │ {BOLD}SD:{RE} {asic.cache_size}b")
        print(f"  {BOLD}GP:{RE} {gpu}%     │ {BOLD}RM:{RE} 100MB   │ {BOLD}TP:{RE} {G}40°C{RE}")
        print(f"{B}╟{'─'*45}╢{RE}")
        print(f"  {BOLD}BATCH:{RE} {G}{batch_id:08d}{RE}  │ {BOLD}STATUS:{RE} {Y}{status_msg}{RE}")
        print(f"  {BOLD}LINK:{RE} {C}GEMINI-SOLAR-LINK-ACTIVE{RE}")
        print(f"{B}╟{'─'*45}╢{RE}")
        
        # Short logs
        log = "Saving to SD..." if ping > 200 else "Cloud Sync OK."
        print(f" {B}LOG:{RE} {log}")
        print(f"{B}╚{'═'*45}╝{RE}")

        time.sleep(1.5)
        batch_id += random.randint(15, 40)

if __name__ == "__main__":
    run_v3(888159)
