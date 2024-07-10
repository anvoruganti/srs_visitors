from kivy.app import App # type: ignore
from kivy.uix.screenmanager import ScreenManager # type: ignore
from frontend.screens.scanner_screen import ScannerScreen
from frontend.screens.visitor_info_screen import VisitorInfoScreen

class VisitorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ScannerScreen(name='scanner'))
        sm.add_widget(VisitorInfoScreen(name='visitor_info'))
        return sm