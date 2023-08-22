#!\use\bin\python3
import kivy
import threading
#app and sofware
kivy.require("1.9.0")
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

'''
Screen, ScreenManager with kivy  python 3 login GUI application
'''

#change size
Window.size = (500, 500)
#numbre of colors from 00.00
n_of_colors = 255.00
#create color window 0.00 is black
Window.clearcolor = (0.00/n_of_colors, 0,0 ,0)

class MainWindow(Screen):
    pass;

class SecondWindow(Screen):
    pass;

class WindowManager(ScreenManager):
    pass;

#load kivy file.kv or string
load_file_kivy = Builder.load_string(f"""
WindowManager:
    MainWindow:
    SecondWindow:
<MainWindow>:
    name: "main"
    GridLayout:
        cols:1
        GridLayout:
            cols: 1
            Label:
                text: "Password: "
            TextInput:
                id: passw
                multiline: False
        Button:
            text: "Next Screen"
            on_release:
                app.root.current = "second"
                root.manager.transition.direction = "left"
<SecondWindow>:
    name: "second"
    Button:
        text: "Go Back"
        on_release:
            app.root.current = "main"
            root.manager.transition.direction = "right"
            """)
#build app
class multiscreens(App):

    def build(self):
        self.title = 'multiscreens'
        self.icon = "multiscreens.png"
        return load_file_kivy

#run app
if __name__ == "__main__":
    th = threading.Thread(target=multiscreens().run())
    th.start()