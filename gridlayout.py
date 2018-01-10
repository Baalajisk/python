from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
def display(instance):
    print('username:%s'%txt1.text)
    print('password:%s'%txt2.text)



class Loginform(App):
    def build(self):
        glayout=GridLayout(cols=2)
        l1=Label(text='user name')
        l2=Label(text='password')
        global txt1
        txt1=TextInput(text='',width=50,height=50)
        global txt2
        txt2=TextInput(text='',width=50,height=50)
        btn=Button(text='click')
        btn.bind(on_press=display)
        glayout.add_widget(l1)
        glayout.add_widget(txt1)
        glayout.add_widget(l2)
        glayout.add_widget(txt2)
        glayout.add_widget(btn)
        return glayout
Loginform().run()
    
        
