#!use\bin\python3
import kivy
import pathlib
import threading
#import skip_dirs
kivy.require('1.9.0')# app and software
from kivy.app import App
from os.path import dirname, join
from kivy.core.window import Window
from kivy.uix.videoplayer import VideoPlayer

Window.size = (400, 400)
Window.title = 'VideoPlayer python3'
Window.clearcolor = (222//255.0, 0,0 ,0)
'''
run and play your mp4 video, moves, clip player with python kivy kv
'''
path = str("vedio.MKV")

class VideoPlay(App):

    def build(self):
    	# path of you vedio mp4 in source
    	return(VideoPlayer(source=f"{path}", state='stop'))

#run app with multithrading
if __name__ == '__main__':
	th = threading.Thread(target=VideoPlay().run())
	th.start()
