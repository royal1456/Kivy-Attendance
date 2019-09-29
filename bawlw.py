




















































































































































































                                 RecycleBoxLayout):
                                for i in self.datepickers.text.split('-'))
                                for i in self.datepickers.text.split('/'))
                      pos=(self.size[0] / 2 - self.texture_size[0] / 2 + self.pos[0], self.size[1] / 2 - self.texture_size[1] / 2 + self.pos[1]))
                    angle_end=(0.001 if self.value_normalized == 0 else self.value_normalized * 360))
                    size=(self.size[0] - self.thickness, self.size[1] - self.thickness))
                    st = st + str(i) + '              '
                    st = st + str(i) + '              '
                '              ')
                app.root.current = "delete"
                app.root.current = "main"
                app.root.current = "main"
                app.root.current = "main"
                app.root.current = "main"
                app.root.current = "set"
                app.root.current = "update"
                app.root.current = "View_data"
                b = Factory.MultiSelectOption(text=value)
                b.bind(state=self.select_value)
                default_size: None, dp(40)
                default_size_hint: 0.9, None
                for i in x:
                for i in x:
                height: self.minimum_height
                id:lay
                multiselect: True
                orientation: 'vertical'
                print('called if')
                print('No values to remove')
                return False
                root.manager.transition.direction = "left"
                root.manager.transition.direction = "left"
                root.manager.transition.direction = "left"
                root.manager.transition.direction = "left"
                root.manager.transition.direction = "right"
                root.manager.transition.direction = "right"
                root.manager.transition.direction = "right"
                root.manager.transition.direction = "right"
                root.manager.transition.duration = 0.5
                root.manager.transition.duration = 0.5
                root.manager.transition.duration = 0.5
                root.manager.transition.duration = 0.5
                self.cp.set_value(self.cp.value + steps)
                self.dropdown.add_widget(b)
                self.dropdown.clear_widgets()
                self.row.append({'text': st})
                self.row.append({'text': st})
                self.selected_values.append(instance.text)
                self.selected_values.remove(instance.text)
                self.selected_values.remove(rv.data[index])
                self.spinner_up_lt.text), self.holiday)
                size_hint_y: None
                st = ''
                st = ''
                touch_multiselect: True
              self.days.text, self.default_la.text)
            #     size_hint=(1, 0.5), id='val')
            # [{'text': y for y in list(x)} for x in v]
            # [{'text': y for y in list(x)} for x in v]
            # Center and draw the progress text
            # converting a tuple to list as(v returned a tuple which is alist ('Monday', '22-08-2019', 0, 0, 'h')  )
            # converting a tuple to list as(v returned a tuple which is alist ('Monday', '22-08-2019', 0, 0, 'h')  )
            # Draw no-progress circle
            # Draw progress circle, small hack if there is no progress (angle_end = 0 results in full progress)
            # Draw the inner circle (colour should be equal to the background)
            # Empty canvas instructions
            # return False
            # self.active passes self,instance,value-which true or flase
            # self.ids.val.add_widget(RV(id='y'))
            # self.remove_widget(self.x)
            # self.x = FloatLayout(
            # value or active
            '-'.join(self.datepickers.text.split('/')))  # -date>today( )
            '0')  # (total lectures equal)
            ("\n holiday" if(self.box_id.state == "active") else "\n working day.")
            Color(0, 0, 0)
            Color(0.26, 0.26, 0.26)
            Color(1, 0, 0)
            Color(1, 1, 1, 1)
            color:0,0,0,1
            color:0,0,0,1
            data = values[5][1]
            data:root.row
            day, month, year = (int(i)
            day, month, year = (int(i)
            days_val = values[2][1]
            daysoff = int(values[1][1])
            db.delete(values[1])  # --date
            db.insert(self.days, self.datepickers.text, int(self.spinner_up_la.text), int(
            default = int(values[3][1])
            Ellipse(pos=(self.pos[0] + self.thickness / 2, self.pos[1] + self.thickness / 2),
            Ellipse(pos=self.pos, size=self.size)
            Ellipse(pos=self.pos, size=self.size,
            else:
            error = 'unable to delete value'
            error = 'Unable to display attendance'
            except:
            font_size:0
            font_size:14
            font_size:14
            font_size:14
            font_size:14
            font_size:23
            font_size:23
            font_size:30
            font_size:30
            font_size:30
            font_size:30
            font_size:30
            font_size:30
            font_size:30
            font_size:30
            font_size:30
            font_size:30
            font_size:30
            font_size:30
            font_size:30
            for value in values:
            for x in v:
            for x in v:
            height: root.height*0.2
            id: box_id
            id: slider
            id: took_off
            id:calendar
            id:cp
            id:database_name
            id:datepickers
            id:days
            id:default_la
            id:label
            id:label
            id:max_l
            id:notification
            id:spinner_up
            id:spinner_up_la
            id:spinner_up_lt
            id:switch_id
            if instance.text in self.selected_values:
            if instance.text not in self.selected_values:
            if self.dropdown.children:
            if(self.cp.value == 100 or self.cp.value >= max):
            max = int(values[0][1])
            max: 100
            max: 2
            max_view = int(values[4][1])
            min: 1
            on_active: root.box_on(self,self.active)
            on_active: root.on_active(self,self.active)
            on_active: root.took_off_day(self,self.active)
            on_press:root.get_selected()
            on_press:root.popup()
            on_press:root.popup()
            on_press:root.update()
            on_release:
            on_release:
            on_release:
            on_release:
            on_release:
            on_release:
            on_release:
            on_release:
            on_release: root.dismiss()
            on_release: root.dismiss()
            on_release:root.my_widget.submit()
            on_text:root.checkdate(self)
            padding : 10, 10
            padding:(10,10)
            padding:(20,5)
            pHint:(0.8,0.8)
            pos: self.pos
            pos_hint:{"x":0.05}
            pos_hint:{"x":0.8,"y":0.85+0.92}
            pos_hint:{"x":0.8,"y":0.85}
            pos_hint:{"x":0.8,"y":0.85}
            pos_hint:{"x":0.8,"y":0.85}
            pos_hint:{'x':0.015,'y':0.5}
            pos_hint:{'x':0.015,'y':0.6}
            pos_hint:{'x':0.05,'y':0.05}
            pos_hint:{'x':0.05,'y':0.45}
            pos_hint:{'x':0.1,'y':0.1}
            pos_hint:{'x':0.1,'y':0.38}
            pos_hint:{'x':0.1,'y':0.3}
            pos_hint:{'x':0.1,'y':0.3}
            pos_hint:{'x':0.1,'y':0.4+0.67}
            pos_hint:{'x':0.1,'y':0.4}
            pos_hint:{'x':0.1,'y':0.4}
            pos_hint:{'x':0.1,'y':0.55+0.77}
            pos_hint:{'x':0.1,'y':0.5}
            pos_hint:{'x':0.1,'y':0.5}
            pos_hint:{'x':0.1,'y':0.6}
            pos_hint:{'x':0.1,'y':0.6}
            pos_hint:{'x':0.1,'y':0.7+0.87}
            pos_hint:{'x':0.1,'y':0.7}
            pos_hint:{'x':0.1,'y':0.7}
            pos_hint:{'x':0.2,'y':0.16}
            pos_hint:{'x':0.3,'y':0.9+0.92}
            pos_hint:{'x':0.3,'y':0.9}
            pos_hint:{'x':0.3,'y':0.9}
            pos_hint:{'x':0.3,'y':0.9}
            pos_hint:{'x':0.3,'y':0.9}
            pos_hint:{'x':0.4,'y':0.15}
            pos_hint:{'x':0.4,'y':0.16}
            pos_hint:{'x':0.4,'y':0.2}
            pos_hint:{'x':0.4,'y':0.3+0.67}
            pos_hint:{'x':0.4,'y':0.65}
            pos_hint:{'x':0.5,'y':0.3}
            pos_hint:{'x':0.5,'y':0.4}
            pos_hint:{'x':0.5,'y':0.5+0.97}
            pos_hint:{'x':0.5,'y':0.5}
            pos_hint:{'x':0.5,'y':0.6}
            pos_hint:{'x':0.5,'y':0.7}
            pos_hint:{'x':0.55,'y':0.05}
            pos_hint:{'x':0.55,'y':0.45}
            pos_hint:{'x':0.6,'y':0.16}
            pos_hint:{'x':0.6,'y':0.3}
            pos_hint:{'x':0.6,'y':0.45+0.67}
            pos_hint:{'x':0.6,'y':0.4}
            pos_hint:{'x':0.6,'y':0.5}
            pos_hint:{'x':0.6,'y':0.6}
            pos_hint:{'x':0.6,'y':0.7}
            pos_hint:{'x':0.7,'y':0.45+0.67}
            print("called set of RV")
            print("called try of set")
            print("called try of set")
            print("selection changed to {0}".format(rv.data[index]))
            print("selection removed for {0}".format(rv.data[index]))
            print('called checkdate else')
            print('callllled checkdate if')
            print('rv,setted=', self.row)
            print('rv,setted=', self.row)
            print(error)
            Rectangle(texture=self.label.texture, size=self.texture_size,
            return self.parent.select_with_touch(self.index, touch)
            return True
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
            rv, index, data)
            SelectableRecycleBoxLayout:
            self.animate, self.max_value, steps), 0.03)
            self.box_id.active = False
            self.box_id.active = False
            self.box_id.active = True
            self.canvas.clear()
            self.dropdown = DropDown()
            self.dropdown.dismiss()
            self.dropdown.open(self)
            self.holiday = 'h'
            self.holiday = 'w'
            self.holiday = 'w'
            self.i.label.text = '\nINVALID ENTRY TO DATABASE\n\n ->Check Respective Constrain\n ->Chek for duplicate entries'
            self.i.open()
            self.notification.font_size = 0
            self.notification.font_size = 12
            self.row = [{'text': 'no entry yet'}]
            self.row = [{'text': 'no entry yet'}]
            self.selected_values.append(rv.data[index])
            self.set_holiday()
            self.set_holiday()
            self.set_la_lt()
            self.set_la_lt()
            self.set_la_lt()
            self.spinner_up_la.text = '0'
            self.spinner_up_la.values = ('0')
            self.text = ''
            self.text = ', '.join(value)
            self.took_off.active = False
            self.update()
            self.update()
            self.val.size_hint = 1, 0
            self.val.size_hint = 1, 0.5
            size: self.size
            size_hint: (None, None)
            size_hint: .12,.07
            size_hint: .35,.07
            size_hint:0.06,0.06
            size_hint:0.06,0.06
            size_hint:0.06,0.06
            size_hint:0.06,0.06
            size_hint:0.1,0.07
            size_hint:0.1,0.07
            size_hint:0.12,0.07
            size_hint:0.12,0.07
            size_hint:0.12,0.07
            size_hint:0.12,0.07
            size_hint:0.2,0.1
            size_hint:0.2,0.1
            size_hint:0.2,0.2
            size_hint:0.2,0.2
            size_hint:0.2,0.2
            size_hint:0.35,0.07
            size_hint:0.8,0.1
            size_hint:0.8,0.5
            size_hint:None,None
            source:'icons/checkmark-outline.png'
            source:'icons/refresh-outline.png'
            step: 1
            text: "delete"
            text: "Home"
            text: "Home"
            text: "Home"
            text: "Home"
            text: "Settings"
            text: "update"
            text: "View"
            text: 'Close'
            text: 'OK'
            text: 'Save'
            text: str(slider.value)
            text:"(unchecking this box will make the holiday counted as working day)"
            text:"deleting"
            text:"Enter Date:"
            text:"Enter Default Lectures:"
            text:"Enter Holidays:"
            text:"Enter Max Lectures:"
            text:"Enter Max records to display:"
            text:"Enter person name:"
            text:"Holiday"
            text:"Lectures Attended:"
            text:"Lectures Took:"
            text:"Record of days:"
            text:"Settings"
            text:"show data box:"
            text:"submit"
            text:"submit"
            text:"Took off:"
            text:'0'
            text:'0'
            text:'5'
            text:'5'
            text:'5'
            text:'7'
            text:'Attendance Monitiring'
            text:'Saturday,Sunday'
            text:'Updating Data'
            text:'Viewing Records'
            text_size : self.width, None
            text_size : self.width, None
            try:
            values = [x.split(':') for x in f.read().split('\n')]
            values = SelectableLabel.selected_values[0]['text'].split(
            values:'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'
            viewclass: 'SelectableLabel'
            width:  root.height*0.2
            {'text': 'Day                     Date               Attended    Total      Working day'}]
            {'text': 'Day                     Date               Attended    Total      Working day'}]
        #       ['text'].split('              '))
        #     minimum_height=self.calendar.setter('height'))
        #     partial(datepicker.DayAbbrWeekendLabel.Change,  (1, 1, 0, 1), self.datepickers), -1)
        #     return self._calendar.state_change
        #    # CalendarWidget:
        #   #     id:calendar
        # (total lectures equal)
        # ---------used for smooth runing in linux as init creates problem in intializing
        # @property
        # @self.calendar.state_change.setter
        # Animate the progress bar
        # Clock.schedule_once(
        # Create a direct text representation
        # def state_change(self):
        # def state_change(self, value):
        # Draw all the elements
        # Initialise the texture_size variable
        # no of days,sunday,saturdayetc
        # print(RV.selectable)
        # print(RV.selected)
        # print(SelectableLabel.selected_values[0]
        # print(value, 'LOL--Changed', self.calendar.state_change)
        # Refresh the text
        # Render the label
        # s()
        # selectetd dictoinary using key text,dict_ was inside a list -['Monday', '24-08-2019', '5', '7', 'w', ''] op
        # self.calendar.bind(
        # self.data requires----------------- {'text': '9'}]--list pf dictonary
        # self.datepickers.cal.init_ui([17, 18, 19])#--tKWN OFF
        # self.on_enter()--makes bar at right rendering
        # self.on_enter()--same as above
        # self.spinner_up.self.selected_values = ['Saturday', 'Sunday']
        # self.t is aninstance of mypop and here self passed act as my_widget
        # self.t.label refers to label decalred in my_wifget in popup
        # Set constant for the bar thickness
        # Set the texture size each refresh
        # time.sleep(0.1)
        # Update textual value and refresh the texture
        # Update the progress bar value
        # updating label only and animating later
        # while(self.root.cp.value != 50):
        ''' Add selection on touch down '''
        ''' Catch and handle the view changes '''
        ''' if off is taken on working day '''
        ''' Respond to the selection of items in the view. '''
        '''in case  occassionaly off'''
        '''In case of occasionally off'''
        a = 1
        app = App.get_running_app()
        box_id = ObjectProperty(None)
        calendar = ObjectProperty(None)
        CalendarWidget:
        CheckBox:      ##for holiday cheking-------------------------------ui-command
        CheckBox:      ##for holiday taken-------------------------------ui-command
        CircularProgressBar:
        Clock.schedule_once(self._do_setup)
        Clock.schedule_once(self._do_setup)
        Clock.schedule_once(self._do_setup)
        Clock.schedule_once(self.checkdate)
        Color:
        cp = ObjectProperty(None)
        Custombutton:
        Custombutton:
        Custombutton:
        Custombutton:
        Custombutton:
        Custombutton:
        Custombutton:
        Custombutton:
        Custombutton:
        Custombutton:
        Custombutton:
        Custominput:
        Custominput:
        Custominput:
        Custominput:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        Customlabel:
        data = str(self.database_name.text)
        database_name = ObjectProperty(None)
        DatePicker:   ##for calender handling------------------------kivy-ui-commands
        datepickers = ObjectProperty(None)
        days = ObjectProperty(None)
        days_val = self.spinner_up.text
        daysoff = len(days_val.split(','))
        db.create()
        default = int(self.default_la.text)
        default_la = ObjectProperty(None)
        e = Clock.schedule_interval(partial(
        else:
        else:
        else:
        else:
        else:
        else:
        else:
        else:
        else:
        else:
        else:
        error = 'unable to read database'
        except:
        except:
        except:
        f.write('Data:' + str(data))
        f.write('days_val:' + str(days_val) + '\n')
        f.write('daysoff:' + str(daysoff) + '\n')
        f.write('lec_default:' + str(default) + '\n')
        f.write('lec_in_day:' + str(max) + '\n')
        f.write('max_days:' + str(max_view) + '\n')  # max views
        get_data()
        get_data()
        get_data()  # global adding
        global db
        global max, max_view, default, daysoff, days_val, data
        global max, max_view, default, daysoff, days_val, data, error, db
        global max, max_view, default, daysoff, days_val, data, error, db
        global max, max_view, default, daysoff, days_val, data, error, db
        global max, max_view, default, daysoff, days_val, data, error, db
        global max, max_view, default, daysoff, days_val, data, error, db
        id:val
        if (value is True):
        if is_selected:
        if not self.dropdown:
        if self.collide_point(*touch.pos) and self.selectable:
        if self.dropdown.parent:
        if super().on_touch_down(touch):
        if value == 'down':
        if value:
        if values:
        if(len(self.datepickers.text.split('/')) > 1):
        if(SelectableLabel.selected_values):
        if(self.days in days_val.split(',')):
        if(v):
        if(v):
        if(value is True):
        if(value is True):
        Imagebutton:
        Imagebutton:
        label = ObjectProperty(None)
        label = ObjectProperty(None)
        max = self.max_l.text
        max_l = ObjectProperty(None)
        max_view = int(self.days.text)  # max_view
        MultiSelectSpinner:       ##for changing holidays took-------------------------db-commands
        notification = ObjectProperty(None)
        padding : 10, 10
        padding : 10, 10
        padding : 10, 10
        padding:10,10
        print("caleed ", value)
        print("called submit", self.datepickers.text)
        print("Changes saved", self.max_l.text,
        print("v,returned", v)
        print("v,returned", v)
        print('called box id', value)
        print('calledd,selected', SelectableLabel.selected_values)
        print('do called')
        print('enter called')
        print('init called')
        print('set called')
        print('set_holiday called ')
        print(db.show_all())  # -----------------testing
        print(error)
        print(max, max_view, default, daysoff, days_val, data, error, db)
        print(root)
        print(self.calendar.state_change)
        print(self.cp.value)
        print(self.o)
        print(self.row)
        print(value, 'LOL--Changed', self.calendar.state_change)
        Rectangle:
        return screen_manager
        return super().refresh_view_attrs(
        root = App.get_running_app().root
        RV:
        self.bind(dropdown=self.update_dropdown)
        self.bind(on_release=self.toggle_dropdown)
        self.bind(values=self.update_dropdown)
        self.box_id.active = False
        self.calendar.bind(state_change=self.on_btn_press)
        self.calendar.init_ui([17, 18, 19])  # --tKWN OFF
        self.cp.height = 0
        self.cp.height = app.root.height * 0.2
        self.cp.set_label(self.max_value)
        self.cp.value = 0
        self.database_name.text = str(data)
        self.datepickers.cal.left_arrow.color = (1, 1, 0, 1)
        self.datepickers.text = (
        self.days = 'Monday'
        self.days = datetime.date(year, month, day).strftime("%A")
        self.days.text = str(max_view)  # max_view
        self.default_la.text = str(default)
        self.draw()
        self.holiday = 'h'
        self.holiday = 'w'
        self.holiday = 'w'
        self.i = Infopopup(self)
        self.index = index
        self.label = CoreLabel(text="0%", font_size=self.thickness)
        self.label.refresh()
        self.label.text = str(int(self.value_normalized * 100)) + "%"
        self.max_l.text = str(max)
        self.max_value = 50
        self.my_widget = my_widget  # mywidget instance is used to accees child values
        self.my_widget = my_widget  # mywidget instance is used to accees child values
        self.o.append(1)
        self.refresh_text()
        self.refresh_text()
        self.row = [
        self.row = [
        self.row = []
        self.row = []
        self.selected = is_selected
        self.set()
        self.set()
        self.set()
        self.set_help()  # global helping
        self.set_la_lt()
        self.sets()
        self.slider.max = max_view
        self.spinner_up.text = str(days_val)
        self.spinner_up_la.text = self.spinner_up_lt.text = '0'
        self.spinner_up_la.text = str(default)
        self.spinner_up_la.values = tuple([str(x) for x in range(max + 1)])
        self.spinner_up_lt.text = str(max)
        self.spinner_up_lt.values = self.spinner_up_la.values
        self.spinner_up_lt.values = self.spinner_up_la.values = (
        self.t = MyPopup(self)
        self.t = MyPopup(self)
        self.t.dismiss()
        self.t.dismiss()
        self.t.label.text = text
        self.t.label.text = text
        self.t.open()
        self.t.open()
        self.texture_size = list(self.label.texture.size)
        self.texture_size = None
        self.thickness = 20
        self.took_off = []
        self.took_off.active = False
        self.update()
        self.value = 0
        self.value = value
        self.value = value
        set_data()
        set_data()  # global_saving
        set_database()
        size_hint:1,0.5
        size_hint:1,0.5
        slider = ObjectProperty(None)
        Slider:
        Spinner:       ##for changing lectures attended-------------------------db-commands
        Spinner:       ##for changing lectures took-------------------------db-commands
        spinner_up = ObjectProperty(None)
        spinner_up_la = ObjectProperty(None)
        spinner_up_lt = ObjectProperty(None)
        steps = self.max_value * 0.25
        Submitbutton:
        Submitbutton:
        super().__init__(**kwargs)
        super().__init__(**kwargs)
        super().__init__(**kwargs)
        super().__init__(**kwargs)
        super().__init__(**kwargs)
        super().__init__(**kwargs)
        super().__init__(**kwargs)
        super(CircularProgressBar, self).__init__(**kwargs)
        super(MultiSelectSpinner, self).__init__(**kwargs)
        super(RV, self).__init__(**kwargs)
        Switch:
        switch_id = ObjectProperty(None)
        text = "Confirm entery of " + self.datepickers.text + " as a " + \
        text = "Save Changes?"
        took_off = ObjectProperty(None)
        try:
        try:
        try:
        v = db.show_all()
        v = db.show_all()
        val = ObjectProperty(None)
        values = self.values
        view = ObjectProperty(None)
        Window.clearcolor = (1, 1, 1, 1)
        with open('settings.txt', 'r') as f:
        with self.canvas:
     #-----------la-lt-being-setted-----------------------
     size: self.texture_size
    """(internal) DropDown used with MultiSelectSpinner."""
    """List of values selected by the user."""
    """Values to choose from."""
    """Widget allowing to select multiple text options."""
    #     #plot.points = [(1, 0), (2, 0), (3, 0), (4, 0)]
    #     MeshLinePlot
    #     plot = MeshLinePlot(color=[1, 0, 0, 1])
    #     plot.points = [(x, x * x) for x in range(0, 101)]
    #     print("update_graph called")
    #     self.graph_data.add_plot(plot)
    #     self.graph_data.xlabel = 'lol'
    # def update_graph(self):
    # Draw a background to indicate selection
    # graph_data = ObjectProperty(None)
    # id:graph_data
    # my_widget is now the object where popup was called from.
    # my_widget is now the object where popup was called from.
    # padding:5
    # plot:
    # pos_himt:{'x':0.2,'y':0.1}
    # size: root.width * 2 / 3 , root.height * 18 / 24]
    # size_hint:0.5,0.5
    # x: self.parent.x
    # x_grid_label:True
    # xmax:100
    # xmin:0
    # y: self.parent.y
    # y_grid_label:True
    # ymax:10000
    # ymin:0
    ''' Add selection support to the Label '''
    ''' Adds selection and focus behaviour to the view. '''
    allow_stretch: True
    auto_dismiss: False
    auto_dismiss: False
    box_id:box_id
    calendar:calendar
    canvas.before:
    color:0,0,0,1
    cp:cp
    database_name:database_name
    datepickers:datepickers
    days:days
    db = database(max, data)
    db.create()
    def __init__(self,  **kwargs):
    def __init__(self, **kwargs):
    def __init__(self, **kwargs):
    def __init__(self, **kwargs):
    def __init__(self, **kwargs):
    def __init__(self, **kwargs):
    def __init__(self, **kwargs):
    def __init__(self, **kwargs):
    def __init__(self, my_widget, **kwargs):
    def __init__(self, my_widget, **kwargs):
    def _do_setup(self, *args):
    def _do_setup(self, *l):
    def _do_setup(self, *l):
    def animate(self, max, steps, dt):
    def apply_selection(self, rv, index, is_selected):
    def box_on(self, instance, value):
    def build(self):
    def checkdate(self, *args, **kwargs):
    def draw(self):
    def get_selected(self):
    def on_active(self, instance, value):
    def on_btn_press(self):
    def on_enter(self):
    def on_selected_values(self, instance, value):
    def on_start(self):
    def on_touch_down(self, touch):
    def popup(self):
    def popup(self):
    def refresh_text(self):
    def refresh_view_attrs(self, rv, index, data):
    def select_value(self, instance, value):
    def set(self):
    def set(self):
    def set_help(self):
    def set_holiday(self):  # setting values for all spinners in case of holiday
    def set_la_lt(self):
    def set_label(self, value):
    def set_value(self, value):
    def sets(self):
    def submit(self):
    def submit(self):
    def toggle_dropdown(self, *args):
    def took_off_day(self, instance, value):
    def update(self):
    def update(self):
    def update_dropdown(self, *args):
    def v(self):
    default_la:default_la
    dropdown = ObjectProperty(None)
    except:
    FloatLayout:
    FloatLayout:
    FloatLayout:
    FloatLayout:
    FloatLayout:
    FloatLayout:
    FloatLayout:
    FloatLayout:
    focus:True
    focus:True
    font_size: 24
    font_size: 24
    font_size:30
    font_size:44
    global max, max_view, default, daysoff, days_val, data, error, db
    global max, max_view, default, daysoff, days_val, data, error, db
    global max, max_view, default, daysoff, days_val, data, error, db
    height: '48dp'
    index = None
    label:label
    label:label
    lay:lay
    max_l:max_l
    multiline:False
    multiline:True
    name:"delete"
    name:"main"
    name:"set"
    name:"update"
    name:"view_data"
    notification:notification
    o = [0, 8, 9]
    padding:(40,5)
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    row = ListProperty([])
    row = ListProperty([])
    selectable = BooleanProperty(True)
    selected = BooleanProperty(False)
    selected_values = []
    selected_values = ListProperty([])
    size: 25, 25
    size: self.texture_size
    size_hint: .12,.07
    size_hint: 1, None
    size_hint: None,None
    size_hint: None,None
    size_hint: None,None
    size_hint: None,None
    size_hint:0.5,0.5
    size_hint:0.5,0.5
    size_hint_y: None  ##imp
    slider:slider
    spinner_up:spinner_up
    spinner_up_la:spinner_up_la
    spinner_up_lt:spinner_up_lt
    switch_id:switch_id
    text_size: root.width, None
    text_size: root.width, None
    title:"Confirm"
    title:"Invalid Entry"
    took_off:took_off
    try:
    val:val
    values = ListProperty([])
    with open('settings.txt', 'w+') as f:
""")
# # done by object propperrty
# ------------------Delete_data---------------------------
# ------------------Essentials---------------------------
# ------------------Main_interface---------------------------
# ------------------Set_data---------------------------
# ------------------Update_data---------------------------
# ------------------View_data---------------------------
# -------------savebutton---------
# -----------refernce https://kivy.org/doc/stable/api-kivy.properties.html?highlight=numericproperty-----------
# -----------reresh-button----------
# Add the screens to the manager and then supply a name
# app:always refers to the instance of your application
# base Class of your App inherits from the App class.
# below this kivy version you cannot
# Builder is used when .kv file is
# changing a class variable--data
# class--------------View_for_deletion---------
# Create a class for all screens in which you can include
# Create the App class
# dedicated to managing multiple screens for your application.
# from kivy.garden.graph import Graph, MeshLinePlot
# helpful methods specific to that screen
# import kivy module
# NO DOcumentation yet found :([ Graph:
# Program to Show how to create a switch
# run the app
# that is used to switch screens
# The screen manager is a widget
# this restrict the kivy version i.e
# to be used in .py file
# use the app or software
# Window.size = (550, 700)
#-------------------------------UPDATING----------------------------------
#------------------------DELETING_INTERFACE---------------------------------
#------------------------ESSENTIAL_REQUIREMENT---------------------------------
#------------------------MAIN_CALLING---------------------------------
#------------------------SCREEN_MANAGER---------------------------------
#------------------------SETTING_INTERFACE---------------------------------
#------------------------VIEW_DATA_INTERFACE---------------------------------
#-------------to be changed at interaction-------------
#-----------Calling-Ids--------------Class-Variables-----------
#-----------Calling-Ids--------------Class-Variables-----------
#-----------Holidays-setting-------------------------
#-----------Ideal-Settings--------------------------
#---------up-----------------------------
#:import Factory kivy.factory.Factory
#:import MeshLinePlot kivy.garden.graph.MeshLinePlot
'''
'''
'''
'''
-------------bug----------
::op[0, 8, 9]
<Custombutton@Button>:
<Custominput@TextInput>:
<Customlabel@Label>:
<Deleting>:
<Imagebutton>:
<Infopopup>:
<MainWindow>:
<MultiSelectOption@ToggleButton>:
<MyPopup>:
<SelectableLabel>:
<Set>:
<Submitbutton@Button>:
<Updating>:
<View_data>:
[0, 8, 9, 1] [0, 8, 9, 1]
accessing method or sub will not affect class variable but intializing will like self.o=...
Builder.load_string("""
centering te text in databse label
class CircularProgressBar(ProgressBar):
class Deleting(Screen):
class Imagebutton(ButtonBehavior, Image):  # -------------oder yhi hpga call ka
class Infopopup(Popup):
class MainWindow(Screen):
class MultiSelectSpinner(Button):
class MyPopup(Popup):
class RV(RecycleView):  # ---------------------------popup?
class ScreenApp(App):
class SelectableLabel(RecycleDataViewBehavior, Label):
class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior,
class Set(Screen):
class Updating(Screen):
class View_data(Screen):
class x:
data = 'none'  # string vala none xD
date sapcing in update-
date_picker bug-previous months date
days_val = 'Saturday,Sunday'
daysoff = 2
db = None
def get_data():
def set_data():
def set_database():
default = 5
error = 'none'
float layots's size hint is only accesed not pos hint
from att_interactdb import database
from functools import partial  # --animation progress bar circular
from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import Label as CoreLabel
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.behaviors import FocusBehavior, ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
get_data()
https://stackoverflow.com/questions/49935190/kivy-how-to-initialize-the-viewclass-of-the-recycleview-dynamically
imp for correct placements:
import datepicker
import datetime
import kivy
import time
init has no self for object property but need 1 when accesing
init problems for class--Solved
kivy.require('1.9.0')
max = 7
max_view = 5  # days
never forget that super.init()
pHint = size of calendar
popup is edited and called externally
reading from file blocks highlight in set()
rv-popup?--dropped 4 now---------newrvppoup
sample_app = ScreenApp()
sample_app.run()
screen_manager = ScreenManager()
screen_manager.add_widget(Deleting(name="delete"))
screen_manager.add_widget(MainWindow(name="main"))
screen_manager.add_widget(Set(name="set"))
screen_manager.add_widget(Updating(name="update"))
screen_manager.add_widget(View_data(name="View_data"))
size_hint = size of text label
starting date as a holiday is not counted
