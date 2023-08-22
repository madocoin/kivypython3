#!\use\bin\python3
import kivy
kivy.require("1.9.0")#apps and softwares
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.core.window import Window

Window.size = (500, 300)
Window.icon = 'stigproperty.png'
#Simple file kivy.kv wiyh load string
kv = Builder.load_string(r"""
<runStringProperty>
    orientation:"vertical"
    Label:
        id:mylabel
        text:root.stringProperty_mylabel
    Button:
        text: "if you click her will be return -> (StringProperty) in you consel"
        on_press: root.printMe()
    """)

class runStringProperty(BoxLayout):
    stringProperty_mylabel= StringProperty("StringProperty")

    def printMe(self):
    	try:
    		print(self.stringProperty_mylabel)
    	except Exception as e:
    		print(f'Exception Error{e}')
    		pass;

class stringProperty(App):

    def build(self):
        return runStringProperty()

#run app
stringProperty().run()