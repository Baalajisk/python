from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
def display(instance):
    print('username:%s'%txt1.text)
    print('password:%s'%txt2.text)



class Loginform(App):
    def build(self):
        flayout=FloatLayout()
        l1=Label(text='user name',size_hint=(.1,.05),pos=(200,500))
        l2=Label(text='password',size_hint=(.1,.05),pos=(200,450))
        global txt1
        txt1=TextInput(text='',size_hint=(.2,.05),pos=(300,500))
        global txt2
        txt2=TextInput(text='',size_hint=(.2,.05),pos=(300,450))
        btn=Button(text='click',pos=(300,400),size_hint=(.2,.05))
        btn.bind(on_press=display)
        flayout.add_widget(l1)
        flayout.add_widget(txt1)
        flayout.add_widget(l2)
        flayout.add_widget(txt2)
        flayout.add_widget(btn)
        return flayout
Loginform().run()
    
        
