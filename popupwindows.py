#!\use\bin\python3
import kivy
#apps and software
kivy.require("1.9.0")
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

#numbre of colors from 00.00
n_of_colors = 255.00
#create color window 0.00 is black
Window.clearcolor = (00.00/n_of_colors, 0,0 ,0)
#change size
Window.size = (500, 500)

#upload file kv kivy to string or file with Builder.load_file(kivy.kv)
loadkvstring = Builder.load_string(r'''
<Widgets>:
    Button:
        text: "click Her"
        on_release: root.btn()

<fout>:
    Label:
        text: "You pressed the button"
        size_hint: 0.5, 0.5
        pos_hint: {"x":0.2, "top":1}

    Button:
        text: "You pressed the button"
        size_hint: 0.8, 0.2
        pos_hint: {"x":0.1, "y":0.1}
        ''')

def open_popup():
    show = fout();
    popupWindow = Popup(title="title of this popup windows", content=show, size_hint=(0.5,0.5),size=(300,300))
    popupWindow.open()

class Widgets(Widget):
    def btn(self):
        open_popup();

class fout(FloatLayout):
    pass;

class MyApp(App):
    def build(self):
        self.title = "Popup Window"
        self.icon = "popupwindows.png"
        return Widgets();

if __name__ == "__main__":
    MyApp().run()