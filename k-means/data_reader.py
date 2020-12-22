import numpy as np


def read_data(filename,i=3,j=4):#默认读取数据集第3和4列
	try:
		with open(filename) as f:
			data_list = []
			for line in f:
				line_split = line.split('\t')
				line_list = [float(i.rstrip()) for i in line_split if i.rstrip() != '']
				data_list.append(line_list)
	except FileNotFoundError:
		print('the file',filename,'does not exist!')
	else:
		data_arr = np.asarray(data_list)
		return data_arr[...,i:j+1]


