from kivy.uix.screenmanager import Screen # type: ignore
from kivy.uix.boxlayout import BoxLayout # type: ignore
from kivy.uix.button import Button # type: ignore
from kivy.uix.camera import Camera # type: ignore
from kivy.clock import Clock # type: ignore
from frontend.utils.qr_scanner import scan_qr_code
import requests # type: ignore

class ScannerScreen(Screen):
    def __init__(self, **kwargs):
        super(ScannerScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True, resolution=(640, 480))
        self.scan_button = Button(text='Scan QR Code', on_press=self.scan_qr)
        layout.add_widget(self.camera)
        layout.add_widget(self.scan_button)
        self.add_widget(layout)

    def scan_qr(self, instance):
        self.camera.export_to_png("qr_image.png")
        Clock.schedule_once(self.process_image, 0.1)

    def process_image(self, dt):
        new_id = scan_qr_code("qr_image.png")
        if new_id:
            try:
                response = requests.get(f'http://localhost:5000/visitor_pass/{new_id}')
                if response.status_code == 200:
                    visitor_data = response.json()['VisitorPass']
                    self.manager.get_screen('visitor_info').update_visitor_info(visitor_data)
                    self.manager.current = 'visitor_info'
                else:
                    print("Error fetching visitor data")
            except requests.RequestException as e:
                print(f"Network error: {e}")
        else:
            print("No QR code found")