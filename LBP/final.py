import ULBP
import numpy as np
import os

def get_img(file_dir):
    '''返回 dirPath 下的所有图片'''
    for root, dirs, files in os.walk(file_dir, topdown=False):
        return [f for f in files]

def get_feature(files):
    feature = []        # LBPH特征值矩阵，size of feature: 10 * 3776 (sampleNum * featureNum)

    for f in files:
        loc = file_dir + '\\' + f
        feature.append(ULBP.get_LBPH(loc))
    return feature

def get_sMat(feature):
    '''由特征矩阵得到模糊相似矩阵(Fuzzy similarity matrix)'''
    r = np.zeros((n, n))
    for i in range(n):     
        for j in range(n): 
            if i == j:
                r[i][j] = 1.0
            else:
                r[i][j] = M * 1 / sum([abs(x - y) for x, y in zip(feature[i], feature[j])])
    return r

def get_closure(r):
    '''
    返回由模糊相似矩阵得到的模糊等价矩阵(传递闭包) R
    其中R_ij = ∨{(r_ik ∧ r_kj) | 1 ≤ k ≤ n}.
    '''
    n = len(r)
    R = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            R[i][j] = max([min(x, y) for x, y in zip(r[i], r[:, j])])
    
    return R

def get_range(R):
    '''根据模糊等价矩阵中的隶属度，确定一系列用以分类的lamda。'''
    res = []
    getRound = lambda x: round(x, 2)
    for i in R:
        res.extend(getRound(x) for x in i)
    return sorted(list(set(res)))

def get_truncation_matrix(R, lam):
    '''
    根据给定的 lambda，返回 R 的λ截矩阵
    '''
    res = []
    def cmp(x):
        if x >= lam: 
            return 1
        else: 
            return 0
    for row in R:
        res.append([cmp(x) for x in row])
    return res

def get_class(tMat):
    '''根据截断矩阵获得元素的分类'''
    # tMat = np.array(tMat)
    n = len(tMat)
    st = np.zeros(n, dtype = bool)
    res = []

    for i in range(n):
        if st[i] == True:
            continue;
        st[i] = True
        oneClass = [i]
        for j in range(i + 1, n):
            if tMat[i] == tMat[j]:
                st[j] = True
                oneClass.append(j)
        res.append(oneClass)
    return res

def putMat(R):
    '''用更直观的方式打印矩阵'''
    for i in R:
        print(i)
    print()


file_dir = "D:\\Course\\XDU_Mathmatical_Modeling\\Fuzzy Mathematics\\fuzzy_mathematics_homework\\LBP\\data\\1"

files = get_img(file_dir)
feature = get_feature(files)
            
n = len(feature)    # 高，Height of feature
m = len(feature[0]) # 宽，Width of feature
M = 85              # 绝对值倒数法的系数，Coefficients of the Reciprocal Absolute Value Method

r = get_sMat(feature)# 相似矩阵，Similarity matrix

print("\n所有 r_ij 是否均位于 [0, 1] 区间内：" + str(all([x <= 1 and x >= 0 for i in r for x in i])) + '\n')

R = get_closure(r)
# print("模糊等价矩阵为：")
# putMat(R)
ran = get_range(R)
print("lambda 的取值有：" + str(ran))

for lam in ran:
    tMat= get_truncation_matrix(R, lam)
    print(str(lam) + " 对应的截断矩阵为：")
    putMat(tMat)
    print(str(lam) + " 对应的分类为:")
    res = get_class(tMat)
    print(res, '\n')
