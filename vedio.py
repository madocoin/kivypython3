#!\use\bin\python3
import kivy
import threading
kivy.require('1.9.0')
from kivy.app import App
from random import randint
from kivy.uix.video import Video
from os.path import join, dirname
from kivy.core.window import Window
'''
run your videos with python kivy video
'''
#numbre of colors
n_of_colors = 255.00
#random color rom 00.00 to 255.00
color = randint(5, n_of_colors)
#create color window
Window.clearcolor = (color/n_of_colors, 0,0 ,0)
#window size
Window.size = (300, 300)

class VideoApp(App):

    def build(self):
    	#title, icon of app with App kivy
    	self.title = 'Video'
    	self.icon = 'video.png'
    	# get path of directory vedio
    	vediodirect = join(dirname(__file__), 'vedio.mkv')
    	if True:
    	    return(Video(source=vediodirect, play=True))

if __name__ == '__main__':
	#multithreading (run speed)
 	thread = threading.Thread(target= VideoApp().run(), args=None)
 	thread.start()