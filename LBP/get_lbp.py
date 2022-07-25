# -*- coding: utf-8 -*-
# get_LBP_from_Image.py
# 2015-7-7
# github: https://github.com/michael92ht
# __author__ = 'huangtao'

# import the necessary packages
import numpy as np
import cv2
from PIL import Image
from pylab import *


class LBP:

    def describe(self, image):
        '''将图像载入，并转化为灰度图，获取图像灰度图的像素信息'''
        image_array = np.array(Image.open(image).convert('L'))
        return image_array

    def calute_basic_lbp(self, image_array, i, j):
        '''
        图像的LBP原始特征计算算法：将图像指定位置的像素与周围8个像素比较，
        比中心像素大的点赋值为1，比中心像素小的赋值为0，返回得到的二进制序列
        '''
        sum = []
        if image_array[i - 1, j - 1] > image_array[i, j]:
            sum.append(1)
        else:
            sum.append(0)
        if image_array[i - 1, j] > image_array[i, j]:
            sum.append(1)
        else:
            sum.append(0)
        if image_array[i - 1, j + 1] > image_array[i, j]:
            sum.append(1)
        else:
            sum.append(0)
        if image_array[i, j - 1] > image_array[i, j]:
            sum.append(1)
        else:
            sum.append(0)
        if image_array[i, j + 1] > image_array[i, j]:
            sum.append(1)
        else:
            sum.append(0)
        if image_array[i + 1, j - 1] > image_array[i, j]:
            sum.append(1)
        else:
            sum.append(0)
        if image_array[i + 1, j] > image_array[i, j]:
            sum.append(1)
        else:
            sum.append(0)
        if image_array[i + 1, j + 1] > image_array[i, j]:
            sum.append(1)
        else:
            sum.append(0)
        return sum

    # 获取二进制序列进行不断环形旋转得到新的二进制序列的最小十进制值
    def get_min_for_revolve(self, arr):
        values = []
        circle = arr
        circle.extend(arr)
        for i in range(0, 8):
            j = 0
            sum = 0
            bit_num = 0
            while j < 8:
                sum += circle[i + j] << bit_num
                bit_num += 1
                j += 1
            values.append(sum)
        return min(values)

    # 获取值r的二进制中1的位数
    def calc_sum(self, r):
        num = 0
        while (r):
            r &= (r - 1)
            num += 1
        return num

    def lbp_basic(self, image_array):
        '''获取图像的LBP原始模式特征'''
        basic_array = np.zeros(image_array.shape, np.uint8)
        width = image_array.shape[0]
        height = image_array.shape[1]
        for i in range(1, width - 1):
            for j in range(1, height - 1):
                sum = self.calute_basic_lbp(image_array, i, j)
                bit_num = 0
                result = 0
                for s in sum:
                    result += s << bit_num
                    bit_num += 1
                basic_array[i, j] = result
        return basic_array

    def show_hist(self, img_array, im_bins, im_range):
        '''绘制指定维数和范围的图像灰度归一化统计直方图'''
        hist = cv2.calcHist([img_array], [0], None, im_bins, im_range)
        hist = cv2.normalize(hist, None).flatten()
        plt.plot(hist, color='r')
        plt.xlim(im_range)
        plt.show()

    
    def show_basic_hist(self, img_array):
        '''绘制图像原始LBP特征的归一化统计直方图'''
        self.show_hist(img_array, [256], [0, 256])

    def show_image(self, image_array):
        '''显示图像'''
        cv2.imshow('Image', image_array)
        cv2.waitKey(0)

def get_feature(image):
    '''返回image的 LBP 特征向量'''
    lbp = LBP()
    image_array = lbp.describe(image) # 一个大小和图像大小相等的的矩阵
    
    
    # 获取图像原始LBP特征
    basic_array = lbp.lbp_basic(image_array) # 一个大小和图像大小相等的的矩阵
    max_bins = int(basic_array.max() + 1) # .max()取lbp中最大的数
    test_hist, _ = np.histogram(basic_array, bins=max_bins, range=(0,max_bins)) #test_hist是某个灰度级的个数即y坐标。-是横坐标。
    return test_hist

if __name__ == '__main__':
    image = r"D:\\211.jpg";
    # image = r"C:\Users\wei\Pictures\hhh.jpg"
    lbp = LBP()
    image_array = lbp.describe(image) # 一个大小和图像大小相等的的矩阵
    basic_array = lbp.lbp_basic(image_array) # 一个大小和图像大小相等的的矩阵

    '''
    max_bins = int(basic_array.max() + 1)
    res = []
    for i in range(0, len(basic_array), x_step):
        for j in range(0, len(basic_array[0]), y_step):            
            a = basic_array[i:i + x_step, j:j + y_step]
            hist,bins = np.histogram(a, bins=max_bins, range=(0,max_bins))
            res.extend(hist)
    print(res)
    '''

    #lbp是像素矩阵
    max_bins = int(basic_array.max() + 1)#.max()取lbp中最大的数
    #test_hist是某个灰度级的个数即y坐标。-是横坐标。
    test_hist, _ = np.histogram(basic_array, bins=max_bins, range=(0,max_bins))
    print(test_hist)
