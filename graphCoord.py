from bokeh.models.tools import BoxZoomTool, ResetTool, PanTool, WheelZoomTool
from bokeh.plotting import figure, save, output_file
from bokeh.models import Label

import sqlite3

p = figure(
    width=825, 
    height=820, 
    toolbar_location="below",
    tools = [BoxZoomTool(), ResetTool(), PanTool(), WheelZoomTool()]
)

p.xaxis.axis_label = "X Coords"
p.yaxis.axis_label = "Y Coords"

p.xaxis.axis_label_text_color = "white"
p.yaxis.axis_label_text_color = "white"

p.background_fill_color = "gray"
p.border_fill_color = "black"
p.outline_line_color = "white"

p.axis.major_tick_out = 18

p.xaxis.axis_line_width = 12
p.xaxis.axis_line_color = "green"

p.yaxis.axis_line_width = 12
p.yaxis.axis_line_color = "green"

p.xaxis.major_label_text_color = "orange"
p.yaxis.major_label_text_color = "orange"

p.xaxis.major_tick_line_color = "firebrick"
p.xaxis.major_tick_line_width = 3
p.xaxis.minor_tick_line_color = "orange"

p.yaxis.major_tick_line_color = "firebrick"
p.yaxis.major_tick_line_width = 3
p.yaxis.minor_tick_line_color = "orange"



# change things only on the x-grid
p.xgrid.grid_line_color = "white"

# change things only on the Y-grid
p.ygrid.grid_line_color = "white"

conn = sqlite3.connect('.tt/shipDatabase.db')

c = conn.cursor()

for row in c.execute(
    """
        SELECT coords.x_coords, coords.y_coords, coords.id, coords.color
        FROM coords

        UNION

        SELECT planets.x_planet, planets.y_planet, planets.planet, planets.color
        FROM planets
        ORDER BY coords.x_coords
  """):

  p.scatter([row[0]], [row[1]], color=row[3], size=10, marker="hex")
  text = Label(x=row[0], y=row[1], text=row[2], text_color=row[3], text_font_size="25px")
  p.add_layout(text)

# set output to static HTML file
output_file(filename="graphCoord.html", title="Lotj Map")

save(p)

print("#showme Map done.")
