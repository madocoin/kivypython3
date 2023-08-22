#!use\bin\python3
'''
simpel app timer with kivy python 3
'''
import sys
import kivy
import datetime
# app + software
kivy.require('1.9.0')
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import BooleanProperty, StringProperty
Config.set('graphics', 'width', '450')
Config.set('graphics', 'height', '100'); Config.write()

time_clock = datetime.datetime.now()# your time
#input your time down with minutes
input = int(input('entre your time down minutes _$'))#integer
#assert(60>=input>=1)
#load your str; file.kv
Builder.load_string("""
<Timer>:
    button: button
    Button:
        id: button
        on_press: root.click()
    AnchorLayout:
        Label:
            text: "%s:%s" % (root.minutes, root.seconds)
            font_size: 50
""")

class Timer(FloatLayout):
    minutes = StringProperty()
    seconds = StringProperty()
    running = BooleanProperty(False)#bool[True, False]

    def __init__(self, **kwargs):
        super(Timer, self).__init__(**kwargs)
        self.sound = SoundLoader.load('sound.wav')#load your sound
        self.delta = datetime.datetime.now()+datetime.timedelta(0, 60*input)
        self.update()
    # start count 
    def start(self):
        if not self.running:
            self.running = True
            Clock.schedule_interval(self.update, 0.01)
    # stop count
    def stop(self):
        if self.running:
            self.running = False
            Clock.unschedule(self.update)
    #new count down
    def update(self, *kwargs):
        delta = self.delta - datetime.datetime.now()
        self.minutes, seconds = str(delta).split(":")[1:]
        self.seconds = seconds[:5]
	
        if int(self.minutes) == 0:
            if int(self.seconds.split(".")[0]) == 0:
                if int(self.seconds.split(".")[1]) < 20:
                    self.seconds = "00.00"
                    self.button.background_color = (144,0,0,0)
                    self.sound.play()
                    self.stop()
    # for stop crono if start else start crono
    def click(self):
        self.sound.play()
        if self.running:
            self.stop()
        else:
            self.start()
#run app
if __name__ == '__main__':

    class TimerApp(App):
        def build(self):
            return(Timer())

    #multthreading
    import threading
    threading.Thread(target=TimerApp().run()).start()