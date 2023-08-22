#!use\bin\python3
import kivy
#pp & software
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
#Gridlyaout with Oops
class MyGrid(GridLayout):

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        #you can change self.cols and show what happen
        self.cols = 2

        self.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.add_widget(self.lastName)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

if __name__ == '__main__':

    class gridlayout(App):

        def build(self):
            self.icon = 'gridlyaout.png'
            return(MyGrid())
    #run app        
    if True:
        gridlayout().run()