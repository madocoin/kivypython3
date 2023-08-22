#!\use\bin\python3
import kivy
kivy.require('1.9.0')# app and software
kivy.require('1.0.8')# ScrollView version
from kivy.app import App
from random import randint
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

'''ScrollView with GridLayout and Button in kivy python 3 '''

#numbre of colors
n_of_colors = 255.00
#random color rom 00.00 to 255.00
color = randint(5, n_of_colors)
# title app
#create color window
Window.clearcolor = (color/n_of_colors, 0,0 ,0)
#change size
Window.size = (500, 500)
#build app Scrollview
class Scrollview(App):

    def build(self):
        self.icon = 'ScrollView.png'
        self.title = 'ScrollView'
        # create a default grid_layout with custom width/height
        layout = GridLayout(cols=1, padding=20, spacing=20,
                size_hint=(None, None), height=500);

        # bind gridlyaout into gridlyaout
        layout.bind(minimum_height=layout.setter('height'))

        # add buttons to gridlyaout
        for i in range(10):
            btn = Button(text=str(f' Button Number {i}'), size=(480, 40),
                         size_hint=(None, None))
            layout.add_widget(btn)

        # create a scrollview
        root = ScrollView(size_hint=(None, None), size=(500, 320),
                pos_hint={'center_x': .5, 'center_y': .5}, do_scroll_x=False)
        #add scrollview to GridLayout 
        root.add_widget(layout); return(root)

if __name__ == '__main__':
    Scrollview().run()