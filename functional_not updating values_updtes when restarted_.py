'''
pHint = size of calendar

size_hint = size of text label

imp for correct placements:
     size: self.texture_size
    size_hint: None,None
popup is edited and called externally
never forget that super.init()
init has no self for object property but need 1 when accesing
float layots's size hint is only accesed not pos hint

https://stackoverflow.com/questions/49935190/kivy-how-to-initialize-the-viewclass-of-the-recycleview-dynamically
'''
'''
-------------bug----------
init problems for class--Solved
date sapcing in update-
rv-popup?--dropped 4 now
reading from file blocks highlight in set()
centering te text in databse label
'''
# Program to Show how to create a switch
# import kivy module
import kivy
from kivy.factory import Factory
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
from kivy.uix.spinner import Spinner
# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
kivy.require('1.9.0')
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
# Builder is used when .kv file is
# to be used in .py file
from kivy.lang import Builder
from kivy.core.window import Window
# The screen manager is a widget
# dedicated to managing multiple screens for your application.
from kivy.uix.screenmanager import ScreenManager, Screen
import datepicker
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.slider import Slider
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from att_interactdb import database
import datetime
# Window.size = (550, 700)


#-------------to be changed at interaction-------------


max = 7
default = 5
max_view = 5  # days
daysoff = 2
days_val = 'Saturday,Sunday'
data = 'none'  # string vala none xD
error = 'none'
db = None


def set_data():
    global max, max_view, default, daysoff, days_val, data, error, db
    with open('settings.txt', 'w+') as f:
        f.write('lec_in_day:' + str(max) + '\n')
        f.write('daysoff:' + str(daysoff) + '\n')
        f.write('days_val:' + str(days_val) + '\n')
        f.write('lec_default:' + str(default) + '\n')
        f.write('max_days:' + str(max_view) + '\n')  # max views
        f.write('Data:' + str(data))


def get_data():
    global max, max_view, default, daysoff, days_val, data, error, db
    try:
        with open('settings.txt', 'r') as f:
            values = [x.split(':') for x in f.read().split('\n')]
            max = int(values[0][1])
            daysoff = int(values[1][1])
            days_val = values[2][1]
            default = int(values[3][1])
            max_view = int(values[4][1])
            data = values[5][1]
    except:
        error = 'unable to read database'
        print(error)
        set_data()
        get_data()


get_data()


def set_database():
    global max, max_view, default, daysoff, days_val, data, error, db
    db = database(max, data)
    db.create()


Builder.load_string("""
#:import Factory kivy.factory.Factory


##------------------Essentials---------------------------


<SelectableLabel>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size

<MultiSelectOption@ToggleButton>:
    size_hint: 1, None
    height: '48dp'

<Customlabel@Label>:
    color:0,0,0,1
    font_size:44
    multiline:True
    text_size: root.width, None
    size: self.texture_size
    size_hint_y: None  ##imp

<Custombutton@Button>:
    font_size: 24
    size_hint: None,None
    focus:True

<Custominput@TextInput>:
    size_hint: .12,.07
    font_size:30
    text_size: root.width, None
    focus:True
    multiline:False
    padding:(40,5)

<Infopopup>:
    auto_dismiss: False
    title:"Invalid Entry"
    label:label
    size_hint:0.5,0.5
    FloatLayout:
        Customlabel:
            id:label
            pos_hint:{'x':0.015,'y':0.5}
            font_size:23
        Custombutton:
            size_hint:0.2,0.2
            pos_hint:{'x':0.4,'y':0.16}
            text: 'OK'
            on_release: root.dismiss()

<MyPopup>:
    auto_dismiss: False
    title:"Confirm"
    label:label
    size_hint:0.5,0.5
    FloatLayout:
        Customlabel:
            id:label
            pos_hint:{'x':0.015,'y':0.6}
            font_size:23

        Custombutton:
            size_hint:0.2,0.2
            pos_hint:{'x':0.6,'y':0.16}
            text: 'Close'
            on_release: root.dismiss()
        Custombutton:
            size_hint:0.2,0.2
            pos_hint:{'x':0.2,'y':0.16}
            text: 'Save'
            on_release:root.my_widget.submit()


<Submitbutton@Button>:
    font_size: 24
    size_hint: None,None
<RV>:
    viewclass: 'SelectableLabel'
    SelectableRecycleBoxLayout:
        default_pos_hint:{"x":0.3}
        default_size_hint: 0.5,0.4
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True



##------------------Main_interface---------------------------



<MainWindow>:
    name:"main"
    FloatLayout:
        padding : 10, 10
        Customlabel:
            text:'Attendance Monitiring'
            pos_hint:{'x':0.3,'y':0.9}
        Custombutton:
            pos_hint:{'x':0.05,'y':0.45}
            text: "update"
            on_release:
                app.root.current = "update"
                root.manager.transition.direction = "left"
        Custombutton:
            pos_hint:{'x':0.05,'y':0.05}
            text: "Settings"
            on_release:
                app.root.current = "set"
                root.manager.transition.direction = "left"
        Custombutton:
            pos_hint:{'x':0.55,'y':0.05}
            text: "delete"
            on_release:
                app.root.current = "delete"
                root.manager.transition.direction = "left"
        Custombutton:
            pos_hint:{'x':0.55,'y':0.45}
            text: "View"
            on_release:
                app.root.current = "View_data"
                root.manager.transition.direction = "left"



##------------------Update_data---------------------------



<Updating>:
    name:"update"
    datepickers:datepickers
    spinner_up_lt:spinner_up_lt
    spinner_up_la:spinner_up_la
    box_id:box_id

    FloatLayout:
        padding : 10, 10
        Customlabel:
            text:'Updating Data'
            pos_hint:{'x':0.3,'y':0.9}
        Submitbutton:
            size_hint:0.2,0.1
            pos_hint:{'x':0.4,'y':0.2}
            text:"submit"
            on_press:root.popup()
        Customlabel:
            text:"Enter Date:"
            font_size:30
            pos_hint:{'x':0.1,'y':0.7}
        DatePicker:   ##for calender handling------------------------kivy-ui-commands
            id:datepickers
            on_text:root.checkdate(self)
            pHint:(0.8,0.8)
            size_hint: .12,.07
            padding : 10, 10
            pos_hint:{'x':0.5,'y':0.7}
        Customlabel:
            text:"Lectures Attended:"
            font_size:30
            pos_hint:{'x':0.1,'y':0.6}
        Spinner:       ##for changing lectures attended-------------------------db-commands
            id:spinner_up_la
            text:'0'
            size_hint:0.12,0.07
            pos_hint:{'x':0.5,'y':0.6}
        Customlabel:
            text:"Lectures Took:"
            font_size:30
            pos_hint:{'x':0.1,'y':0.5}
        Spinner:       ##for changing lectures took-------------------------db-commands
            id:spinner_up_lt
            text:'0'
            size_hint:0.12,0.07
            pos_hint:{'x':0.5,'y':0.5}
        Customlabel:
            text:"Holiday"
            font_size:30
            pos_hint:{'x':0.1,'y':0.4}
        CheckBox:      ##for holiday cheking-------------------------------ui-command
            id: box_id
            size_hint:0.12,0.07
            pos_hint:{'x':0.5,'y':0.4}
            on_active: root.box_on(self,self.active)
            color:0,0,0,1
        Custombutton:
            font_size:14
            size_hint:0.06,0.06
            pos_hint:{"x":0.8,"y":0.85}
            text: "Home"
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "right"
                root.manager.transition.duration = 0.5



##------------------Delete_data---------------------------



<Deleting>:
    name:"delete"
    switch_id:switch_id
    slider:slider
    val:val
    FloatLayout:
        size_hint:1,0.5
        padding : 10, 10
        Customlabel:
            text:"deleting"
            pos_hint:{'x':0.3,'y':0.9+0.92}
        Customlabel:
            text:"Record of days:"
            pos_hint:{'x':0.1,'y':0.7+0.87}
            font_size:30

        Slider:
            id: slider
            size_hint:0.8,0.1
            pos_hint:{'x':0.1,'y':0.55+0.77}
            min: 1
            max: 2
            step: 1

        Customlabel:
            text: str(slider.value)
            pos_hint:{'x':0.5,'y':0.5+0.97}
            font_size:30
        Customlabel:
            text:"show data box:"
            pos_hint:{'x':0.1,'y':0.4+0.67}
            font_size:30
        Switch:
            id:switch_id
            size_hint:None,None
            pos_hint:{'x':0.4,'y':0.3+0.67}
            # self.active passes self,instance,value-which true or flase
            on_active: root.on_active(self,self.active)
        Custombutton:
            font_size:14
            size_hint:0.06,0.06
            pos_hint:{"x":0.8,"y":0.85+0.92}
            text: "Home"
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "right"
                root.manager.transition.duration = 0.5
    FloatLayout:
        size_hint:1,0
        id:val
        RV:



##------------------Set_data---------------------------



<Set>:
    name:"set"
    max_l:max_l
    days:days
    default_la:default_la
    spinner_up:spinner_up
    database_name:database_name
    FloatLayout:
        padding:10,10
        Customlabel:
            text:"Settings"
            pos_hint:{'x':0.3,'y':0.9}
        Customlabel:
            text:"Enter Max Lectures:"
            font_size:30
            pos_hint:{'x':0.1,'y':0.7}
        Custominput:
            id:max_l
            text:'7'
            pos_hint:{'x':0.6,'y':0.7}
        Customlabel:
            text:"Enter Default Lectures:"
            font_size:30
            pos_hint:{'x':0.1,'y':0.6}
        Custominput:
            id:default_la
            text:'5'
            pos_hint:{'x':0.6,'y':0.6}
        Customlabel:
            text:"Enter Max records to display:"
            font_size:30
            pos_hint:{'x':0.1,'y':0.5}
        Custominput:
            id:days
            text:'5'
            pos_hint:{'x':0.6,'y':0.5}
        Customlabel:
            text:"Enter Holidays:"
            font_size:30
            pos_hint:{'x':0.1,'y':0.4}
        MultiSelectSpinner:       ##for changing holidays took-------------------------db-commands
            id:spinner_up
            text:'Saturday,Sunday'
            padding:(10,10)
            text_size : self.width, None
            values:'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'
            size_hint:0.35,0.07
            pos_hint:{'x':0.6,'y':0.4}

        Submitbutton:
            size_hint:0.2,0.1
            pos_hint:{'x':0.4,'y':0.2}
            text:"submit"
            on_press:root.popup()
        Customlabel:
            text:"Enter person name:"
            font_size:30
            pos_hint:{'x':0.1,'y':0.3}
        Custominput:
            id:database_name
            padding:(20,5)
            size_hint: .35,.07
            text:'5'
            text_size : self.width, None
            pos_hint:{'x':0.6,'y':0.3}
        Custombutton:
            font_size:14
            size_hint:0.06,0.06
            pos_hint:{"x":0.8,"y":0.85}
            text: "Home"
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "right"
                root.manager.transition.duration = 0.5



##------------------View_data---------------------------



<View_data>:
    name:"view_data"
    FloatLayout:
        Customlabel:
            text:'Viewing Records'
            pos_hint:{'x':0.3,'y':0.9}
        Custombutton:
            font_size:14
            size_hint:0.06,0.06
            pos_hint:{"x":0.8,"y":0.85}
            text: "Home"
            on_release:
                app.root.current = "main"
                root.manager.transition.direction = "right"
                root.manager.transition.duration = 0.5
""")

# Create a class for all screens in which you can include
# helpful methods specific to that screen


class MainWindow(Screen):
    pass


#-------------------------------UPDATING----------------------------------


class Updating(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

#-----------Calling-Ids--------------Class-Variables-----------

        datepickers = ObjectProperty(None)
        spinner_up_lt = ObjectProperty(None)
        spinner_up_la = ObjectProperty(None)
        box_id = ObjectProperty(None)
        # self.t is aninstance of mypop and here self passed act as my_widget
        self.t = MyPopup(self)
        self.i = Infopopup(self)
        self.holiday = 'w'
        self.days = 'Monday'
        self.set()

#-----------Holidays-setting-------------------------

    def set_holiday(self):  # setting values for all spinners in case of holiday
        self.spinner_up_la.values = self.spinner_up_la.values = (
            '0')  # (total lectures equal)
        self.spinner_up_la.text = self.spinner_up_lt.text = '0'

    def box_on(self, instance, value):
        self.checkdate()
        if(value is True):
            self.set_holiday()
            self.holiday = 'h'
        else:
            self.holiday = 'w'

    def popup(self):
        text = "Confirm entery of " + self.datepickers.text + " as a " + \
            ("\n holiday" if(self.box_id.state == "active") else "\n working day.")
        self.t.open()
        self.t.label.text = text
        # self.t.label refers to label decalred in my_wifget in popup

    def checkdate(self, *args, **kwargs):
        global max, max_view, default, daysoff, days_val, data, error, db
        day, month, year = (int(i) for i in self.datepickers.text.split('-'))
        self.days = datetime.date(year, month, day).strftime("%A")
        if(self.days in days_val.split(',')):
            print('callllled')
            self.box_id.value = 'True'

    def submit(self):
        global max, max_view, default, daysoff, days_val, data, error, db
        print("called", self.datepickers.text)
        db.create()
        self.checkdate()
        try:
            db.insert(self.days, self.datepickers.text, int(self.spinner_up_la.text), int(
                self.spinner_up_lt.text), self.holiday)
        except:
            self.i.open()
            self.i.label.text = '\nINVALID ENTRY TO DATABASE\n\n ->Check Respective Constrain\n ->Chek for duplicate entries'
        print(db.show_all())  # -----------------testing
        self.set()
        self.t.dismiss()

#-----------Ideal-Settings--------------------------

    def set(self):
        global max, max_view, default, daysoff, days_val, data, error, db
        #-----------la-lt-being-setted-----------------------
        self.spinner_up_la.values = tuple([str(x) for x in range(max + 1)])
        # (total lectures equal)
        self.datepickers.text = ('-'.join(self.datepickers.text.split('/')))
        self.spinner_up_lt.values = self.spinner_up_la.values
        self.spinner_up_la.text = str(default)
        self.spinner_up_lt.text = str(max)
        self.box_id.value = 'False'
    pass


#------------------------DELETING_INTERFACE---------------------------------


class Deleting(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        switch_id = ObjectProperty(None)
        slider = ObjectProperty(None)
        val = ObjectProperty(None)
        self.set()

    def on_active(self, instance, value):
        print("caleed ", value)
        if (value is True):
            self.val.size_hint = 1, 0.5
            # self.x = FloatLayout(
            #     size_hint=(1, 0.5), id='val')
            # self.ids.val.add_widget(RV(id='y'))
        else:
            self.val.size_hint = 1, 0
            # self.remove_widget(self.x)

    def set(self):
        # self.data requires----------------- {'text': '9'}]--list pf dictonary
        self.slider.max = max_view
    pass


#------------------------SETTING_INTERFACE---------------------------------


class Set(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.t = MyPopup(self)
        max_l = ObjectProperty(None)
        days = ObjectProperty(None)
        default_la = ObjectProperty(None)
        spinner_up = ObjectProperty(None)
        database_name = ObjectProperty(None)
        self.sets()

    def popup(self):
        text = "Save Changes?"
        self.t.open()
        self.t.label.text = text

    def submit(self):
        print("Changes saved", self.max_l.text,
              self.days.text, self.default_la.text)
        self.set_help()  # global helping
        set_data()  # global_saving
        get_data()  # global adding
        self.t.dismiss()

    def set_help(self):
        global max, max_view, default, daysoff, days_val, data
        max = self.max_l.text
        max_view = int(self.days.text)  # max_view
        default = int(self.default_la.text)
        days_val = self.spinner_up.text
        daysoff = len(days_val.split(','))
        # no of days,sunday,saturdayetc
        data = str(self.database_name.text)

    def sets(self):
        self.max_l.text = str(max)
        self.days.text = str(max_view)  # max_view
        self.default_la.text = str(default)
        self.spinner_up.text = str(days_val)
        self.database_name.text = str(data)
        # Updating.set()
        # self.spinner_up.self.selected_values = ['Saturday', 'Sunday']
    pass


#------------------------VIEW_DATA_INTERFACE---------------------------------


class View_data(Screen):
    pass


#------------------------ESSENTIAL_REQUIREMENT---------------------------------


class MyPopup(Popup):
    # my_widget is now the object where popup was called from.
    def __init__(self, my_widget, **kwargs):
        super().__init__(**kwargs)
        self.my_widget = my_widget  # mywidget instance is used to accees child values
        label = ObjectProperty(None)
    pass


class MultiSelectSpinner(Button):
    """Widget allowing to select multiple text options."""

    dropdown = ObjectProperty(None)
    """(internal) DropDown used with MultiSelectSpinner."""

    values = ListProperty([])
    """Values to choose from."""

    selected_values = ListProperty([])
    """List of values selected by the user."""

    def __init__(self, **kwargs):
        self.bind(dropdown=self.update_dropdown)
        self.bind(values=self.update_dropdown)
        super(MultiSelectSpinner, self).__init__(**kwargs)
        self.bind(on_release=self.toggle_dropdown)

    def toggle_dropdown(self, *args):
        if self.dropdown.parent:
            self.dropdown.dismiss()
        else:
            self.dropdown.open(self)

    def update_dropdown(self, *args):
        if not self.dropdown:
            self.dropdown = DropDown()
        values = self.values
        if values:
            if self.dropdown.children:
                self.dropdown.clear_widgets()
            for value in values:
                b = Factory.MultiSelectOption(text=value)
                b.bind(state=self.select_value)
                self.dropdown.add_widget(b)

    def select_value(self, instance, value):
        if value == 'down':
            if instance.text not in self.selected_values:
                self.selected_values.append(instance.text)
        else:
            if instance.text in self.selected_values:
                self.selected_values.remove(instance.text)

    def on_selected_values(self, instance, value):
        if value:
            self.text = ', '.join(value)
        else:
            self.text = ''


class Infopopup(Popup):
    # my_widget is now the object where popup was called from.
    def __init__(self, my_widget, **kwargs):
        super().__init__(**kwargs)
        self.my_widget = my_widget  # mywidget instance is used to accees child values
        label = ObjectProperty(None)
    pass

# class--------------View_for_deletion---------


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
        return super().refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super().on_touch_down(touch):
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


class RV(RecycleView):  # ---------------------------popup?
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)

        self.data = [{'text': str(x)} for x in range(10)]

#---------up-----------------------------


#------------------------SCREEN_MANAGER---------------------------------


screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(MainWindow(name="main"))
screen_manager.add_widget(Updating(name="update"))
screen_manager.add_widget(Deleting(name="delete"))
screen_manager.add_widget(Set(name="set"))
screen_manager.add_widget(View_data(name="View_data"))
# Create the App class


#------------------------MAIN_CALLING---------------------------------


class ScreenApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        get_data()
        set_database()
        return screen_manager


# run the app
sample_app = ScreenApp()
sample_app.run()