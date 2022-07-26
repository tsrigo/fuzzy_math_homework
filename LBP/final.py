import ULBP
import numpy as np
import os

def get_img(dirPath):
    '''返回 dirPath 下的所有图片'''

def get_closure(r):
    '''
    返回由模糊相似矩阵 r(n * n) 得到的模糊等价矩阵(传递闭包) R
    c_ij = ∨{(r_ik ∧ r_kj) | 1 ≤ k ≤ n}.
    '''
    n = len(r)
    R = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            R[i][j] = max([min(x, y) for x, y in zip(r[i], r[:, j])])
    
    return R


dirPath = "/data/1/"

file_dir = "D:\\Course\\XDU_Mathmatical_Modeling\\Fuzzy Mathematics\\fuzzy_mathematics_homework\\LBP\\data\\1"

for root, dirs, files in os.walk(file_dir, topdown=False):
    feature = []    # size of feature: 10 * 3776 (sampleNum * featureNum)  
    for f in files:
        loc = root + '\\' + f
        feature.append(ULBP.get_LBPH(loc))
            
n = len(feature)    # height of feature
m = len(feature[0]) # width of feature
r = np.zeros((n, n))     # similarity matrix
M = 0.008   

for i in range(n):     
    for j in range(n): 
        if i == j:
            r[i][j] = 1.0
        else:
            r[i][j] = 1 / sum([abs(x - y) for x, y in zip(feature[i], feature[j])])

print("\n所有 r_ij 是否均位于 [0, 1] 区间内：" + str(all([x <= 1 and x >= 0 for i in r for x in i])) + '\n')

R = get_closure(r)
print(R)