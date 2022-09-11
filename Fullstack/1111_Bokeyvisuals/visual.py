import pandas as pd
from bokeh.plotting import figure, show , output_file
from bokeh.models import HoverTool , ColumnDataSource


df = pd.read_csv('Sample_of_the_produced_time_values.csv')
print(df)

print('--------------------')
cds = ColumnDataSource(df)
print(cds)

p = figure(x_axis_type = 'datetime' , height = 100 , width = 500 , sizing_mode = 'scale_width', title = "Motion Graph")
# p.yaxis.minor_tick_line_color = None
# p.ygrid[0].ticker.desired_num_ticks = 1

# q = p.quad(left = df["Start"], right = df["End"], bottom = 0 , top = 1 , color ="green" )


q = p.quad(left = "Start", right = "End", bottom = 0 , top = 1 , color ="green" , source = cds)

output_file("graph1.html")
show(p)
