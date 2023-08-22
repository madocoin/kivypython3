#!use\bin\python3
import kivy
kivy.require('1.9.0')
from kivy.app import App
from random import randint
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
#numbre of colors
n_of_colors = 255
#random color
color = randint(0, n_of_colors)
# title app
#create color window
Window.clearcolor = (color/n_of_colors, 0,0 ,0)
#change size
Window.size = (300, 500)

class Simple_app(App):

    def build(self):
        self.icon = 'icon.png'
        self.title = 'text input'

        tin = TextInput(
            text='welcome to text_input',#words of first line input
            multiline=1,# newline -> bool
            font_size=10,#size of text
            size_hint=(0.5, 0.05), #size of hint box of textinput
            pos_hint={'x': 0.25, 'y': 0.5}#postion of textinput
            );

        return(tin)


if __name__ == '__main__':
    #run app Simple_app
    Simple_app().run()