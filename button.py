#!use\bin\python3
import kivy
kivy.require('1.9.0')
from kivy.app import App
from random import randint
from kivy.core.window import Window
from kivy.uix.button import Button

'''
simple app for changed colors
'''
#numbre of colors
n_of_colors = 255
#random color
color = randint(0, n_of_colors)
# title app
#create color window
Window.clearcolor = (color/n_of_colors, 0,0 ,0)
#change size
Window.size = (300, 500)

'''create name of app
    the name of app is the name of class with first alpha is upper (capital)
    with the object of app is App
    for example 
'''
# with button
class Simple_app(App):
    def build(self):
        # title, icon of app
        self.icon = 'button.png'
        self.title= 'app with button'
    	#button
        button = Button(
        	text='Click',
        	size_hint=(.33, .3),#width, heith
        	pos_hint={'x':0.5,'y':.4},# left -> x, top -> y
            color=(1, 1, 1, 1),# color text
            background_color=(0, 0, 0.8, 1)# back ground of color
        ) 
        return(button)

if __name__ == '__main__':
    #run app Simple_app
    Simple_app().run()