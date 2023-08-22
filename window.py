#!use\bin\python3
import kivy
#app and software version
kivy.require('1.9.0')
from kivy.app import App
from random import randint
from kivy.core.window import Window

'''
simple app with changed Window
'''
#numbre of colors
n_of_colors = 255.00
#random color rom 00.00 to 255.00
color = randint(5, n_of_colors)
# title app
#create color window
Window.clearcolor = (color/n_of_colors, 0,0 ,0)
#change size
Window.size = (500, 500)

'''create name of app
    the name of app is the name of class with first alpha is upper (capital)
    with the object of class is App for example 
'''
# with build
class Simple_app(App):
    def build(self):
        # title, icon of app
        self.icon = 'window.png'
        self.title= 'window with color'

if __name__ == '__main__':
    #run app Simple_app
    Simple_app().run()