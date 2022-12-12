# from bokeh.layouts import column
# from bokeh.models import CustomJS, ColumnDataSource
# from bokeh.plotting import Figure, output_file, show
# from bokeh.models.widgets import Slider

# x = [x*0.05 for x in range(0, 200)]
# y = x

# source = ColumnDataSource(data=dict(x=x, y=y))
# plot = Figure(plot_width=400, plot_height=400)
# plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

# handler = CustomJS(args=dict(source=source), code="""
#    var data = source.data;
#    var f = cb_obj.value
#    var x = data['x']
#    var y = data['y']
#    for (var i = 0; i < x.length; i++) {
#       y[i] = Math.pow(x[i], f)
#    }
#    source.change.emit();
# """)

# slider = Slider(start=0.0, end=5, value=1, step=.25, title="Slider Value")

# slider.js_on_change('value', handler)
# layout = column(slider, plot)
# show(layout)

from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource
from bokeh.plotting import Figure, output_file, show
from bokeh.models.widgets import RadioGroup, Select

x = [x*0.05 for x in range(0, 200)]
y = x

source = ColumnDataSource(data=dict(x=x, y=y))

plot = Figure(plot_width=400, plot_height=400)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

radiohandler = CustomJS(args=dict(source=source), code="""
   var data = source.data;
   console.log('Tap event occurred at x-position: ' + cb_obj.active);
   //plot.title.text=cb_obj.value;
   x = data['x']
   y = data['y']
   if (cb_obj.active==0){
      for (i = 0; i < x.length; i++) {
         y[i] = x[i];
      }
   }
   if (cb_obj.active==1){
      for (i = 0; i < x.length; i++) {
         y[i] = Math.pow(x[i], 2)
      }
   }
   if (cb_obj.active==2){
      for (i = 0; i < x.length; i++) {
         y[i] = Math.pow(x[i], 4)
      }
   }
   source.change.emit();
""")

selecthandler = CustomJS(args=dict(source=source), code="""
   var data = source.data;
   console.log('Tap event occurred at x-position: ' + cb_obj.value);
   //plot.title.text=cb_obj.value;
   x = data['x']
   y = data['y']
   if (cb_obj.value=="line"){
      for (i = 0; i < x.length; i++) {
         y[i] = x[i];
      }
   }
   if (cb_obj.value=="SquareCurve"){
      for (i = 0; i < x.length; i++) {
         y[i] = Math.pow(x[i], 2)
      }
   }
   if (cb_obj.value=="CubeCurve"){
      for (i = 0; i < x.length; i++) {
         y[i] = Math.pow(x[i], 4)
      }
   }
   source.change.emit();
""")

radio = RadioGroup(
   labels=["line", "SqureCurve", "CubeCurve"], active=0)
radio.js_on_change('active', radiohandler)
select = Select(title="Select:", value='line', options=["line", "SquareCurve", "CubeCurve"])
select.js_on_change('value', selecthandler)

layout = column(radio, select, plot)
show(layout)