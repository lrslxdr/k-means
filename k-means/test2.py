import numpy as np
from data_reader import read_data
from k_means import k_means
from visualization import draw_graph,scatter_k_means

datafile = 'seeds_dataset.txt'
data = read_data(datafile)
#加入三个异常点到数据集中
data = np.vstack([data,[8.0,2.0]])
data = np.vstack([data,[8.0,3.0]])
data = np.vstack([data,[9.0,4.0]])

colors = ['r','b','g','y']
markers = ['+','_','x','*']

centers,clusters = k_means(data,k = 3,t = 100)

scatter_k_means(centers,clusters,colors,markers,text = 'k=3,t=100')
draw_graph(title = 'k-means result')