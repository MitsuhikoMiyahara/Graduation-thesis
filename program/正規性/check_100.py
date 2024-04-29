# 正規性らしさを確認する
# txtで偏差を受け取って，それを0を中心としてプロットする

import matplotlib.pyplot as plt
import glob, cv2, os
import math as np

dir_Path = "nomask_seg_result/dist"
file_list = glob.glob(os.path.join(dir_Path, "*.txt"))

# 全ての偏差の中で絶対値が最大のもの
abs_max = 0

for i, Path in enumerate(file_list):
    f = open(Path, 'r')
    datalist = f.readlines()
    count = len(datalist)
    for j in range(count):
        # print(datalist[i])
        datalist[j] = datalist[j].replace('\n', '')
        if np.fabs(float(datalist[j])) > abs_max:
            abs_max = np.fabs(float(datalist[j]))

# print(abs_max)

# ヒストグラムの表示
# 今回は-100~100までは10ごと，それ以降は50ごとに表示する
num_e =  abs_max - 100
num_f = int(num_e // 100 + 1)
num_g = 100 + 100 * num_f
# print(num_g)
# print(num_f)

# bin_list = [-1 * num_g + i * 100 for i in range(num_f)] + [-100 + i * 10 for i in range(20)] + [100 + i * 100 for i in range(num_f + 1)]

# print(bin_list)

# bin_list1 = [-600, 0, 600]

for i, Path in enumerate(file_list):
    # print(i)
    file_name = os.path.basename(Path).split('.', 1)[0]
    f = open(Path, 'r')

    datalist = f.readlines()
    count = len(datalist)

    # print(count)

    list_param = []
    for j in range(count):
        # print(datalist[i])
        datalist[j] = datalist[j].replace('\n', '')
        list_param.append(float(datalist[j]))
    # print(list_param)
    # print(len(list_param))
    # plt.xlim(0,50.0)    
    # plt.hist(list_param, bins = 20, range=(-100, 100), density=True)
    # print(abs_max)
    plt.hist(list_param, bins = 20, range = (-100, 100), density = True)
    plt.savefig(file_name)
    plt.close()
    # plt.show()