from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Widgets(Widget):
    pass


class SimpleKivy(App):
    def build(self):
        return Widgets()

def hi():
    print('hi da')

if __name__=="__main__":
    SimpleKivy().run()


