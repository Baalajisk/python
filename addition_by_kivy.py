from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.image import Image as CoreImage

def show(instance):
    add=int(num1.text)+int(num2.text)
    print(add)

class TestApp(App):
    def build(self):
        b=BoxLayout(orientation='vertical')
        im="C:\\Users\\Admin\\Desktop\\hrithik.jpg"
        CoreImage.load(im)
        global num1
        num1=TextInput(text='')
        global num2
        num2=TextInput(text='')
        btn=Button(text='add')
        btn.bind(on_press=show)
        '''btn.bind(on_press=show)'''
        b.add_widget(num1)
        b.add_widget(num2)
        b.add_widget(btn)
        
        return b
TestApp().run()

