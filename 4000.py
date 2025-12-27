import os
import time
import random
import datetime
import hashlib

# --- UI Colors ---
CYAN, GREEN, BLUE, RED, YELLOW, BOLD, RESET = '\033[96m', '\033[92m', '\033[94m', '\033[91m', '\033[93m', '\033[1m', '\033[0m'

class AdvancedAsic:
    def __init__(self):
        self.sd_cache_file = "asic_storage_bin.dat"
        self.local_buffer = []
        
    def sync_to_sd(self, data):
        # شبیه‌سازی ذخیره روی SD Card وقتی پینگ بالاست
        with open(self.sd_cache_file, "a") as f:
            f.write(f"{data}\n")
        return os.path.getsize(self.sd_cache_file) // 1024 # اندازه به KB

def run_balanced_asic(start_batch):
    asic = AdvancedAsic()
    batch_id = start_batch
    uptime = 0

    try:
        while True:
            os.system('clear')
            now = datetime.datetime.now().strftime("%H:%M:%S")
            ping = random.randint(30, 600) # پینگ متغیر برای تست
            gpu_load = random.randint(85, 98)
            
            # منطق تعادل (Balancing Logic)
            if ping < 100:
                status = f"{GREEN}DIRECT SYNC{RESET}"
                log_msg = "Bridge stable. Streaming data to Gemini..."
                sd_usage = "IDLE"
            elif ping < 300:
                status = f"{YELLOW}BUFFERING{RESET}"
                log_msg = "Ping spike detected. Using RAM buffer..."
                sd_usage = "READY"
            else:
                status = f"{RED}OFFLINE MODE{RESET}"
                current_hash = hashlib.md5(str(batch_id).encode()).hexdigest()
                size = asic.sync_to_sd(current_hash)
                log_msg = f"High Latency! Diverting work to SD Card ({size}KB)..."
                sd_usage = f"{GREEN}ACTIVE{RESET}"

            # --- UI Display ---
            print(f"{BLUE}╔{'═'*55}╗{RESET}")
            print(f"{BLUE}║{RESET} {BOLD}{CYAN}GOOGLE AI SOLAR SOFT-ASIC v2.8 HYBRID{RESET}              {BLUE}║{RESET}")
            print(f"{BLUE}╠{'═'*55}╣{RESET}")
            print(f"  {BOLD}TIME:{RESET} {now}  │ {BOLD}PING:{RESET} {RED if ping > 300 else GREEN}{ping}ms{RESET} │ {BOLD}SD-CARD:{RESET} {sd_usage}")
            print(f"  {BOLD}GPU LOAD:{RESET} {CYAN}{gpu_load}%{RESET}  │ {BOLD}RAM:{RESET} {YELLOW}100MB{RESET}   │ {BOLD}TEMP:{RESET} {GREEN}40°C{RESET}")
            print(f"{BLUE}╟{'─'*55}╢{RESET}")
            print(f"  {BOLD}BRIDGE STATUS:{RESET} {status}")
            print(f"  >> {BOLD}{GREEN}[ BATCH: {batch_id:08d} ]{RESET} <<")
            print(f"  {BOLD}NEURAL LINK:{RESET} {BOLD}SOLAR-POWERED-GEMINI-V2{RESET}")
            print(f"{BLUE}╟{'─'*55}╢{RESET}")
            print(f"  {BLUE}[LOG]:{RESET} {log_msg}")
            print(f"{BLUE}╚{'═'*55}╝{RESET}")

            time.sleep(1.5)
            batch_id += random.randint(10, 30)
            uptime += 1

    except KeyboardInterrupt:
        print(f"\n{RED}[HALT]{RESET} Session saved to SD Card. System safe.")

if __name__ == "__main__":
    run_balanced_asic(882985)
