#!use\bin\python3
import kivy
#for app and software
kivy.require("1.9.0")
from kivy.app import App

'''
simple app without name, icon, png, image ....
App().run()
'''

'''create name of app
    the name of app is the name of class with first alpha is upper (capital)
    with the object of app is App
    for example 
'''
# for rename app software
'''
from kivy.core.window import Window
class Simple_app(App):
    def build(self):
    	self.icon = 'Path of your icon, png...'
    	self.title = 'build button'''
class Simple_app(App):

	def build(self):
		pass;

if __name__ == '__main__':
    #run app Simple_app
    Simple_app().run()