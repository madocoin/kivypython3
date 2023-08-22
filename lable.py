import kivy
#for run app and software
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.label import Label
#simple libel with kivy python3
class Simple_app(App):
    def build(self):
        # title, icon of app
        self.icon = 'lable.PNG'
        self.title= 'Label'
    	#simple label
        label = Label(text='Hi From Label', size=(50, 60))
        return(label)

if __name__ == '__main__':
    #run app Simple_app
    Simple_app().run()