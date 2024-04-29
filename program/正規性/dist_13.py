import math as np


# テストデータの数
num_data = 6
# キーポイントの数
num_point = 8
f = open('nomask_seg_result/result_nomask_seg', 'r')
# f1.write("1\n")
datalist = f.readlines()
count = len(datalist)
list_param = []
param = []
for i in range(count):
    data = datalist[i]
    split_data = data.split()
    if len(split_data) == 1:
        param.append(split_data[0])
    if len(split_data) > 1:
        if split_data[0] != "score":
            param.append(split_data[2])
    if len(param) == 1 + 2 * num_point:
        list_param.append(param)
        param = []

print(list_param)
# # ここまでのcheck
# if len(list_param) == num_data:
#     print("OK")
# else:
#     print("FALSE")
f.close()
# 正解座標のdata
list_ans = [["test0", 52, 20, 49, 143, 37, 413, 56, 429, 48, 312, 43, 196, 41, 100, 50, 26],
 ["test1", 42, 22, 63, 151, 100, 433, 84, 453, 49, 329, 28, 238, 19, 115, 38, 25],
 ["test2", 101, 27, 82, 169, 49, 482, 7, 507, 49, 375, 82, 253, 103, 129, 101, 31],
 ["test3", 71, 22, 56, 169, 32, 510, 62, 524, 85, 381, 107, 255, 104, 126, 79, 26], 
 ["test4", 54, 6, 80, 255, 127, 807, 162, 847, 94, 601, 43, 395, 19, 185, 47, 11], 
 ["test5", 47, 37, 52, 195, 53, 541, 63, 562, 40, 401, 29, 260, 25, 137, 43, 42], 
 ["test6", 40, 18, 45, 133, 51, 385, 59, 399, 40, 291, 24, 195, 19, 103, 37, 20], 
 ["test7", 29, 17, 54, 166, 103, 509, 103, 529, 63, 395, 31, 267, 13, 133, 23, 20], 
 ["test8", 25, 22, 34, 132, 51, 381, 68, 404, 43, 290, 24, 190, 15, 94, 22, 26], 
 ["test9", 65, 24, 53, 182, 36, 539, 17, 576, 50, 407, 70, 261, 82, 132, 70, 27], 
 ["test10", 29, 23, 41, 191, 72, 519, 20, 557, 33, 403, 46, 249, 45, 123, 29, 29], 
 ["test11", 41, 21, 76, 185, 136, 529, 154, 585, 95, 436, 52, 301, 26, 157, 36, 28], 
 ["test12", 50, 22, 52, 170, 58, 488, 79, 533, 49, 372, 29, 233, 25, 112, 46, 23]]

true_list = []

num_data = len(list_ans)


for i in range(num_data):
    num_a = list_ans[i][1] - list_ans[i][5]
    num_b = list_ans[i][2] - list_ans[i][6]
    num_c = num_a ** 2 + num_b ** 2
    num_d = float(np.sqrt(num_c))
    true_list.append(num_d)
#     f1.write(str(num_d))
#     f1.write(",")
# f1.write("\n")

print("それぞれのマストの長さ：",true_list)

base = 500.0
# f1.write("base = ")
# f1.write(str(base))
# f1.write("\n")

scale_list = []

for i in range(len(true_list)):
    num_s = base / true_list[i]
    # print(num_s)
    # f1.write(str(num_s))
    # f1.write(",")
    scale_list.append(num_s)
print("比率:", scale_list)
# f1.write("\n")


dis_list = []
dis = []
# dis_all = []

list_score = [0,0,0,0,0,0,0,0]

for i in range(num_data):
    for j in range(num_data):
        if list_ans[i][0] == list_param[j][0]:
            dis.append(list_ans[i][0])
            for k in range(num_point * 2):
                # if float(list_ans[i][k + 1]) > float(list_param[j][k + 1]):
                #     num = float(list_ans[i][k + 1]) - float(list_param[j][k + 1])
                # else:
                #     num = float(list_param[j][k + 1]) - float(list_ans[i][k + 1])
                num = float(list_param[j][k + 1]) - float(list_ans[i][k + 1])
                num = num * scale_list[i]
                dis.append(num)
    dis_list.append(dis)
    dis = []

print(dis_list)

# x,yに分ける

list_x = []
list_y = []

# キーポイントの番号
list_key = [ 1, 2, 3, 4, 5, 6, 7, 8]

txtname = 'result_dist_x.txt'
f3 = open(txtname, 'a')
txtname = 'result_dist_y.txt'
f4 = open(txtname, 'a')


for i in range(len(list_key)):
    txtname = 'result_dist_' + str(list_key[i]) + '_x.txt'
    f1 = open(txtname, 'a')
    txtname = 'result_dist_' + str(list_key[i]) + '_y.txt'
    f2 = open(txtname, 'a')

    num_key = int(list_key[i]) * 2 - 1

    for j in range(len(dis_list)):
        f1.write(str(dis_list[j][num_key]))
        f2.write(str(dis_list[j][num_key + 1]))
        f1.write('\n')
        f2.write('\n')
        f3.write(str(dis_list[j][num_key]))
        f4.write(str(dis_list[j][num_key + 1]))
        f3.write('\n')
        f4.write('\n')
    f1.close()
    f2.close()