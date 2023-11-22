#The Bokeh library is specifically used for web browsers’ interactive data visualization.
#This library produces a JSON file (JavaScript Object Notation),
# used for transmitting data between a web application and a server
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.iris import flowers
def main():
    # line plot example
    x = [1, 2, 3, 4, 5]
    y = [5, 6, 1, 3, 4]
    output_file("line_example.html")
    plot = figure(title="Line Plot", x_axis_label="x axis",
    y_axis_label="y axis")
    plot.line(x, y, legend="line example", line_width=2)
    show(plot)
    # cos(x) function example
    output_file("cosx_example.html")
    x = np.linspace(-6, 6, 100)
    y = np.cos(x)
    plot = figure(width=500, height=500, title="Cos(x) Plot",
    x_axis_label="x axis", y_axis_label="y axis")
    plot.circle(x, y, size=7, color="firebrick", alpha=0.5,
    legend="cos(x) example")
    show(plot)
    # bar chart example
    output_file("barchart_example.html")
    teams = ["A", "B", "C", "D", "E", "F"]
    plot = figure(x_range=teams, height=500, title="Bar Chart Plot",
    x_axis_label="teams", y_axis_label="values")
    plot.vbar(x=teams, top=[4, 2, 3, 1, 3, 5], width=0.6,
    legend="bar chart example")
    show(plot)
    # iris flowers scatter example
    output_file("iris_scatter_example.html")
    colormap = {"setosa":"orange", "versicolor":"blue", "virginica":"gray"}
    colors = [colormap[x] for x in flowers['species']]
    plot = figure(title = "Iris Flowers Scatter Plot", x_axis_label=
    "petal length", y_axis_label="petal width")
    plot.circle(flowers["petal_length"], flowers["petal_width"],
    color=colors,
    fill_alpha=0.2, size=10, legend="scatter plot example")
    show(plot)
if __name__ == '__main__':
    main()