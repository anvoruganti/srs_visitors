from kivy.uix.screenmanager import Screen # type: ignore
from kivy.uix.boxlayout import BoxLayout # type: ignore
from kivy.uix.label import Label # type: ignore
from kivy.uix.button import Button # type: ignore
import requests # type: ignore

class VisitorInfoScreen(Screen):
    def __init__(self, **kwargs):
        super(VisitorInfoScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.info_label = Label(text="Visitor Information")
        self.checkin_button = Button(text="Check In", on_press=self.check_in)
        self.layout.add_widget(self.info_label)
        self.layout.add_widget(self.checkin_button)
        self.add_widget(self.layout)

    def update_visitor_info(self, visitor_data):
        self.visitor_data = visitor_data
        self.info_label.text = f"Name: {visitor_data['FullName']}\nContact: {visitor_data['ContactNumber']}\nEmail: {visitor_data['EmailAddress']}\nStatus: {'Checked In' if visitor_data['IsCheckedIn'] else 'Not Checked In'}"
        self.checkin_button.disabled = visitor_data['IsCheckedIn']

    def check_in(self, instance):
        try:
            response = requests.post('http://localhost:5000/visitor_checkin', json={"NewId": self.visitor_data['NewId']})
            if response.status_code == 200:
                print("Visitor checked in successfully")
                self.visitor_data['IsCheckedIn'] = True
                self.update_visitor_info(self.visitor_data)
            else:
                print("Error checking in visitor")
        except requests.RequestException as e:
            print(f"Network error: {e}")