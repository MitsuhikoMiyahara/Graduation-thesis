# 正規性らしさを確認する
# txtで偏差を受け取って，それを0を中心としてプロットする

import matplotlib.pyplot as plt
import glob, cv2, os
import math as np

dir_Path = "nomask_seg_result/dist_65"
file_list1 = glob.glob(os.path.join(dir_Path, "*.txt"))

# 全ての偏差の中で絶対値が最大のもの
abs_max = 0

for i, Path in enumerate(file_list1):
    f = open(Path, 'r')
    datalist1 = f.readlines()
    count = len(datalist1)
    for j in range(count):
        # print(datalist[i])
        datalist1[j] = datalist1[j].replace('\n', '')

dir_Path = "nomask_seg_result/dist_13"
file_list2 = glob.glob(os.path.join(dir_Path, "*.txt"))
for i, Path in enumerate(file_list2):
    f = open(Path, 'r')
    datalist2 = f.readlines()
    count = len(datalist2)
    for j in range(count):
        # print(datalist[i])
        datalist2[j] = datalist2[j].replace('\n', '')

print(datalist1)
print(datalist2)

print(len(datalist1))
print(len(datalist2))

datalist = []

for i in range(len(datalist1)):
    datalist.append(datalist1[i])
for i in range(len(datalist2)):
    datalist.append(datalist2[i])

print(datalist)
print(len(datalist))

for i in range(len(datalist)):
    if np.fabs(float(datalist[i])) > abs_max:
        abs_max = np.fabs(float(datalist[i]))
print(abs_max)

# ヒストグラムの表示
# 今回は-100~100までは10ごと，それ以降は100ごとに表示する
num_e =  abs_max - 100
num_f = int(num_e // 100 + 1)
num_g = 100 + 100 * num_f
print(num_g)
print(num_f)

bin_list = [-1 * num_g + i * 100 for i in range(num_f)] + [-100 + i * 10 for i in range(20)] + [100 + i * 100 for i in range(num_f + 1)]

print(bin_list)

list_all = []
list_na = []

for i, Path in enumerate(file_list1):
    # print(i)
    file_name = os.path.basename(Path).split('.', 1)[0]
    list_na.append(file_name)
    f = open(Path, 'r')

    datalist_1 = f.readlines()
    count = len(datalist_1)
    list_param = []
    for j in range(count):
        # print(datalist[i])
        datalist_1[j] = datalist_1[j].replace('\n', '')
        list_param.append(float(datalist_1[j]))
    list_all.append(list_param)
    list_param = []

for i, Path in enumerate(file_list2):
    # print(i)
    file_name = os.path.basename(Path).split('.', 1)[0]
    f = open(Path, 'r')

    datalist_2 = f.readlines()
    count = len(datalist_2)
    list_param = []
    for j in range(count):
        # print(datalist[i])
        datalist_2[j] = datalist_2[j].replace('\n', '')
        list_param.append(float(datalist_2[j]))
    list_all.append(list_param)
    list_param = []
        # print(count)
print(int(len(list_all) / 2))
for i in range(int(len(list_all) / 2)):
    # print(i, len(list_all[i]))
    list_all[i] = list_all[i] + list_all[i + 18]
    print(i, len(list_all[i]))


print(len(list_na))

for i in range(len(list_na)):
    plt.hist(list_all[i], bins = 20, range = (-100, 100), density = True)
    plt.savefig(list_na[i])
    plt.close()
    # plt.show()