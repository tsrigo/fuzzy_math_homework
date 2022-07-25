# CSDN: https://blog.csdn.net/lk3030/article/details/84034963
# __author__ = https://blog.csdn.net/lk3030

import cv2
import numpy as np

def uniform_pattern_LBP(img,radius=3, neighbors=8):
    h,w=img.shape
    dst = np.zeros((h-2*radius, w-2*radius),dtype=img.dtype)
    # LBP特征值对应图像灰度编码表，直接默认采样点为8位
    temp = 1
    table =np.zeros((256),dtype=img.dtype)
    for i in range(256):
        if getHopTimes(i)<3:
            table[i] = temp
            temp+=1
    # 是否进行UniformPattern编码的标志
    flag = False
    # 计算LBP特征图
    for k in range(neighbors):
        if k==neighbors-1:
            flag = True
      
        # 计算采样点对于中心点坐标的偏移量rx，ry
        rx = radius * np.cos(2.0 * np.pi * k / neighbors)
        ry = -(radius * np.sin(2.0 * np.pi * k / neighbors))
        # 为双线性插值做准备
        # 对采样点偏移量分别进行上下取整
        x1 = int(np.floor(rx))
        x2 = int(np.ceil(rx))
        y1 = int(np.floor(ry))
        y2 = int(np.ceil(ry))
        # 将坐标偏移量映射到0-1之间
        tx = rx - x1
        ty = ry - y1
        # 根据0-1之间的x，y的权重计算公式计算权重，权重与坐标具体位置无关，与坐标间的差值有关
        w1 = (1-tx) * (1-ty)
        w2 =    tx  * (1-ty)
        w3 = (1-tx) *    ty
        w4 =    tx  *    ty
        # 循环处理每个像素
        for i in range(radius,h-radius):
            for j in range(radius,w-radius):
                # 获得中心像素点的灰度值
                center = img[i,j]
                # 根据双线性插值公式计算第k个采样点的灰度值
                neighbor = img[i+y1,j+x1] * w1 + img[i+y2,j+x1] *w2 + img[i+y1,j+x2] *  w3 +img[i+y2,j+x2] *w4
                # LBP特征图像的每个邻居的LBP值累加，累加通过与操作完成，对应的LBP值通过移位取得
                dst[i-radius,j-radius] |= (neighbor>center)  <<  (np.uint8)(neighbors-k-1)
                # 进行LBP特征的UniformPattern编码
                if flag:
                    dst[i-radius,j-radius] = table[dst[i-radius,j-radius]]
    return dst
             
def getHopTimes(data):
    '''
    计算跳变次数
    '''
    count = 0;
    binaryCode = "{0:0>8b}".format(data)
     
    for i in range(1,len(binaryCode)):
        if binaryCode[i] != binaryCode[(i-1)]:
            count+=1
    return count

def getLBPH(img_lbp,numPatterns = 59,grid_x = 8,grid_y = 8,normed = True):
    '''
    计算LBP特征图像的直方图LBPH
    '''
    h,w=img_lbp.shape
    width = int(w / grid_x)
    height = int(h / grid_y)
    # 定义LBPH的行和列，grid_x*grid_y表示将图像分割的块数，numPatterns表示LBP值的模式种类
    result = np.zeros((grid_x * grid_y,numPatterns),dtype=float)
    resultRowIndex = 0
    # 对图像进行分割，分割成grid_x*grid_y块，grid_x，grid_y默认为8
    for i in range(grid_x):
        for j in range(grid_y):
            # 图像分块
            src_cell = img_lbp[i*height:(i+1)*height,j*width:(j+1)*width]
            # 计算直方图
            hist_cell = getLocalRegionLBPH(src_cell,0,(numPatterns-1),True)
            #将直方图放到result中
            result[resultRowIndex]=hist_cell
            resultRowIndex+=1
    return np.reshape(result,(-1))

def getLocalRegionLBPH(src,minValue,maxValue,normed):
    '''
    计算一个LBP特征图像块的直方图
    '''
    # 把二维的 src 变为 1 维的
    data = np.reshape(src,(-1))
    # 计算得到直方图bin的数目，直方图数组的大小
    bins = maxValue - minValue + 1;
    # 定义直方图每一维的bin的变化范围
    ranges = (float(minValue),float(maxValue + 1))
    hist, bin_edges = np.histogram(src, bins=bins, range=ranges, normed=normed)
    return hist

def get_LBPH(imgDir):
    gray = cv2.imread(imgDir, cv2.IMREAD_GRAYSCALE)
    uniform_pattern = uniform_pattern_LBP(gray,3,8)
    lbph = getLBPH(uniform_pattern,59,8,8,True)
    return lbph
