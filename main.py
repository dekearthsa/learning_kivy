from kivy.app import App
from kivy.metrics import dp

from kivy.uix.pagelayout import PageLayout
from kivy.uix.dropdown import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen

import requests

class GUIControlToolsWidge(GridLayout):
    def push_upper(self):
        print("Upper")

    def push_left(self):
        print("Left")

    def push_down(self):
        print("Down")

    def push_right(self):
        print("Right")


class ManualScreen(Screen):
    pass

class AutoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.counting = 0

    def get_data_from_server(self):
        try:
            response = requests.get('http://localhost:2222/get')
            # print("response => ", response)
            json_d = response.json()
            # print("data => ",json_d)
            self.update_label_with_data(json_d['data'])
        except requests.RequestException as e:
            self.update_label_with_data(str(e))

    def update_label_with_data(self, data):
        self.counting += 1
        self.ids.data_label.text = data + "fetch count: " + str(self.counting)

class SettingScreen(Screen):
    pass

class LabHeaderWidget(BoxLayout):
    pass

class MainFrameWidget(BoxLayout):
    pass

class RelativeLayOutWidget(PageLayout):
    pass

class PageLayOutWidget(PageLayout):
    pass

### TestSize ###

class TestingSizeHint(BoxLayout):
    pass

class TestingGrid(GridLayout):
    pass

### TestSize end ###

class ScrollViewWidget(ScrollView):
    pass

class StackLayOutWidget(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 99):
            i += 1
            b = Button(text=str(i), size_hint=(None, None), size=(dp(100), dp(100)))
            self.add_widget(b)

class GridLayOutWidget(GridLayout):
    pass

class BoxLayOutWidget(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     b1 = Button(text="A")
    #     b2= Button(text="b")
    #     self.add_widget(b1)
    #     self.add_widget(b2)

# class MainWidget(Widget):
#     pass

class TheLabApp(App):
    pass
    # def build(self):
    #     return BoxLayOutWidget()

if __name__ == "__main__":
    TheLabApp().run()
