#!use\bin\python3
import kivy
from kivy.app import App
from random import randint
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage 
#for app or software
kivy.require('1.9.0')
#numbre of colors
n_of_colors = 255
#random color
color = randint(0, n_of_colors)
#create color window
Window.clearcolor = (color/n_of_colors, 0,0 ,0)
#change size
Window.size = (300, 500)

class Setup_install_kivy(App):

    def build(self):
        #build image
        image = Image(
            source = 'setup_install_kivy.png',#path of image.png
            size_hint_x = 1,
            size_hint_y = 1,
            pos= (2,1 ), 
            opacity= 1
            );

        self.icon = 'setup_install_kivy.png'
        self.title = 'setup_install_kivy'
        return(image)

if __name__ == '__main__':
    #run app Simple_app
    Setup_install_kivy().run()