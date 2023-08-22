#!use\bin\python3
from kivy.app import App
from random import randint
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
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
        self.icon = 'checkbox.png'
        self.title = 'CheckBox'

        box = CheckBox()
        return(box)

if __name__ == '__main__':
    #run app Simple_app
    Simple_app().run()