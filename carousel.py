#!\use\bin\python3 
import kivy  
import random
kivy.require('1.9.0')#app and software (version)
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.carousel import Carousel
from kivy.uix.gridlayout import GridLayout

#numbre of colors in kivy python3
n_of_colors = 255.00
#random color rom 00.00 to 255.00
color = random.randint(100, n_of_colors)
#create color window
Window.clearcolor = (color/n_of_colors, 0,0 ,0)
#change size
Window.size = (450, 300)
#load your string kivy or file kivy with Builder.load_file(file.kv)
Builder.load_string(r'''
<gridlayout>:
    cols: 1#desin window
    Label:
        text: 'click next--> for new id\n' +'         '+ str( id({root}))
    Button:
        text: 'next-->'
        on_release:
            root.parent.parent.load_next()
    Button:
        text: '<--Back'
        on_release:
            root.parent.parent.load_previous()
''')

#require gridlayaout for show your buttons in kivy string, file
class gridlayout(GridLayout):
    pass;

#build app with corousel
class carousel(App):

    def build(self):
        root = Carousel()
        # x is number of pages
        for x in range(5):
            root.add_widget(gridlayout())
        return root;
        
#run the app
if __name__ == '__main__':
    carousel().run()