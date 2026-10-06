from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
import time

class TachoApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Заголовок
        self.label_title = Label(
            text="Тахограф / Режимы труда и отдыха", 
            font_size='20sp', 
            size_hint=(1, 0.1),
            bold=True
        )
        self.main_layout.add_widget(self.label_title)

        # Таймер / Статус
        self.label_status = Label(
            text="Статус: Отдых\nВремя: 00:00:00", 
            font_size='24sp', 
            size_hint=(1, 0.2)
        )
        self.main_layout.add_widget(self.label_status)

        # Кнопки управления
        btn_layout = GridLayout(cols=2, spacing=10, size_hint=(1, 0.3))
        
        btn_drive = Button(text="Вождение", background_color=(0.2, 0.8, 0.2, 1))
        btn_drive.bind(on_press=lambda x: self.set_status("Вождение"))
        
        btn_rest = Button(text="Отдых", background_color=(0.2, 0.6, 1, 1))
        btn_rest.bind(on_press=lambda x: self.set_status("Отдых"))

        btn_work = Button(text="Работа", background_color=(1, 0.6, 0.2, 1))
        btn_work.bind(on_press=lambda x: self.set_status("Работа"))

        btn_break = Button(text="Перерыв 45m", background_color=(0.8, 0.8, 0.2, 1))
        btn_break.bind(on_press=lambda x: self.set_status("Перерыв"))

        btn_layout.add_widget(btn_drive)
        btn_layout.add_widget(btn_rest)
        btn_layout.add_widget(btn_work)
        btn_layout.add_widget(btn_break)

        self.main_layout.add_widget(btn_layout)

        # Инициализация переменных
        self.current_mode = "Отдых"
        self.start_time = time.time()
        
        # Обновление каждую секунду
        Clock.schedule_interval(self.update_timer, 1)

        return self.main_layout

    def set_status(self, mode):
        self.current_mode = mode
        self.start_time = time.time()
        self.update_timer(0)

    def update_timer(self, dt):
        elapsed = int(time.time() - self.start_time)
        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.label_status.text = f"Режим: {self.current_mode}\nПрошло: {time_str}"

if __name__ == '__main__':
    TachoApp().run()
