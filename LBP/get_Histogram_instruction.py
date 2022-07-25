# CSDN: https://blog.csdn.net/qq_44386182/article/details/124031615
# Author: https://blog.csdn.net/qq_44386182

import numpy as np
import skimage

# histogram(a,bins=10,range=None,weights=None,density=False);
 
# a是待统计数据的数组；
 
# bins指定统计的区间个数；
 
# range是一个长度为2的元组，表示统计范围的最小值和最大值，默认值None，表示范围由数据的范围决定
 
# weights为数组的每个元素指定了权值,histogram()会对区间中数组所对应的权值进行求和
 
# density为True时，返回每个区间的概率密度；为False，返回每个区间中元素的个数
 
a = np.random.rand(10, 10)
print(a)
hist,bins = np.histogram(a,bins=5,range=(0,1), density= True)
print(np.histogram(a,bins=5,range=(0,1), density= False)[0])
print(hist)
# print(bins)