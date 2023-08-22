#!use\bin\python3
import kivy
#app and software
kivy.require('1.9.0')
from kivy.app import App
from random import randint
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.core.window import Window
#numbre of colors
n_of_colors = 255
#create color window
rand= randint(0, 250)
Window.clearcolor = (rand/n_of_colors, 0,0 ,1)
#change size
Window.size = (300, 600)
class MyApp(App):
    def build(self):
        self.title= 'runTouchApp'
        self.icon= 'runtouchapp.png'
#kivy code string
runTouchApp(Builder.load_string(r'''

ActionBar:
    pos_hint:{'top':1}
    ActionView:
        ActionPrevious:
            title:'runTouchApp'
        ActionButton:
            text:"ActionButton"
        ActionGroup:
            text:"ActionGroup"
            color:.3,.6,2,1
            ActionButton:
                text:"ActionButton2"
            ActionButton:
                text:"ActionButton3"
            ActionButton:
                text:"ActionButton4"
                '''))
