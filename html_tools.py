#Potential Bokeh widgets to include for plot interactions. 
#Code based off of examples from this link: https://docs.bokeh.org/en/latest/docs/user_guide/interaction/widgets.html 

#Attempting to add multiple widgets to the same website using tutorial at this link: 
#https://www.geeksforgeeks.org/how-to-line-up-different-widgets-horizontally-in-bokeh/#:~:text=There%20are%20different%20widgets%20in%20Bokeh%20such%20as%3A,CheckboxButtonGroup%203%20Dropdown%204%20TextInput%20and%20Many%20more.

#DatePicker - Potentially used to let user pick which date they want to view data from
from bokeh.io import *
from bokeh.models import CustomJS, DatePicker
from bokeh.layouts import gridplot
import json
import os
from datetime import date

available_dates = []

for root, dirs, files in os.walk(f"{os.getcwd()}/project_data_json"):
    for file in files:
        available_dates.append(file.replace('covidinfo', '').replace('.json', ''))

my_website =  output_file('covid_dashboard.html')

date_picker = DatePicker(title='Select date', value=f"{date.today()}", min_date=f"{available_dates[0]}", max_date=f"{available_dates[-1]}")
date_picker.js_on_change("value", CustomJS(code="""
    console.log('date_picker: value=' + this.value, this.toString())
"""))

#show(date_picker)


#DateRangeSlider - Potentially used to let user pick a range of dates they want to view data from
from datetime import date

#from bokeh.io import show
from bokeh.models import DateRangeSlider

date_range_slider = DateRangeSlider(value=(date(2016, 1, 1), date(2016, 12, 31)),
                                    start=date(2015, 1, 1), end=date(2017, 12, 31))
date_range_slider.js_on_change("value", CustomJS(code="""
    console.log('date_range_slider: value=' + this.value, this.toString())
"""))

#show(date_range_slider)

#Dropdown - Potentially for letting users pick different plot types or different countries to display
#from bokeh.io import show
from bokeh.models import Dropdown

menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]

dropdown = Dropdown(label="Dropdown button", button_type="warning", menu=menu)
dropdown.js_on_event("menu_item_click", CustomJS(code="console.log('dropdown: ' + this.item, this.toString())"))

#show(dropdown)

#MultiSelect - Potentially for letting users pick different countries or plots to look at
#from bokeh.io import show
from bokeh.models import MultiSelect

OPTIONS = [("1", "foo"), ("2", "bar"), ("3", "baz"), ("4", "quux")]

multi_select = MultiSelect(value=["1", "2"], options=OPTIONS)
multi_select.js_on_change("value", CustomJS(code="""
    console.log('multi_select: value=' + this.value, this.toString())
"""))

#show(multi_select)

#Select - Potentially for letting users pick a specific plot or country 
from bokeh.io import show
from bokeh.models import Select

select = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])
select.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))

#show(select)

#Switch - Potentially used to hide or show a particular plot
#from bokeh.io import show
from bokeh.models import Switch

switch = Switch(active=True)
switch.js_on_change("active", CustomJS(code="""
    console.log('switch: active=' + this.active, this.toString())
"""))
#show(switch)

#TextInput - Potentially used to get a specific country's data the user wants to look at 
#from bokeh.io import show
from bokeh.models import TextInput

text_input = TextInput(value="default", title="Label:")
text_input.js_on_change("value", CustomJS(code="""
    console.log('text_input: value=' + this.value, this.toString())
"""))

#show(text_input)

#Toggle - Potentially used to allow a certain number of plots to be displayed or not
#from bokeh.io import show
from bokeh.models import Toggle

toggle = Toggle(label="Foo", button_type="success")
toggle.js_on_event('button_click', CustomJS(args=dict(btn=toggle), code="""
    console.log('toggle: active=' + btn.active, this.toString())
"""))


#example of programing a button push to print
from bokeh.io import show
from bokeh.models import Button, CustomJS
button = Button(label="Click Me", button_type="success")
button.js_on_click(CustomJS(code="alert('ok')"))
# display plot
#show(button)

#example of connecting slider to a plot
# Import Library
import numpy as np
from bokeh.plotting import figure, show
from bokeh.layouts import layout
from bokeh.models import RangeSlider
# Using Sin graph
n = 200
X = np.linspace(0, 4*np.pi, n)
Y = np.sin(X) 
plot = figure(x_range=(1,5))
points = plot.x(x=X, y=Y, size=40)
# Creating the Slider 
range_slider = RangeSlider(title=" Adjust X-Axis range",start=0,end=13,step=1,value=(plot.x_range.start, plot.x_range.end))
range_slider.js_link("value", plot.x_range, "start", attr_selector=0)
range_slider.js_link("value", plot.x_range, "end", attr_selector=1)
# displaying the output
layout = layout([range_slider], [plot])
#show(layout)

#widgets = gridplot([[date_picker, date_range_slider, dropdown, multi_select, select, switch, text_input, toggle]])
#show(widgets)