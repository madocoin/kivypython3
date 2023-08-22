#!use\bin\python3
import kivy
kivy.require('1.9.0')#virsion apps and software
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import ObjectProperty

#window size gyometry
Window.size = (500, 500)
# you can use this with file.kv and with the name of class == name of file.kv
Builder.load_string(f"""
<loginpage>:
    password: password
    email: email
    GridLayout:
        cols:1
        size: root.width - 200, root.height -200
        pos: 110, 110
        GridLayout:
            cols:2
            Label:
                text: "Password: "
            TextInput:
                id: password
                multiline:False
            Label:
                text: "Email: "
            TextInput:
                id: email
                multiline:False
        Button:
            text:"log_in"
            on_press: root.btn()""")
#Simple login GUI
class loginpage(Widget):
    password = ObjectProperty(None)#bool[True, False]
    email = ObjectProperty(None)#bool

    def btn(self):
        print("Password:", self.password.text, "email:", self.email.text)
        self.password.text = ""
        self.email.text = ""

class LoginGUI(App):

    def build(self):
        return loginpage()

#run app
if __name__ == "__main__":
    LoginGUI().run()