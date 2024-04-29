# 流れ
# 分散の差を検定
# 有意差の検定

import math
import numpy as np
import scipy.stats as stats
import glob, cv2, os

# 有意水準
alpha = 0.05
# alpha = 0.1

# 検定対象

list1 = []
list2 = []

# 例1
# list1 = [165, 130, 182, 178, 194, 206, 160, 122, 212, 165, 247, 195]
# list2 = [180, 180, 235, 270, 240, 285, 164, 152]
# 例2
# list1 = [37.1,36.7,36.6,37.4,36.8,36.7,36.9,37.4,36.6,36.7]
# list2 = [36.8,36.6,36.5,37.0,36.7,36.5,36.6,37.1,36.4,36.7]

path1 = "result_dist_1_x_5.txt"
path2 = "result_dist_1_x_no.txt"
f = open(path1, 'r')
datalist = f.readlines()
count = len(datalist)
for i in range(count):
    datalist[i] = datalist[i].replace('\n', '')
    list1.append(float(datalist[i]))
f.close()
f = open(path2, 'r')
datalist = f.readlines()
count = len(datalist)
for i in range(count):
    datalist[i] = datalist[i].replace('\n', '')
    list2.append(float(datalist[i]))
f.close()

# print(list1)
# print(list2)
# print(len(list1))
# print(len(list2))


# それぞれの平均と分散
mean1 = np.mean(list1)
mean2 = np.mean(list2)
var1 = np.var(list1, ddof = 1)
var2 = np.var(list2, ddof = 1)
list1_df = len(list1) - 1
list2_df = len(list2) - 1
# print(mean1, mean2, var1, var2, list1_df, list2_df)
F = var1 / var2
print(f"F値 : {F}")

# 両側検定の棄却域の閾値を計算
f_critical_lower = stats.f.ppf(alpha / 2, list1_df, list2_df)
f_critical_upper = stats.f.ppf(1 - alpha / 2, list1_df, list2_df)

print(f"棄却域の下限（F値）: {f_critical_lower}")
print(f"棄却域の上限（F値）: {f_critical_upper}")

if F < f_critical_lower or F > f_critical_upper:
    print("ウェルチの検定")
    mean = mean1 -mean2
    T = mean / np.sqrt(var1 / (list1_df + 1) + var2 / (list2_df + 1))
    print(f"T値 : {T}")
    # t検定の棄却域
    df = ((var1 / (list1_df + 1) + var2 / (list2_df + 1)) ** 2) / (((var1 ** 2) /  (((list1_df + 1) ** 2) * list1_df)) + ((var2 ** 2) /  (((list2_df + 1) ** 2) * list2_df)))
    # print(df)
    # 偶数丸めであることに注意
    df = round(df)
    # print(df)
    t_critical_lower = stats.t.ppf(alpha / 2, df)
    t_critical_upper = stats.t.ppf(1 - alpha / 2, df)
    print(f"棄却域 : {t_critical_lower}, {t_critical_upper}")
    if T < t_critical_lower or T > t_critical_upper:
        print("帰無仮説は棄却される➡ 有意差あり")
    else:
        print("帰無仮説は棄却されない➡ 有意差なし")
else:
    print("t検定")
    mean = mean1 -mean2
    s2 = (list1_df * var1 + list2_df * var2) / (list1_df + list2_df)
    T = mean / np.sqrt((1/(list1_df + 1) + 1/(list2_df + 1)) * s2)
    print(f"T値 : {T}")
    # t検定の棄却域
    df = list1_df + list2_df
    t_critical_lower = stats.t.ppf(alpha / 2, df)
    t_critical_upper = stats.t.ppf(1 - alpha / 2, df)
    print(f"棄却域 : {t_critical_lower}, {t_critical_upper}")
    if T < t_critical_lower or T > t_critical_upper:
        print("帰無仮説は棄却される➡ 有意差あり")
    else:
        print("帰無仮説は棄却されない➡ 有意差なし")