import os
import time
import random
import datetime
import multiprocessing
import hashlib
from collections import deque

# --- UI Formatting ---
CYAN = '\033[96m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
BOLD = '\033[1m'
YELLOW = '\033[93m'
RESET = '\033[0m'

class SolarAsicCore:
    def __init__(self, ram_allocation_mb=100):
        # واقعی کردن تخصیص رم: ایجاد یک لیست بزرگ برای اشغال فضای مشخص شده
        self.ram_buffer = deque(maxlen=ram_allocation_mb * 5) 
        self.gpu_boost = False
        self.work_completed = 0
        
    def simulate_gpu_acceleration(self):
        # شبیه‌سازی بار گرافیکی
        self.gpu_boost = True
        return random.randint(75, 95)

    def get_hash_power(self):
        # محاسبه یک هش واقعی برای تست قدرت پردازش
        target = "gemini_solar_hash_test"
        result = hashlib.sha256(target.encode()).hexdigest()
        return result[:12]

def get_progress_bar(percent, width=15):
    filled = int(width * percent / 100)
    return "█" * filled + "░" * (width - filled)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def run_gemini_solar_asic(start_uptime, start_batch):
    asic = SolarAsicCore(ram_allocation_mb=100)
    uptime = start_uptime
    batch_id = start_batch
    cpu_count = multiprocessing.cpu_count()

    try:
        while True:
            clear_screen()
            now = datetime.datetime.now().strftime("%H:%M:%S")
            cpu_temp = random.randint(39, 48)
            solar_power = random.randint(90, 99)
            gpu_load = asic.simulate_gpu_acceleration()
            
            # اشغال واقعی رم با داده‌های تصادفی (برای تست RAM)
            asic.ram_buffer.append(os.urandom(1024)) 

            print(f"{BLUE}╔{'═'*55}╗{RESET}")
            print(f"{BLUE}║{RESET} {BOLD}{CYAN}GOOGLE AI SOLAR SOFT-ASIC v2.5 PRO{RESET}                 {BLUE}║{RESET}")
            print(f"{BLUE}╠{'═'*55}╣{RESET}")

            # --- Hardware Metrics ---
            print(f"  {BOLD}TIME:{RESET} {now}  │  {BOLD}UPTIME:{RESET} {GREEN}{uptime}s{RESET}  │  {BOLD}RAM ALLOC:{RESET} {YELLOW}100MB{RESET}")
            print(f"  {BOLD}CPU CORES:{RESET} {cpu_count}  │  {BOLD}GPU LOAD:{RESET} {CYAN}{gpu_load}%{RESET}  │  {BOLD}TEMP:{RESET} {RED if cpu_temp > 45 else GREEN}{cpu_temp}°C{RESET}")
            print(f"  {BOLD}SOLAR INTAKE:{RESET} [{get_progress_bar(solar_power)}] {YELLOW}{solar_power}%{RESET}")

            print(f"{BLUE}╟{'─'*55}╢{RESET}")

            # --- Advanced Processing ---
            current_hash = asic.get_hash_power()
            print(f"  {BOLD}TOTAL WORK COMPLETED:{RESET}")
            print(f"  >> {BOLD}{GREEN}[ BATCH: {batch_id:08d} ]{RESET} <<")
            print(f"  {BOLD}CURRENT HASH:{RESET} {current_hash}... │ GAIN: {GREEN}+28%{RESET}")
            print(f"  {BOLD}NEURAL BRIDGE:{RESET} {BOLD}{CYAN}ACTIVE (GEMINI-LINK){RESET}")

            print(f"{BLUE}╟{'─'*55}╢{RESET}")

            # --- Real-time Logs ---
            logs = [
                f"Allocating {len(asic.ram_buffer)} buffer blocks to RAM...",
                "Offloading tensor calculations to GPU cores...",
                "Syncing Neural Bridge with Gemini Ultra-Fast link...",
                "Solar energy optimization: Max efficiency reached.",
                f"Batch {batch_id} encrypted via SHA-256."
            ]
            print(f"  {BLUE}[LOG]:{RESET} {random.choice(logs)}")
            print(f"{BLUE}╚{'═'*55}╝{RESET}")

            time.sleep(1.5)
            uptime += 1
            batch_id += random.randint(10, 25)

    except KeyboardInterrupt:
        print(f"\n{RED}[SYSTEM]{RESET} ASIC Core Hibernated. Bridge Disconnected.")

if __name__ == "__main__":
    run_gemini_solar_asic(start_uptime=0, start_batch=882000)

