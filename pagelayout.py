from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

class pagelayout(PageLayout):
    pass

class page(App):
    def build(self):
        return pagelayout()

page().run()
