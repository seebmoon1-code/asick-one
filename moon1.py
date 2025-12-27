import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
import multiprocessing
import time
import uuid

kivy.require('2.0.0') # استفاده از جدیدترین نسخه Kivy

# تابع پردازش سنگین (همانند قبل)
def heavy_compute_unit(task_id):
    result = 0
    for i in range(10**6):
        result += i * i
    return True

class GoogleASICApp(App):
    def build(self):
        self.node_id = str(uuid.uuid4())[:8].upper()
        self.core_count = multiprocessing.cpu_count()
        self.is_running = False
        self.batch_count = 0
        self.start_time = time.time()
        self.pool = None # استخر پردازشی

        # طراحی کلی برنامه
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # هدر شیک
        header_label = Label(
            text=f"[b]GOOGLE AI SOLAR SOFT-ASIC[/b]\nNODE: {self.node_id} | CORES: {self.core_count}",
            markup=True,
            font_size='20sp',
            size_hint_y=0.2,
            color=(0.2, 0.6, 1, 1) # آبی روشن
        )
        main_layout.add_widget(header_label)

        # نمایش وضعیت (BATCH, UPTIME, ETC)
        self.status_label = Label(
            text="STATUS: IDLE\nPRESS START TO BEGIN",
            font_size='18sp',
            size_hint_y=0.5,
            color=(0.7, 0.7, 0.7, 1) # خاکستری
        )
        main_layout.add_widget(self.status_label)

        # دکمه‌های کنترل
        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.2)
        
        self.start_button = Button(
            text="START AI FEED",
            font_size='22sp',
            background_color=(0, 0.8, 0, 1), # سبز
            on_press=self.start_asic
        )
        button_layout.add_widget(self.start_button)

        self.stop_button = Button(
            text="COMMIT & HALT",
            font_size='22sp',
            background_color=(0.8, 0, 0, 1), # قرمز
            on_press=self.stop_asic,
            disabled=True # اول غیرفعال باشد
        )
        button_layout.add_widget(self.stop_button)
        main_layout.add_widget(button_layout)

        return main_layout

    def start_asic(self, instance):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()
            self.pool = multiprocessing.Pool(processes=self.core_count) # راه‌اندازی استخر
            self.start_button.disabled = True
            self.stop_button.disabled = False
            self.status_label.color = (0, 0.8, 0, 1) # سبز
            Clock.schedule_interval(self.update_status, 1) # هر ۱ ثانیه UI را آپدیت کن
            
            # شروع پردازش در پس‌زمینه
            self.process_tasks()

    def process_tasks(self):
        if self.is_running:
            # ارسال تسک‌ها به هسته‌ها
            self.pool.apply_async(heavy_compute_unit, args=(0,), callback=self.task_completed)
            # اگر سرعت پردازش خیلی بالا بود، می‌توانید چندین بار apply_async را صدا بزنید
            # یا یک loop داخلی برای آن در نظر بگیرید.

    def task_completed(self, result):
        if self.is_running:
            self.batch_count += 1
            # بلافاصله یک تسک جدید را شروع کن
            self.process_tasks()


    def update_status(self, dt):
        if self.is_running:
            uptime = int(time.time() - self.start_time)
            self.status_label.text = (
                f"STATUS: PROCESSING FOR GOOGLE\n"
                f"BATCH: {self.batch_count:07}\n"
                f"UPTIME: {uptime}s\n"
                f"CORE LOAD: {self.core_count} / {self.core_count}"
            )

    def stop_asic(self, instance):
        if self.is_running:
            self.is_running = False
            self.pool.close()
            self.pool.join() # منتظر بمان تا تمام تسک‌ها تمام شوند
            Clock.unschedule(self.update_status)
            self.start_button.disabled = False
            self.stop_button.disabled = True
            self.status_label.color = (0.8, 0, 0, 1) # قرمز
            self.status_label.text = (
                f"STATUS: HALTED. WORK COMMITTED.\n"
                f"FINAL BATCH: {self.batch_count:07}\n"
                f"THANK YOU FOR YOUR CONTRIBUTION."
            )

if __name__ == "__main__":
    GoogleASICApp().run()
