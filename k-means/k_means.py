import numpy as np
import random

def k_means(data,k,t = 100):
	#初始化类中心
	centers = []
	for i in range(k):
		centers.append(list(random.choice(data)))

	centers = np.asarray(centers)

	for i in range(t):
		clusters = [[] for i in range(k)]
		for sample in data:#对每个样本点聚类
			clusters[_clustering(sample,centers)].append(sample)

		centers = _update_center(clusters)#更新中心点
	clusters = _cluster_to_array(clusters)
	return centers,clusters



def _distance(A,B):#计算两点之间欧式距离
	return ((A[0] - B[0])**2 + (A[1] - B[1])**2)**0.5


def _clustering(sample,center):
	distance_to_centers = [_distance(sample,center[i]) for i in range(len(center))]
	min_distance = min(distance_to_centers)
	return distance_to_centers.index(min_distance)

def _update_center(clusters):
	centers = []
	for k in range(len(clusters)):
		center = sum(clusters[k])/len(clusters[k])
		centers.append(center)
	return centers

def _cluster_to_array(clusters):
	for k in range(len(clusters)):
		clusters[k] = np.asarray(clusters[k])
	return clusters

