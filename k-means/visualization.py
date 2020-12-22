import matplotlib.pyplot as plt



def draw_graph(title = None,xlabel = 'length',ylabel = 'width',saveFig = None,show = True):
	
	if title:
		plt.title(title,fontsize = 24)

	plt.xlabel(xlabel,fontsize = 14)
	plt.ylabel(ylabel,fontsize = 14)
	
	if saveFig:
		plt.savefig(saveFig,bbox_inches = 'tight')

	if show:
		plt.show()
	pass


#将聚类结果绘制成散点图
def scatter_k_means(centers,clusters,colors,markers,text = None):

	k = len(clusters)

	x_centers = [c[0] for c in centers]
	y_centers = [c[1] for c in centers]

	if text:
		plt.text(x = 5,y = 4, s = text)


	for i in range(k):
		cx = x_centers[i]
		cy = y_centers[i]

		x = clusters[i][...,0]
		y = clusters[i][...,1]

		color = colors[i]
		m = markers[i]

		plt.scatter(cx,cy,c = color,marker ='o',alpha = 0.3)
		plt.scatter(x,y,c = color, marker = m)

	