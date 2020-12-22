from data_reader import read_data
from k_means import k_means
from visualization import draw_graph,scatter_k_means

datafile = 'seeds_dataset.txt'
data = read_data(datafile)
colors = ['r','b','g','y']
markers = ['+','_','x','*']


for i in range(2,5):#k分别取2 3 4，对数据集进行聚类
	centers,clusters = k_means(data,k=i,t=100)
	text = 'k=' + str(i) + ',t=100'
	scatter_k_means(centers,clusters,colors,markers,text)
	figname = 'k=' + str(i) + '.png'
	draw_graph(title = 'k-means result',saveFig = figname)