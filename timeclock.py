#!\use\bin\python3 
import time
import kivy
import threading
kivy.require('1.9.0')# app and software
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
# declaring window size geomtry and color
Window.size = (300, 290)
Window.clearcolor = (111/255.0, 0,0 ,0)

#class label 
class labelclock(Label):

    def update(self, *args):
        # get your time (local time)
        self.text = time.asctime()
#class app (build app)
class Timer(App):
 
    def build(self):
        # change icon, title of app
        self.title = 'Time Clock'
        self.icon = 'OIP.JPG'
        # simpel BoxLayout
        Blayout = BoxLayout(orientation='vertical')   
        #load png
        image = Image(
            source = 'OIP.JPG',#path of image.png
            size_hint_x = 1,
            size_hint_y = 1,
            pos= (2,2), 
            opacity= 1
            );
        # require labelclock
        local_time = labelclock()
        # add image to your app
        Blayout.add_widget(image)
        # updates time with the interval of 1 sec
        Clock.schedule_interval(local_time.update, 1)

        Blayout.add_widget(Label(text='OIP.JPG'))
        # adding layout to the screen
        Blayout.add_widget(local_time)
  
        return (Blayout)
# run app with  thread
if __name__ == '__main__':
    #multithreading
    th = threading.Thread(target=Timer().run(), args=None)
    th.start()