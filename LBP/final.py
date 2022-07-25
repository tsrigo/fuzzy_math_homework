import get_lbp
import ULBP
import os

def get_img(dirPath):
    '''返回 dirPath 下的所有图片'''

dirPath = "/data/1/"

file_dir = "D:\\Course\\XDU_Mathmatical_Modeling\\Fuzzy Mathematics\\fuzzy_mathematics_homework\\LBP\\data\\1"
r = []
for root, dirs, files in os.walk(file_dir, topdown=False):
    feature = []
    for f in files:
        loc = root + '\\' + f
        print(loc)
        feature.append(ULBP.get_LBPH(loc))
    print(feature)

# for i in range(len(feature)):
#     for j in range(len(feature)):

