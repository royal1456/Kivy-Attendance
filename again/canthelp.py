from kivy.app import App
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty

'''
default_size: None, dp(5)-- decrease size of selectable
default_size_hint: 0.5, None--shifts all to left

'''
Builder.load_string('''
#:import random random.random
<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_size: None, dp(40)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True

<CustomScreen>:
    hue: random()
    canvas:
        Color:
            hsv: self.hue, .5, .3
        Rectangle:
            size: self.size

    Label:
        font_size: 42
        text: root.name

    Button:
        text: 'Next screen'
        size_hint: None, None
        pos_hint: {'right': 1}
        size: 150, 50
        on_release: root.manager.current = root.manager.next()

<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size

<RVScreen>:
    FloatLayout:
        size_hint:1,0.5
        orientation: "vertical"
        Button:
            pos_hint:{"y":1.4}
            text: 'up'
            on_release:
                root.s()
    FloatLayout:
        size_hint:1,0.5
        orientation: "vertical"
        RV:
            data:root.data
        
''')


class CustomScreen(Screen):
    hue = NumericProperty(0)


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected
        if is_selected:
            print("selection changed to {0}".format(rv.data[index]))
        else:
            print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    def rm(self):
        #self.clear_widgets()
        self.refresh_from_data()

    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        print([{'text': str(x)} for x in range(20)])


class RVScreen(Screen):
    data=ListProperty([])
    def s(self):
        self.data = [{'text': "('Monday', '20-08-2019', 5, 7, 'w')"}, {'text': "('Friday', '2-8-2019', 5, 7, 'w')"}, {'text': "('Thursday', '15-8-2019', 0, 0, 'h')"},{'text': "('Monday', '20-08-2019', 5, 7, 'w')"}, {'text': "('Friday', '2-8-2019', 5, 7, 'w')"}, {'text': "('Thursday', '15-8-2019', 0, 0, 'h')"},{'text': "('Monday', '20-08-2019', 5, 7, 'w')"}, {'text': "('Friday', '2-8-2019', 5, 7, 'w')"}, {'text': "('Thursday', '15-8-2019', 0, 0, 'h')"},{'text': "('Monday', '20-08-2019', 5, 7, 'w')"}, {'text': "('Friday', '2-8-2019', 5, 7, 'w')"}, {'text': "('Thursday', '15-8-2019', 0, 0, 'h')"}]
class ScreenManagerApp(App):

    def build(self):
        root = ScreenManager()
        root.add_widget(CustomScreen(name='CustomScreen'))
        root.add_widget(RVScreen(name='RVScreen'))
        return root


if __name__ == '__main__':
    ScreenManagerApp().run()
