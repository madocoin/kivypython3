import kivy
#soft and apps
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Touch(Widget):
    obp = ObjectProperty(None)

    def on_touch_down(self, touch):
        print("Mouse Down", touch)

    def on_touch_move(self, touch):
        print("Mouse Move", touch)

    def on_touch_up(self, touch):
        print("Mouse UP", touch)


class MyApp(App):
    def build(self):
        self.title = 'tuch and mouse inputs'
        self.icon = 'tuchandmouse_input.png'
        return Touch()


if __name__ == "__main__":
    MyApp().run()