import matplotlib.pyplot as plt
from data_reader import read_data
from visualization import draw_graph

datafile = 'seeds_dataset.txt'
data = read_data(datafile)

x = data[...,0]
y = data[...,1]

plt.scatter(x,y)#数据集散点图

draw_graph(title = 'seeds_scatter',saveFig = 'seeds-scatter.png')
