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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior, ButtonBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.slider import Slider
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from att_interactdb import database
import datetime
from functools import partial  # --animation progress bar circular
from kivy.clock import Clock
from kivy.core.text import Label as CoreLabel
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
import time
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
        error = 'Internl error code:unable to read database of settings'
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


# ------------------Essentials---------------------------


<SelectableLabel>:
    # Draw a background to indicate selection
    col_1:col_1
    col_2:col_2
    col_3:col_3
    col_4:col_4
    col_5:col_5
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        id:col_1
        text:'None'
    Label:
        id:col_2
        text:'None'
    Label:
        id:col_3
        text:'None'
    Label:
        id:col_4
        text:'None'
    Label:
        id:col_5
        text:'None'
<Imagebutton>:
    size_hint: (None, None)

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
        default_pos_hint:{"x":0.01,}
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        multiselect: True
        touch_multiselect: True



# ------------------Main_interface---------------------------



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



# ------------------Update_data---------------------------



<Updating>:
    name:"update"
    datepickers:datepickers
    spinner_up_lt:spinner_up_lt
    spinner_up_la:spinner_up_la
    box_id:box_id
    took_off:took_off
    notification:notification
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
        Customlabel:
            id:notification
            text:"(unchecking this box will make the holiday counted as working day)"
            font_size:12
            opacity: 0
            pos_hint:{'x':0.1,'y':0.38}

        CheckBox:      ##for holiday cheking-------------------------------ui-command
            id: box_id
            size_hint:0.12,0.07
            pos_hint:{'x':0.5,'y':0.4}
            on_active: root.box_on(self,self.active)
            color:0,0,0,1
        Customlabel:
            text:"Took Off"
            font_size:30
            pos_hint:{'x':0.1,'y':0.3}
        CheckBox:      ##for holiday taken-------------------------------ui-command
            id: took_off
            size_hint:0.12,0.07
            pos_hint:{'x':0.5,'y':0.3}
            on_active: root.took_off_day(self,self.active)
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



# ------------------Delete_data---------------------------



<Deleting>:
    name:"delete"
    switch_id:switch_id
    slider:slider
    val:val
    recycleview:recycleview
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
        Imagebutton:##--to update database
            pos_hint:{'x':0.6,'y':0.45+0.67}
            size_hint:0.1,0.07
            source:'icons/checkmark-outline.png'
            on_press:root.update()

        Imagebutton:##--to refresh text
            pos_hint:{'x':0.7,'y':0.45+0.67}
            size_hint:0.1,0.07
            source:'icons/refresh-outline.png'
            on_press:root.refresh()
        RV:
            id:recycleview




# ------------------Set_data---------------------------



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



# ------------------View_data---------------------------



<View_data>:
    name:"view_data"
    FloatLayout:
        cp:cp
        Customlabel:
            text:'Viewing Records'
            pos_hint:{'x':0.3,'y':0.9}
        CircularProgressBar:
            id:cp
            size_hint: (None, None)
            height: root.height*0.2
            width:  root.height*0.2
            max: 100
            pos_hint:{'x':0.4,'y':0.65}

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
        Clock.schedule_once(self._do_setup)
        # self.t is aninstance of mypop and here self passed act as my_widget
        self.set()

    def _do_setup(self, *args):
        datepickers = ObjectProperty(None)
        spinner_up_lt = ObjectProperty(None)
        spinner_up_la = ObjectProperty(None)
        box_id = ObjectProperty(None)
        took_off = ObjectProperty(None)
        notification = ObjectProperty(None)
        self.t = MyPopup(self)
        self.i = Infopopup(self)
        self.holiday = 'w'
        self.days = 'Monday'

#-----------Holidays-setting-------------------------

    def set_holiday(self):  # setting values for all spinners in case of holiday
        self.spinner_up_la.values = self.spinner_up_lt.values = (
            '0')  # (total lectures equal)
        self.spinner_up_la.text = self.spinner_up_lt.text = '0'

    def box_on(self, instance, value):
        print('called box on')
        if(value is True):
            self.set_holiday()
            self.notification.opacity = 1
            self.holiday = 'h'
            self.took_off.active = False
        else:
            # self.notification.font_size = 0
            self.notification.opacity = 0
            self.holiday = 'w'
            self.set_la_lt_default()

    def on_enter(self):
        print('/n \n entered called')

    def took_off_day(self, instance, value):
        print('caleed took off')
        if(value is True):
            self.box_id.active = False
            self.holiday = 'w'
            self.spinner_up_la.values = ('0')
            self.spinner_up_la.text = '0'
            print('took off called')
        else:
            self.checkdate()

    def popup(self):
        text = "Confirm entery of " + self.datepickers.text + " as a " + \
            ("\n holiday" if(self.box_id.state == "down") else "\n working day.")
        self.t.open()
        self.t.label.text = text
        # self.t.label refers to label decalred in my_wifget in popup

    def checkdate(self, *args, **kwargs):
        global max, max_view, default, daysoff, days_val, data, error, db
        day, month, year = (int(i) for i in self.datepickers.text.split('-'))
        self.days = datetime.date(year, month, day).strftime("%A")
        if(self.days in days_val.split(',')):
            print('callllled')
            self.box_id.active = True

    def submit(self):
        global error, db
        print("called submit", self.datepickers.text)
        db.create()
        self.checkdate()
        try:
            db.insert(self.days, self.datepickers.text, int(self.spinner_up_la.text), int(
                self.spinner_up_lt.text), self.holiday)
        except:
            self.i.open()
            self.i.label.text = '\nINVALID ENTRY TO DATABASE\n\n ->Check Respective Constrain\n ->Chek for duplicate entries'
        print(db.show_all(), db)  # -----------------testing
        self.set()
        self.t.dismiss()

    def set_la_lt_default(self):
        self.spinner_up_la.values = tuple([str(x) for x in range(max + 1)])
        # (total lectures equal)
        self.spinner_up_lt.values = self.spinner_up_la.values
        self.spinner_up_la.text = str(default)
        self.spinner_up_lt.text = str(max)

#-----------Ideal-Settings--------------------------

    def set(self):
        global max, max_view, default, daysoff, days_val, data, error, db
        #-----------la-lt-being-setted-----------------------
        self.datepickers.text = ('-'.join(self.datepickers.text.split('/')))
        self.set_la_lt_default()
        self.box_id.value = False
    pass


#------------------------DELETING_INTERFACE---------------------------------


class Deleting(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._do_setup)
        self.set()

    def _do_setup(self, *args):
        switch_id = ObjectProperty(None)
        slider = ObjectProperty(None)
        val = ObjectProperty(None)
        row = ListProperty([])  # list because data is type of kivy list object
        no_entries = {}
        recycleview = ObjectProperty(None)

    def on_enter(self):
        print('/n \n entered called')
        self.refresh()

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

    def refresh(self):
        global db
        # db.insert('M', '12.10.19', 5, 7, 'h')
        # print(db, db.show_all())
        self.recycleview.data = self.row
        database_values = db.show_all()
        try:  # handle any excpetion in rv
            if(database_values):
                for tuples in database_values:
                    print(tuples[0])
                    self.recycleview.data.append({'col1': {'text': str(tuples[0])}, 'col2': {'text': str(tuples[1])}, 'col3': {
                                                 'text': str(tuples[2])}, 'col4': {'text': str(tuples[3])}, 'col5': {'text': str(tuples[4])}})
                    # {[ {'label2': {'text': 'pineapple'}, 'label3': {'text': 'cat'} }, {'label2': {'text': 'apple'}, 'label3': {'text': 'rat'}}, {'label2': {'text': 'banana'}, 'label3': {'text': 'dog'}}, {'label2': {'text': 'pear'}, 'label3': {'text': 'bat'}}]}
                # print("Nope", self.recycleview.data)  # - -no need of zip here
            else:
                self.recycleview.data.append(self.no_entries)
        except:
            error = 'Internl error code:error indeleting/rv probs'
            print(error)

    # def get_selected(self):
    #     global max, max_view, default, daysoff, days_val, data, error, db

    def update(self):
        global db, error
        try:
            if(SelectableLabel.selected_values):
                if(SelectableLabel.selected_values[0] == 'no entry yet'):
                    self.delete_empty()
                else:
                    print(SelectableLabel.selected_values)
                    for i in SelectableLabel.selected_values:
                        db.delete(i['col2']['text'])
                    self.refresh()
            else:
                self.delete_empty()
        except:
            error = 'Internl error code:error in updating/database commands'
            print(error)

    def delete_empty(self):
        global error
        error = 'Nothing to Delete / Update here'
        print(error)

    def set(self):
        # self.data requires----------------- {'text': '9'}]--list pf dictonary
        set_database()  # database must exist before delete
        self.row = [{'col1': {'text': 'Day'}, 'col2': {'text': 'Date'}, 'col3': {
            'text': 'Lecture Attended'}, 'col4': {'text': 'Lecture took'}, 'col5': {'text': 'Holiday'}}]  # a base row
        self.no_entries = {'col1': {'text': ''}, 'col2': {'text': ''}, 'col3': {
            'text': 'no entry yet'}, 'col4': {'text': ''}, 'col5': {'text': ''}}
        print("called set of RV")
        print('rv,setted=', self.row)
        # print(db.show_all())  # -----------------testing
        self.slider.max = max_view
        self.refresh()


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


#-----!@$#%^&*()- Clock.schedule_once(self.checkdate)

#------------------------VIEW_DATA_INTERFACE---------------------------------


class View_data(Screen):
    def __init__(self, **kwargs):
        Clock.schedule_once(self._do_setup)

    def _do_setup(self, *args):
        cp = ObjectProperty(None)
        self.max_value = 50
        steps = self.max_value * 0.25
        e = Clock.schedule_interval(
            partial(self.animate, self.max_value, steps), 0.03)

    self.cp.value = 0

    def on_enter(self):
        self.cp.height = 0

    def animate(self, max, steps, dt):
        self.cp.height = app.root.height * 0.2
        print(self.cp.value)
        if(self.cp.value == 100 or self.cp.value >= max):
            self.cp.set_label(self.max_value)
        else:
            self.cp.set_value(self.cp.value + steps)

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


class Imagebutton(ButtonBehavior, Image):  # -------------oder yhi hpga call ka
    pass
# class--------------View_for_deletion---------


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
                                 RecycleBoxLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableLabel(RecycleDataViewBehavior, GridLayout):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)
    cols = 5
    selected_values = []
    col_1 = ObjectProperty(None)
    col_2 = ObjectProperty(None)
    col_3 = ObjectProperty(None)
    col_4 = ObjectProperty(None)
    col_5 = ObjectProperty(None)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        print("To be parsed::", data['col1']['text'])
        # name matching col1 wont work as name is matching with it's base class
        self.col_1.text = data['col1']['text']
        # dictionary from its rv and selectable class
        self.col_2.text = data['col2']['text']
        self.col_3.text = data['col3']['text']
        self.col_4.text = data['col4']['text']
        self.col_5.text = data['col5']['text']

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
            self.selected_values.append(rv.data[index])
        else:
            print("selection removed for {0}".format(rv.data[index]))
            try:
                self.selected_values.remove(rv.data[index])
            except:
                print('unable to delete in rv class')


class RV(RecycleView):  # ---------------------------popup?
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': 'no entry yet'}]

#---------up-----------------------------


class CircularProgressBar(ProgressBar):

    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)

        # Set constant for the bar thickness
        self.thickness = 40

        # Create a direct text representation
        self.label = CoreLabel(text="0%", font_size=self.thickness)

        # Initialise the texture_size variable
        self.texture_size = None

        # Refresh the text
        self.refresh_text()

        # Redraw on innit
        self.draw()

    def draw(self):

        with self.canvas:

            # Empty canvas instructions
            self.canvas.clear()

            # Draw no-progress circle
            Color(0.26, 0.26, 0.26)
            Ellipse(pos=self.pos, size=self.size)

            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
            Color(1, 0, 0)
            Ellipse(pos=self.pos, size=self.size,
                    angle_end=(0.001 if self.value_normalized == 0 else self.value_normalized * 360))

            # Draw the inner circle (colour should be equal to the background)
            Color(0, 0, 0)
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),
                    size=(self.size[0] - self.thickness, self.size[1] - self.thickness))
            print('s', self.pos[0], self.thickness,
                  self.pos[1], self.thickness)
            # Center and draw the progress text
            Color(1, 0, 0)  # s 0 40 0 40

 # 200 73 200 48
            print('\n', self.size[0], self.texture_size[0],
                  self.size[1], self.texture_size[1])
            Rectangle(texture=self.label.texture, size=self.texture_size,
                      pos=(self.size[0] / 2 - self.texture_size[0] / 2 + self.pos[0], self.size[1] / 2 - self.texture_size[1] / 2 + self.pos[1]))

    def refresh_text(self):
        # Render the label
        self.label.refresh()

        # Set the texture size each refresh
        self.texture_size = list(self.label.texture.size)

    def set_value(self, value):
        time.sleep(0.01)
        # Update the progress bar value
        self.value = value

        # Update textual value and refresh the texture
        self.label.text = str(int(self.value_normalized * 100)) + "%"
        self.refresh_text()

        # Draw all the elements
        self.draw()
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
