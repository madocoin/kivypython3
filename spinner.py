#!\use\bin\python3
import kivy
kivy.require("1.9.0")
from kivy.app import App
from kivy.uix.spinner import Spinner

spinner = Spinner(
    text='spinner',
    values=('valuespinner1', 'valuespinner2', 'valuespinner3', 'valuespinner4'),
    size_hint=(None, None), size=(100, 50),
    pos_hint={'center_x': .5, 'center_y': .5})

'''
you can use spiner.bind(text='your text output');
'''
class Spinner(App):

	def build(self):
		self.icon = 'spinner.png'
		self.title = "spiner"
		return((spinner))

if __name__ == '__main__':
	Spinner().run()