#!\use\bin\python3
#__all__
import kivy
import kivymd
kivymd.require('1.9.0')
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.uix.label import MDLabel, MDicon
from kivy.uix.video import Video
from kivy.base import runTouchApp
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Ellipse, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.image import Image, AsyncImage
from kivy.uix.floatlayout import FloatLayout
from kivym.properties import StringProperty, ObjectProperty

'''
you can use 2 fonctions in python for help your self and bbuild any code python 
                this fonctions is [dir([lib, module, class, fonction, method]),
                        help([lib, module, class, fonction, method])]
                                    with print() your outputs;

                                  print(dir(Video), help(Video))

this 2 fonctions work about show code, thicks, steups, ....
'''