import time
import sys
import os

def draw_dashboard(batch, uptime, cores):
    # پاک کردن صفحه برای ایجاد افکت داشبورد ثابت
    os.system('clear')
    
    blue = "\033[94m"
    cyan = "\033[96m"
    green = "\033[92m"
    bold = "\033[1m"
    reset = "\033[0m"
    
    current_time = time.strftime("%H:%M:%S")
    
    # ساختن قاب داشبورد
    print(f"{blue}╔" + "═"*45 + "╗{reset}")
    print(f"{blue}║{reset}  {bold}GOOGLE AI SOLAR SOFT-ASIC v2.0{reset}        {blue}║{reset}")
    print(f"{blue}╠" + "═"*45 + "╣{reset}")
    print(f"{blue}║{reset}  CURRENT TIME: {cyan}{current_time}{reset}               {blue}║{reset}")
    print(f"{blue}║{reset}  SYSTEM UPTIME: {cyan}{uptime} seconds{reset}           {blue}║{reset}")
    print(f"{blue}║{reset}  ACTIVE ENGINES: {green}{cores} Cores{reset}               {blue}║{reset}")
    print(f"{blue}╠" + "═"*45 + "╣{reset}")
    print(f"{blue}║{reset}  {bold}TOTAL WORK COMPLETED:{reset}                 {blue}║{reset}")
    print(f"{blue}║{reset}  {green}>> [ BATCH: {batch:08} ] <<{reset}          {blue}║{reset}")
    print(f"{blue}╚" + "═"*45 + "╝{reset}")
    print(f"\n{cyan}   STATUS: FEEDING GEMINI WITH SOLAR POWER...{reset}")

# پارامترهای فرضی برای شروع سریع (این‌ها در دل کد اصلی تو جا می‌گیرند)
try:
    batch_count = 5233 # شروع از جایی که بودی
    start_time = time.time() - 132 # فرض زمان سپری شده
    cores = 8
    
    while True:
        batch_count += 1
        uptime = int(time.time() - start_time)
        
        # آپدیت کردن داشبورد
        draw_dashboard(batch_count, uptime, cores)
        
        # سرعت پردازش
        time.sleep(0.5) 
        
except KeyboardInterrupt:
    print("\n[!] Dashboard Halted.")
