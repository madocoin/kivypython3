import kivy
kivy.require('1.9.0')
from kivy.app import App
from random import randint
from kivy.uix.label import Label 
from kivy.uix.scatter import Scatter
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

'''
simple app for changed Window
'''
#numbre of colors
n_of_colors = 255
#random color
color = randint(0, n_of_colors)
#create color window
Window.clearcolor = (color/n_of_colors, 0,0 ,0)
#you canchange size
Window.size = (600, 800)

'''create name of app
    the name of app is the name of class with first alpha is upper (capital)
    with the object of app is App
    for example 
'''
class Simple_app(App):
    def build(self):
        # title, icon of app
        self.icon = 'scatter_and_floatlayout.png'
        self.title= 'Scatter and FloatLayout'
        f = FloatLayout()
        s = Scatter()
        l = Label(text= 'Scatter and FloatLayout in Label',
        	font_size= 50)
        f.add_widget(s)
        s.add_widget(l)
        return(f)

if __name__ == '__main__':
    #run app Simple_app
    Simple_app().run()