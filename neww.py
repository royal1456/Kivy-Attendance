from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
''' pos_hint: {"x":0.5, "top":1}
'''
# capital is imp and position also(kicy kv calling change fixed error)  # exception unknown windwow manager
class Updating(Screen):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
    pass


Builder.load_string("""#:import Spinner kivy.uix.spinner
<Updating>:
    name:"update"
    Spinner:
        size_hint:0.3,0.2
        pos_hint :{'x': .35, 'y':.75}
        text: 'Python'
        values :["Python", "Java"]
        on_value:
""")


class MyMainApp(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return Updating()


if __name__ == "__main__":
    MyMainApp().run()
