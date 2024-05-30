from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class main(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lineV = BoxLayout(orientation="vertical", padding=8, spacing=8,size_hint= (0.8, None), height="200sp", pos_hint={'center_x': 0.5, "center_y": 0.5})
        self.text_input = TextInput(multiline = False,size_hint=(0.4, 0.07),pos_hint={"center_x": 0.5, "y" : 0})
        lineV.add_widget(self.text_input)
        but = Button(text="Розпочати",size_hint=(0.8, 0.05),pos_hint={"center_x": 0.5, "y" : 0}, background_color=(0,1,3,100))
        lineV.add_widget(but)

        

        



        self.add_widget(lineV)
def next_win(self):
    self.manager.current = "2"
    self.manager.transition.direction = "up"

class First(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lineV = BoxLayout(orientation="vertical", padding=8, spacing=8,size_hint= (0.8, None), height="200sp", pos_hint={'center_x': 0.5, "center_y": 0.5})
        self.text_input = TextInput(multiline = False,size_hint=(0.4, 0.07),pos_hint={"center_x": 0.5, "y" : 0})
        lineV.add_widget(self.text_input)
        but = Button(text="Розпочати",size_hint=(0.8, 0.05),pos_hint={"center_x": 0.5, "y" : 0}, background_color=(0,1,3,100))
        lineV.add_widget(but)


class Win(App):
    def build(self):
        Window.clearcolor= (1,1,0,1)
        Window.size = (400,600)
        main_screen = ScreenManager()
        main_screen.add_widget(main(name="main"))
        return main_screen










app = Win()
app.run()  