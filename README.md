# k-means
k-均值聚类算法的简单实现与测试，主要用于机器学习导引课程论文。

# 运行环境
Python 3.7.9
numpy 1.19.4
matplotlib 3.3.3

# 数据集简介
所用数据集是uci机器学习数据库 (http://archive.ics.uci.edu/ml/datasets.php) 中的一个小麦种子数据集 (http://archive.ics.uci.edu/ml/datasets/seeds) ,数据集文件为seeds_dataset.txt。

# 项目简介
算法实现代码为k_means.py,data_reader.py用于读取数据，visualization.py用于数据可视化，将数据绘制成散点图。
test0.py将未聚类前数据集绘制成散点图，test1.py测试取不同k值时聚类结果，test2.py测试k取3且加入3个异常点时聚类结果。
result文件夹里为实验所得结果图。
