#!\use\bin\python3
import kivy
kivy.require('1.9.0')
from kivy.app import App
from random import randint
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scatter import ScatterPlane

#numbre of colors
n_of_colors = 255.00
#random color rom 00.00 to 255.00
color = randint(5, n_of_colors)
# title app
#create color window
Window.clearcolor = (color/n_of_colors, 0,0 ,0)
#change size
Window.size = (500, 500)

class MyScatterplane(App):

    def build(self):
        s = ScatterPlane(scale=.5)
        l1 = Label(text='ScatterPlane l1', font_size=60, pos=(400, 100), mipmap=1)
        l2 = Label(text='ScatterPlane l2', font_size=100, pos=(400, 328))
        showlabel = Label(text='hi from scatter', font_size=50, pos=(200, 150))

        s.add_widget(showlabel)
        s.add_widget(l1)
        s.add_widget(l2)
        return s

if __name__ == '__main__':
    MyScatterplane().run()