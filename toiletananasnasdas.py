from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.image import Image
from ins import *
p1,p2,p3 = 0,0,0
new_age = 0
a = 0

 #1111111111111111111111111111111111111111111111111111111111111111111111111  
class Main1(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        label2 = Label(text = inst2, size_hint=(1,0.5),
                      pos_hint={"y":0.5, "center_x":0.5})
                      
        but2 = Button(text = "Почати тестування", size_hint=(0.35,0.15),
                      pos_hint={"y":0.01, "center_x":0.5})
        
        

        lineF = FloatLayout(size_hint=(1,1))
        lineF.add_widget(label2)
        
        
        lineF.add_widget(but2)

        self.add_widget(lineF)
        but2.on_press = self.next_win

    def next_win(self):
        self.manager.current = 'main2'
        self.manager.transition.direction = "up"
#22222222222222222222222222222222222222222222222222222222222222222222222222
class Main2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        label2 = Label(text = inst3, size_hint=(1,0.5),
                      pos_hint={"y":0.5, "center_x":0.5})
                      
        but2 = Button(text = "Далі", size_hint=(0.35,0.15),
                      pos_hint={"y":0.01, "center_x":0.5})
        city = TextInput(multiline=False,size_hint=(0.35,0.05),
                      pos_hint={"y":0.5, "center_x":0.5} )
        
        lineF = FloatLayout(size_hint=(1,1))
        lineF.add_widget(label2)
        lineF.add_widget(city)
        
        lineF.add_widget(but2)

        self.add_widget(lineF)
        but2.on_press = self.next_win

    def next_win(self):
        self.manager.current = 'main3'
        self.manager.transition.direction = "up"

#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
class Main3(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        label2 = Label(text = inst4, size_hint=(1,0.5),
                      pos_hint={"y":0.5, "center_x":0.5})
                      
        but2 = Button(text = "Продовжуєм", size_hint=(0.35,0.15),
                      pos_hint={"y":0.01, "center_x":0.5})
        age = TextInput(multiline=False,size_hint=(0.35,0.05),
                      pos_hint={"y":0.5, "center_x":0.5} )
        
        lineF = FloatLayout(size_hint=(1,1))
        lineF.add_widget(label2)
        lineF.add_widget(age)
        
        lineF.add_widget(but2)

        self.add_widget(lineF)
        but2.on_press = self.next_win

    def next_win(self):
        self.manager.current = 'main4'
        self.manager.transition.direction = "up"


#44444444444444444444444444444444444444444444444444444444444444444444444444444444
class Main4(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        label2 = Label(text = inst5, size_hint=(1,0.5),
                      pos_hint={"y":0.5, "center_x":0.5})
                      
        but2 = Button(text = "Продовжити", size_hint=(0.35,0.15),
                      pos_hint={"y":0.01, "center_x":0.5})
        mounth = TextInput(multiline=False,size_hint=(0.35,0.05),
                      pos_hint={"y":0.5, "center_x":0.5} )
        
        lineF = FloatLayout(size_hint=(1,1))
        lineF.add_widget(label2)
        lineF.add_widget(mounth)
        
        lineF.add_widget(but2)

        self.add_widget(lineF)
        but2.on_press = self.next_win

    def next_win(self):
        self.manager.current = 'main5'
        self.manager.transition.direction = "up"

#55555555555555555555555555555555555555555555555555555555555555555555555555555555
class Main5(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        label2 = Label(text = inst6, size_hint=(1,0.5),
                      pos_hint={"y":0.5, "center_x":0.5})
                      
        but2 = Button(text = "Продовжити", size_hint=(0.35,0.15),
                      pos_hint={"y":0.01, "center_x":0.5})
        male_or_female = TextInput(multiline=False,size_hint=(0.35,0.05),
                      pos_hint={"y":0.5, "center_x":0.5} )
        
        lineF = FloatLayout(size_hint=(1,1))
        lineF.add_widget(label2)
        lineF.add_widget(male_or_female)
        
        lineF.add_widget(but2)

        self.add_widget(lineF)
        but2.on_press = self.next_win

    def next_win(self):
        self.manager.current = 'main6'
        self.manager.transition.direction = "up"

#666666666666666666666666666666666666666666666666666666666666666666666666666666666666
class Main6(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        label2 = Label(text = inst2, size_hint=(1,0.5),
                      pos_hint={"y":0.5, "center_x":0.5})
                      
        but2 = Button(text = "Продовжити", size_hint=(0.35,0.15),
                      pos_hint={"y":0.01, "center_x":0.5})
        male_or_female = TextInput(multiline=False,size_hint=(0.35,0.05),
                      pos_hint={"y":0.5, "center_x":0.5} )
        
        lineF = FloatLayout(size_hint=(1,1))
        lineF.add_widget(label2)
        lineF.add_widget(male_or_female)
        
        lineF.add_widget(but2)

        self.add_widget(lineF)
        but2.on_press = self.next_win

    def next_win(self):
        self.manager.current = 'main6'
        self.manager.transition.direction = "up"



class Win(App):
    def build(self):

        main_screen= ScreenManager()
      
        main_screen.add_widget(Main1(name='main1'))
        main_screen.add_widget(Main2(name='main2'))
        main_screen.add_widget(Main3(name='main3'))
        main_screen.add_widget(Main4(name='main4'))
        main_screen.add_widget(Main5(name='main5'))
        main_screen.add_widget(Main6(name='main6'))
        return main_screen

app = Win()
app.run()
