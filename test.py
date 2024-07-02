from bokeh.plotting import figure, output_file, show

p = figure(width=825, height=825)

# p.circle(34,22, radius=0.3, alpha=0.5)

p.scatter([1,2,3,4,5], [6,7,8,9,10], size=20, color="navy", alpha=0.5)

show(p)
