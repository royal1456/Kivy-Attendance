from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.button import Button

''' pos_hint: {"x":0.5, "top":1}
'''
# capital is imp and position also(kicy kv calling change fixed error)  # exception unknown windwow manager


class Updating(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.popup = Infopopup(self)
        layout = ObjectProperty(None)

    def ok(self):
        print("in")
        self.popup.open()
        print("values of update", self.layout.height,
              self.layout.width)
        print("Values are", self.popup.height, self.popup.width, ",", self.popup.fout.height, self.popup.fout.width, ",",
              self.popup.fin1.height, self.popup.fin1.width, ",", self.popup.fin2.height, self.popup.fin2.width)
        print("Values are", self.popup.pos, ",", self.popup.fout.pos, ",",
              self.popup.fin1.pos,  ",",  self.popup.fin2.pos)


Builder.load_string("""#:import Spinner kivy.uix.spinner
<Infopopup>:
    auto_dismiss: False
    title:"Invalid Entry"
    fout:fout
    fin1:fin1
    fin2:fin2
    size_hint:0.5,0.5
    FloatLayout:
        pos_hint:{'center_y':.5,'center_x':.5}
        id:fout
        ##after dividing screen now .5,.5 is base_size all iszes will be added accordingly
        FloatLayout:
            id:fin1
            size_hint:1,0.5
            ##pos:root.width*.2, root.height / 2
            pos_hint:{'top':0.4,'center_x':0.2}
            Label:
                pos_hint:{'x':0,'y':0}
                text:'ll'
                font_size:23
            Button:
                size_hint:0.2,0.2
                pos_hint:{'x':1,'y':1}
                text: 'OK'
                on_release: root.dismiss()
            Button:
                size_hint:0.2,0.2
                pos_hint:{'x':1,'y':1}
                text: 'OK__top'
                on_release: root.dismiss()
        FloatLayout:
            id:fin2
            size_hint:1,0.5
            pos_hint:{'top':0.8,'center_x':0.2}
            Label:
                pos_hint:{'x':0,'y':0}
                text:'ll'
                font_size:23
            Button:
                size_hint:0.2,0.2
                pos_hint:{'x':1,'y':1}
                text: 'OK2'
                on_release: root.dismiss()

<Updating>:
    name:"update"
    layout:layout
    FloatLayout:
        id:layout
        Button:
            text:"press_here"
            on_release:root.ok()

""")


class Infopopup(Popup):
    # my_widget is now the object where popup was called from.
    def __init__(self, my_widget, **kwargs):
        super().__init__(**kwargs)
        fout = ObjectProperty(None)
        fin1 = ObjectProperty(None)
        fin2 = ObjectProperty(None)


class MyMainApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return Updating()


if __name__ == "__main__":
    MyMainApp().run()
