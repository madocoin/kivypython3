#!use\bin\python3
import kivy
#for app and software
kivy.require('1.9.0')
from time import sleep
from kivy.app import App
#for chow title and icon
from kivy.core.window import Window

'''create name of app
    the name of app is the name of class with first alpha is upper (capital)
    with the object of app is App
OR:
   App().run()#simple app
'''
# with build fonction
class Simple_app(App):
    def build(self):
    	#add icon, png
    	self.icon = 'arabic_lang.png'
    	#name of app
    	self.title = 'with language arabic مع اللغة العربية'


if __name__ == '__main__':
    #run app Simple_app
    app = Simple_app()
    app.run()
    # for stop
    app.stop()