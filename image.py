#!use\bin\python3
import kivy
#for app or software
kivy.require('1.9.0')
from kivy.app import App
from random import randint
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage 
#numbre of colors
n_of_colors = 255
#random color
color = randint(0, n_of_colors)
#create color window
Window.clearcolor = (color/n_of_colors, 0,0 ,0)
#size of window
Window.size = (300, 500)

class Simple_app(App):

    def build(self):
        #build image
        image = Image(
            source = 'icon.png',#€path of image.png
            size_hint_x = 1,
            size_hint_y = 1,
            pos= (2,1 ), 
            opacity= 1
            );

        self.icon = 'image.png'
        self.title = 'Image'
        return(image)

'''
#for online image.
class Simple_app(App):

    def build(self):
        #build image from website
        AsyncImage = AsyncImage(
            source = 'image.png',#url of image.png, gpng
            size_hint_x = 1,
            size_hint_y = 1,
            pos= (2,1 ), 
            opacity= 1
            );

        self.icon = 'image.png'
        self.title = 'Image'
        return(AsyncImage)
'''
if __name__ == '__main__':
    #run app Simple_app
    Simple_app().run()