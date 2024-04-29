# 流れ
# 分散の差を検定
# 有意差の検定

import math
import numpy as np
import scipy.stats as stats
import glob, cv2, os

# 書き込み用ファイル
txtname = 't_result_dataup5_dataupno.txt'
f = open(txtname, 'a')

# 有意水準 0.05
alpha = 0.05

f.write(f"alpha : {alpha}")
f.write('\n')
f.write('\n')

# 検定対象

list1 = []
list2 = []
list1_1 = []
list2_1 = []

# 例1
# list1 = [165, 130, 182, 178, 194, 206, 160, 122, 212, 165, 247, 195]
# list2 = [180, 180, 235, 270, 240, 285, 164, 152]
# 例2
# list1 = [37.1,36.7,36.6,37.4,36.8,36.7,36.9,37.4,36.6,36.7]
# list2 = [36.8,36.6,36.5,37.0,36.7,36.5,36.6,37.1,36.4,36.7]

dir_Path1 = "data_up_no/dict_13"
dir_Path2 = "data_up_no/dict_65"
f.write(f"list1 : {dir_Path1} + {dir_Path2}")
f.write('\n')
file_list1 = glob.glob(os.path.join(dir_Path1, "*.txt"))
file_list2 = glob.glob(os.path.join(dir_Path2, "*.txt"))
file_name_list1 = []
for i, Path in enumerate(file_list1):
    # print(Path)
    file_name = os.path.basename(Path).split('.', 1)[0]
    file_name_list1.append(file_name)
    f1 = open(Path, 'r')
    datalist = f1.readlines()
    count = len(datalist)
    for j in range(count):
        datalist[j] = datalist[j].replace('\n', '')
        list1_1.append(float(datalist[j]))# ここから．とりあえず全部の値をリストに入れたい
    list1.append(list1_1)
    list1_1 = []
for i, Path in enumerate(file_list2):
    # print(Path)
    file_name = os.path.basename(Path).split('.', 1)[0]
    file_name_list1.append(file_name)
    f1 = open(Path, 'r')
    datalist = f1.readlines()
    count = len(datalist)
    for j in range(count):
        datalist[j] = datalist[j].replace('\n', '')
        list1_1.append(float(datalist[j]))# ここから．とりあえず全部の値をリストに入れたい
    list1.append(list1_1)
    list1_1 = []
# print(list1)
for i in range(int(len(list1) / 2)):
    # print(i, len(list_all[i]))
    list1[i] = list1[i] + list1[i + 18]
    # print(i, len(list1[i]))
# print(list1[5])

dir_Path1 = "data_up_5/dict_13"
dir_Path2 = "data_up_5/dict_65"
f.write(f"list2 : {dir_Path1} + {dir_Path2}")
f.write('\n')
f.write('\n')
file_list1 = glob.glob(os.path.join(dir_Path1, "*.txt"))
file_list2 = glob.glob(os.path.join(dir_Path2, "*.txt"))
file_name_list2 = []
for i, Path in enumerate(file_list1):
    # print(Path)
    file_name = os.path.basename(Path).split('.', 1)[0]
    file_name_list2.append(file_name)
    f1 = open(Path, 'r')
    datalist = f1.readlines()
    count = len(datalist)
    for j in range(count):
        datalist[j] = datalist[j].replace('\n', '')
        list2_1.append(float(datalist[j]))# ここから．とりあえず全部の値をリストに入れたい
    list2.append(list2_1)
    list2_1 = []
for i, Path in enumerate(file_list2):
    # print(Path)
    file_name = os.path.basename(Path).split('.', 1)[0]
    file_name_list2.append(file_name)
    f1 = open(Path, 'r')
    datalist = f1.readlines()
    count = len(datalist)
    for j in range(count):
        datalist[j] = datalist[j].replace('\n', '')
        list2_1.append(float(datalist[j]))# ここから．とりあえず全部の値をリストに入れたい
    list2.append(list2_1)
    list2_1 = []
# print(list1)
for i in range(int(len(list2) / 2)):
    # print(i, len(list_all[i]))
    list2[i] = list2[i] + list2[i + 18]
    # print(i, len(list1[i]))
# print(len(list2[5]))
print(file_name_list1)
print(file_name_list2)

# print(list1)
# print(list2)

# 有意差だったものの数
num_a = 0
num_b = 0

if len(list1) != len(list2):
    print(len(list1), len(list2))
    print("Error")
else:
    for i in range(18):
        # ファイル名
        f.write(file_name_list1[i])
        f.write('\n')
        print(file_name_list1[i])
        # それぞれの平均と分散
        mean1 = np.mean(list1[i])
        mean2 = np.mean(list2[i])
        var1 = np.var(list1[i], ddof = 1)
        var2 = np.var(list2[i], ddof = 1)
        list1_df = len(list1[i]) - 1
        list2_df = len(list2[i]) - 1
        f.write(f"free {list1_df}, {list2_df}")
        f.write('\n')
        # print(mean1, mean2, var1, var2, list1_df, list2_df)
        F = var1 / var2
        f.write(f"F_value : {F}")
        f.write('\n')
        print(f"F値 : {F}")

        # 両側検定の棄却域の閾値を計算
        f_critical_lower = stats.f.ppf(alpha / 2, list1_df, list2_df)
        f_critical_upper = stats.f.ppf(1 - alpha / 2, list1_df, list2_df)
        f.write(f"f_lower, f_upper : {f_critical_lower}, {f_critical_upper}")
        f.write('\n')
        print(f"棄却域の下限（F値）: {f_critical_lower}")
        print(f"棄却域の上限（F値）: {f_critical_upper}")

        if F < f_critical_lower or F > f_critical_upper:
            f.write("Welch")
            f.write('\n')
            print("ウェルチの検定")
            mean = mean1 -mean2
            T = mean / np.sqrt(var1 / (list1_df + 1) + var2 / (list2_df + 1))
            f.write(f"T_value : {T}")
            f.write('\n')
            print(f"T値 : {T}")
            # t検定の棄却域
            df = ((var1 / (list1_df + 1) + var2 / (list2_df + 1)) ** 2) / (((var1 ** 2) /  (((list1_df + 1) ** 2) * list1_df)) + ((var2 ** 2) /  (((list2_df + 1) ** 2) * list2_df)))
            # print(df)
            # 偶数丸めであることに注意
            df = round(df)
            # print(df)
            t_critical_lower = stats.t.ppf(alpha / 2, df)
            t_critical_upper = stats.t.ppf(1 - alpha / 2, df)
            f.write(f"t_lower, t_upper : {t_critical_lower}, {t_critical_upper}")
            f.write('\n')
            print(f"棄却域 : {t_critical_lower}, {t_critical_upper}")
            if T < t_critical_lower or T > t_critical_upper:
                f.write("Significant difference") 
                f.write('\n')
                print("帰無仮説は棄却される➡ 有意差あり")
                print(f"それぞれの平均値 : {mean1}, {mean2}")
                if np.fabs(mean1) < np.fabs(mean2):
                    print("list1の方が優れている")
                    f.write("list1 is better")
                    f.write('\n')
                else:
                    print("list2の方が優れている")
                    f.write("list2 is better")
                    f.write('\n')
                num_a += 1
            else:
                f.write("No significant difference")
                f.write('\n')
                print("帰無仮説は棄却されない➡ 有意差なし")
                num_b += 1
        else:
            f.write("t")
            f.write('\n')
            print("t検定")
            mean = mean1 -mean2
            s2 = (list1_df * var1 + list2_df * var2) / (list1_df + list2_df)
            T = mean / np.sqrt((1/(list1_df + 1) + 1/(list2_df + 1)) * s2)
            f.write(f"T_value : {T}")
            f.write('\n')
            print(f"T値 : {T}")
            # t検定の棄却域
            df = list1_df + list2_df
            t_critical_lower = stats.t.ppf(alpha / 2, df)
            t_critical_upper = stats.t.ppf(1 - alpha / 2, df)
            f.write(f"t_lower, t_upper : {t_critical_lower}, {t_critical_upper}")
            f.write('\n')
            print(f"棄却域 : {t_critical_lower}, {t_critical_upper}")
            if T < t_critical_lower or T > t_critical_upper:
                f.write("Significant difference")
                f.write('\n')
                f.write(f"mean : {mean1}, {mean2}")
                f.write('\n')
                print("帰無仮説は棄却される➡ 有意差あり")
                print(f"それぞれの平均値 : {mean1}, {mean2}")
                if np.fabs(mean1) < np.fabs(mean2):
                    print("list1の方が優れている")
                    f.write("list1 is better")
                    f.write('\n')
                else:
                    print("list2の方が優れている")
                    f.write("list2 is better")
                    f.write('\n')
                num_a += 1
            else:
                f.write("No significant difference")
                f.write('\n')
                print("帰無仮説は棄却されない➡ 有意差なし")
                num_b += 1
        f.write('\n')
        
f.write(f"Significant difference : {num_a}, No significant difference : {num_b}")
f.write('\n')
f.write('\n')
print(f"有意差あり : {num_a}, 有意差なし : {num_b}")

# 有意水準 0.1
alpha = 0.1

f.write(f"alpha : {alpha}")
f.write('\n')
f.write('\n')

# 検定対象

list1 = []
list2 = []
list1_1 = []
list2_1 = []

# 例1
# list1 = [165, 130, 182, 178, 194, 206, 160, 122, 212, 165, 247, 195]
# list2 = [180, 180, 235, 270, 240, 285, 164, 152]
# 例2
# list1 = [37.1,36.7,36.6,37.4,36.8,36.7,36.9,37.4,36.6,36.7]
# list2 = [36.8,36.6,36.5,37.0,36.7,36.5,36.6,37.1,36.4,36.7]

dir_Path1 = "data_up_no/dict_13"
dir_Path2 = "data_up_no/dict_65"
f.write(f"list1 : {dir_Path1} + {dir_Path2}")
f.write('\n')
file_list1 = glob.glob(os.path.join(dir_Path1, "*.txt"))
file_list2 = glob.glob(os.path.join(dir_Path2, "*.txt"))
file_name_list = []
for i, Path in enumerate(file_list1):
    # print(Path)
    file_name = os.path.basename(Path).split('.', 1)[0]
    file_name_list.append(file_name)
    f1 = open(Path, 'r')
    datalist = f1.readlines()
    count = len(datalist)
    for j in range(count):
        datalist[j] = datalist[j].replace('\n', '')
        list1_1.append(float(datalist[j]))# ここから．とりあえず全部の値をリストに入れたい
    list1.append(list1_1)
    list1_1 = []
for i, Path in enumerate(file_list2):
    # print(Path)
    file_name = os.path.basename(Path).split('.', 1)[0]
    file_name_list.append(file_name)
    f1 = open(Path, 'r')
    datalist = f1.readlines()
    count = len(datalist)
    for j in range(count):
        datalist[j] = datalist[j].replace('\n', '')
        list1_1.append(float(datalist[j]))# ここから．とりあえず全部の値をリストに入れたい
    list1.append(list1_1)
    list1_1 = []
# print(list1)
for i in range(int(len(list1) / 2)):
    # print(i, len(list_all[i]))
    list1[i] = list1[i] + list1[i + 18]
    # print(i, len(list1[i]))
# print(list1[5])

dir_Path1 = "data_up_5/dict_13"
dir_Path2 = "data_up_5/dict_65"
f.write(f"list2 : {dir_Path1} + {dir_Path2}")
f.write('\n')
f.write('\n')
file_list1 = glob.glob(os.path.join(dir_Path1, "*.txt"))
file_list2 = glob.glob(os.path.join(dir_Path2, "*.txt"))
file_name_list = []
for i, Path in enumerate(file_list1):
    # print(Path)
    file_name = os.path.basename(Path).split('.', 1)[0]
    file_name_list.append(file_name)
    f1 = open(Path, 'r')
    datalist = f1.readlines()
    count = len(datalist)
    for j in range(count):
        datalist[j] = datalist[j].replace('\n', '')
        list2_1.append(float(datalist[j]))# ここから．とりあえず全部の値をリストに入れたい
    list2.append(list2_1)
    list2_1 = []
for i, Path in enumerate(file_list2):
    # print(Path)
    file_name = os.path.basename(Path).split('.', 1)[0]
    file_name_list.append(file_name)
    f1 = open(Path, 'r')
    datalist = f1.readlines()
    count = len(datalist)
    for j in range(count):
        datalist[j] = datalist[j].replace('\n', '')
        list2_1.append(float(datalist[j]))# ここから．とりあえず全部の値をリストに入れたい
    list2.append(list2_1)
    list2_1 = []
# print(list1)
for i in range(int(len(list2) / 2)):
    # print(i, len(list_all[i]))
    list2[i] = list2[i] + list2[i + 18]

# print(list1)
# print(list2)

# 有意差だったものの数
num_a = 0
num_b = 0

if len(list1) != len(list2):
    print("Error")
else:
    for i in range(18):
        # ファイル名
        f.write(file_name_list[i])
        f.write('\n')
        print(file_name_list[i])
        # それぞれの平均と分散
        mean1 = np.mean(list1[i])
        mean2 = np.mean(list2[i])
        var1 = np.var(list1[i], ddof = 1)
        var2 = np.var(list2[i], ddof = 1)
        list1_df = len(list1[i]) - 1
        list2_df = len(list2[i]) - 1
        # print(mean1, mean2, var1, var2, list1_df, list2_df)
        F = var1 / var2
        f.write(f"F_value : {F}")
        f.write('\n')
        print(f"F値 : {F}")

        # 両側検定の棄却域の閾値を計算
        f_critical_lower = stats.f.ppf(alpha / 2, list1_df, list2_df)
        f_critical_upper = stats.f.ppf(1 - alpha / 2, list1_df, list2_df)
        f.write(f"f_lower, f_upper : {f_critical_lower}, {f_critical_upper}")
        f.write('\n')
        print(f"棄却域の下限（F値）: {f_critical_lower}")
        print(f"棄却域の上限（F値）: {f_critical_upper}")

        if F < f_critical_lower or F > f_critical_upper:
            f.write("Welch")
            f.write('\n')
            print("ウェルチの検定")
            mean = mean1 -mean2
            T = mean / np.sqrt(var1 / (list1_df + 1) + var2 / (list2_df + 1))
            f.write(f"T_value : {T}")
            f.write('\n')
            print(f"T値 : {T}")
            # t検定の棄却域
            df = ((var1 / (list1_df + 1) + var2 / (list2_df + 1)) ** 2) / (((var1 ** 2) /  (((list1_df + 1) ** 2) * list1_df)) + ((var2 ** 2) /  (((list2_df + 1) ** 2) * list2_df)))
            # print(df)
            # 偶数丸めであることに注意
            df = round(df)
            # print(df)
            t_critical_lower = stats.t.ppf(alpha / 2, df)
            t_critical_upper = stats.t.ppf(1 - alpha / 2, df)
            f.write(f"t_lower, t_upper : {t_critical_lower}, {t_critical_upper}")
            f.write('\n')
            print(f"棄却域 : {t_critical_lower}, {t_critical_upper}")
            if T < t_critical_lower or T > t_critical_upper:
                f.write("Significant difference") 
                f.write('\n')
                print("帰無仮説は棄却される➡ 有意差あり")
                print(f"それぞれの平均値 : {mean1}, {mean2}")
                f.write(f"means : {mean1}, {mean2}")
                f.write('\n')
                if np.fabs(mean1) < np.fabs(mean2):
                    print("list1の方が優れている")
                    f.write("list1 is better")
                    f.write('\n')
                else:
                    print("list2の方が優れている")
                    f.write("list2 is better")
                    f.write('\n')
                num_a += 1
            else:
                f.write("No significant difference")
                f.write('\n')
                print("帰無仮説は棄却されない➡ 有意差なし")
                num_b += 1
        else:
            f.write("t")
            f.write('\n')
            print("t検定")
            mean = mean1 -mean2
            s2 = (list1_df * var1 + list2_df * var2) / (list1_df + list2_df)
            T = mean / np.sqrt((1/(list1_df + 1) + 1/(list2_df + 1)) * s2)
            f.write(f"T_value : {T}")
            f.write('\n')
            print(f"T値 : {T}")
            # t検定の棄却域
            df = list1_df + list2_df
            t_critical_lower = stats.t.ppf(alpha / 2, df)
            t_critical_upper = stats.t.ppf(1 - alpha / 2, df)
            f.write(f"t_lower, t_upper : {t_critical_lower}, {t_critical_upper}")
            f.write('\n')
            print(f"棄却域 : {t_critical_lower}, {t_critical_upper}")
            if T < t_critical_lower or T > t_critical_upper:
                f.write("Significant difference")
                f.write('\n')
                print("帰無仮説は棄却される➡ 有意差あり")
                print(f"それぞれの平均値 : {mean1}, {mean2}")
                f.write(f"means : {mean1}, {mean2}")
                f.write('\n')
                if np.fabs(mean1) < np.fabs(mean2):
                    print("list1の方が優れている")
                    f.write("list1 is better")
                    f.write('\n')
                else:
                    print("list2の方が優れている")
                    f.write("list2 is better")
                    f.write('\n')
                num_a += 1
            else:
                f.write("No significant difference")
                f.write('\n')
                print("帰無仮説は棄却されない➡ 有意差なし")
                num_b += 1
        f.write('\n')
        
f.write(f"Significant difference : {num_a}, No significant difference : {num_b}")
f.write('\n')
f.write('\n')
print(f"有意差あり : {num_a}, 有意差なし : {num_b}")
f.close()