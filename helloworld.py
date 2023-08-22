import kivy
#app and software
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
#load simpel code string kivy.kv with builder
Builder.load_string('''
<Hello>:
    text: 'Hello World'
''')

class Hello(Label):
    pass;

class SampleApp(App):
    def build(self):
        self.icon = 'helloworld.png'
        self.title = 'Hello World'
        return Hello()

'''run app'''
if __name__ == "__main__":
    SampleApp().run()