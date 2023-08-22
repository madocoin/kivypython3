#!use\bin\python3
import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

#load your file.kv
Builder.load_string(r'''
<Button>:
    title: 'floatlyaout'
    font_size: 30
    color: 0.6,0.5,0.6,5
    size_hint: 0.5,0.5

<FloatLayout>:
    Button:
        text: "simple FloatLayout"
        pos_hint: {"x":0.5, "top":1}

    Button:
        id: btn
        text:"Button" if btn.state == "normal" else "down"''')

class Floatlayout(App):
    def build(self):
        self.title = 'floatlayout'
        self.icon = 'floatlayout.png'
        return FloatLayout()

#run
if __name__ == "__main__":
    Floatlayout().run()