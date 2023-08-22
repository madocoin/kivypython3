#!\use\bin\python3
import kivy
kivy.require("1.9.0")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line


class APPWidget(Widget):
	#super class
    def __init__(self, **kwargs):
        super(APPWidget, self).__init__(**kwargs)
        
        with self.canvas:
        	#coles and Rectangle size with add line
            Line(points=(15,23,100,200,15,200))
            Color(1,0,0,0.5, mode="rgba")
            self.rect = Rectangle(pos=(1,1), size=(50,80))

            Color(1,0,0,0.5, mode="rgba")
            self.rect = Rectangle(pos=(0,0), size=(50,50))
            Color(1,1,0,0.5,mode="rgba")
            self.rect2 = Rectangle(pos=(200,300), size=(100,50))


    def on_touch_down(self, touch):
        self.rect.pos = touch.pos

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos


if __name__ == '__main__':

	class Graphic(App):

		def build(self):
			self.icon = 'ghraphics.png'
			self.title = 'graphics'
			return(APPWidget())

    #run app
	Graphic().run()