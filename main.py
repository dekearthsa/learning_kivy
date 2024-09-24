from kivy.uix.dropdown import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView

class TestingSizeHint(BoxLayout):
    pass

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
