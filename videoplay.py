#!use\bin\python3
import kivy
import random
import pathlib
import threading
#import skip_dirs 'for skip dirs'
#from glob import glob
kivy.require('1.9.0')# app and software
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.video import Video
from os.path import dirname, join
#from display_dir_tree import tree
from kivy.core.window import Window
#from unique_path import unique_path
from kivy.uix.carousel import Carousel
from kivy.uix.gridlayout import GridLayout

'''
run and play your mp4 video, moves, clip player with python kivy kv 
'''

#load your string kivy or file kivy with Builder.load_file(file.kv)
Builder.load_string(r'''
<gridlayout>:
    cols: 1 #: desin window
    Button:
        text: '<--Back'
        on_release:
            root.parent.parent.load_previous()
    Video:# i have one video you can use for loop for more videos
        source: 'video.MKV'
        play: True

    Button:
        text: 'next-->'
        on_release:
            root.parent.parent.load_next()
''')

n_of_colors = 255.00 # the number of colors in kivy
#random color rom 00.00 to 255.00
color = random.randint(0, n_of_colors)
#create color window
Window.clearcolor = (color/n_of_colors, 0,0 ,0)
#change size
Window.size = (500, 300)

#get direct video
videodirect = join(dirname(__file__), 'video.MKV')

#for multivideos
if pathlib.Path(videodirect).exists(): 
    pass;
else: 
    pathin = repr(input('entree your video path here'))
    if pathlib.Path(pathin).exists():
        videodirect = pathin
    else:
        #you can use raise or assert method
        BaseException(f'this path--> {pathin} is not exists')
        print(r'''#entre your path video here for extract all videos from your path
path = repr(input('input your path videos'))
if  pathlib.Path(path).exists():
    pass;
else: 
    BaseException(f'this path--> {path} is not exists')
pathvideos = pathlib.Path(path).rglob("*")
listvideos = [item for item in pathvideos if item.is_file()]
listvideos = listvideos.append(videodirect) if videodirect else listvideos
''')
        exit(0)

#require gridlayaout for show your buttons and kivy code file
class gridlayout(GridLayout):
    pass;

#build app
class VideoPlay(App):

    def build(self):
        carousel = Carousel()
        # x is video from listvideo
        for x in range(4):
            carousel.add_widget(gridlayout())
        return carousel;

#run app with multithrading
if __name__ == '__main__':
	th = threading.Thread(target=VideoPlay().run())
	th.start()