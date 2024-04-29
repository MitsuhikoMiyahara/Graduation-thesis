import glob, cv2, os
import numpy as np

# テストデータの数
num_data = 13
# キーポイントの数
num_point = 8

f = open('result_mask', 'r')
datalist = f.readlines()
count = len(datalist)
# print(count)

# list_param = []
# param = []

# for i in range(count):
#     data = datalist[i]
#     # print(data)
#     split_data = data.split()
#     if len(split_data) == 1:
#         # print(split_data[0][4])
#         number = split_data[0][4]
#         if split_data[0][5] != '.':
#             number = number + split_data[0][5]
#         param.append(number)
#     if len(split_data) > 1:
#         param.append(split_data[2])
#     if len(param) == 2 + 2 * num_point:
#         list_param.append(param)
#         param = []
# if len(list_param) == num_data:
#     print("OK")
# else:
#     print("FALSE")
# f.close()

list_param = [["0",1, 52, 20, 49, 143, 37, 413, 56, 429, 48, 312, 43, 196, 41, 100, 50, 26],
 ["1",1, 42, 22, 63, 151, 100, 433, 84, 453, 49, 329, 28, 238, 19, 115, 38, 25],
 ["2",1, 101, 27, 82, 169, 49, 482, 7, 507, 49, 375, 82, 253, 103, 129, 101, 31],
 ["3",1, 71, 22, 56, 169, 32, 510, 62, 524, 85, 381, 107, 255, 104, 126, 79, 26], 
 ["4",1, 54, 6, 80, 255, 127, 807, 162, 847, 94, 601, 43, 395, 19, 185, 47, 11], 
 ["5",1, 47, 37, 52, 195, 53, 541, 63, 562, 40, 401, 29, 260, 25, 137, 43, 42], 
 ["6",1, 40, 18, 45, 133, 51, 385, 59, 399, 40, 291, 24, 195, 19, 103, 37, 20], 
 ["7",1, 29, 17, 54, 166, 103, 509, 103, 529, 63, 395, 31, 267, 13, 133, 23, 20], 
 ["8",1, 25, 22, 34, 132, 51, 381, 68, 404, 43, 290, 24, 190, 15, 94, 22, 26], 
 ["9",1, 65, 24, 53, 182, 36, 539, 17, 576, 50, 407, 70, 261, 82, 132, 70, 27], 
 ["10",1, 29, 23, 41, 191, 72, 519, 20, 557, 33, 403, 46, 249, 45, 123, 29, 29], 
 ["11",1, 41, 21, 76, 185, 136, 529, 154, 585, 95, 436, 52, 301, 26, 157, 36, 28], 
 ["12",1, 50, 22, 52, 170, 58, 488, 79, 533, 49, 372, 29, 233, 25, 112, 46, 23]]

print(list_param)


dir_Path = "scoretest/"
file_list = glob.glob(os.path.join(dir_Path, "*.jpg"))

# 交点計算
mast_top = []
mast_point = []
mast_bottom = []
boom_edge = []
reach_point3 = []
reach_point2 = []
reach_point1 = []
reach_top = []
mast_list = []
reach_list = []

all_list = []
alllist = []

# 交点リスト
cross_list = []

for i in range(len(list_param)):
    a = 0
    num = int(list_param[i][0])
    mast_top.append(int(list_param[i][2]))
    mast_top.append(int(list_param[i][3]))
    mast_point.append(int(list_param[i][4]))
    mast_point.append(int(list_param[i][5]))
    mast_bottom.append(int(list_param[i][6]))
    mast_bottom.append(int(list_param[i][7]))
    boom_edge.append(int(list_param[i][8]))
    boom_edge.append(int(list_param[i][9]))
    reach_point3.append(int(list_param[i][10]))
    reach_point3.append(int(list_param[i][11]))
    reach_point2.append(int(list_param[i][12]))
    reach_point2.append(int(list_param[i][13]))
    reach_point1.append(int(list_param[i][14]))
    reach_point1.append(int(list_param[i][15]))
    reach_top.append(int(list_param[i][16]))
    reach_top.append(int(list_param[i][17]))
    mast_list.append(mast_top)
    mast_list.append(mast_point)
    mast_list.append(mast_bottom)
    reach_list.append(boom_edge)
    reach_list.append(reach_point3)
    reach_list.append(reach_point2)
    reach_list.append(reach_point1)
    # reach_list.append(reach_top)
    # all_list.append(num)
    all_list.append(mast_top)
    all_list.append(mast_point)
    all_list.append(mast_bottom)
    all_list.append(boom_edge)
    all_list.append(reach_point3)
    all_list.append(reach_point2)
    all_list.append(reach_point1)
    all_list.append(reach_top)
    alllist.append(all_list)
    all_list = []


    # print(list_param[i],num,mast_top,mast_point,mast_bottom,boom_edge,reach_point3,reach_point2,reach_point1,reach_top)

    cross_point=[]
    # cross_point=(0,0)
    # mast_topとmast_pointとの交点
    pointA = mast_list[0]
    pointB = mast_list[1]
    for j in range(len(reach_list) - 1):
        pointC = reach_list[j]
        pointD = reach_list[j + 1]
        bunbo = (pointB[0] - pointA[0]) * (pointD[1] - pointC[1]) - (pointB[1] - pointA[1]) * (pointD[0] - pointC[0])
        if bunbo != 0:
            vectorAC = ((pointC[0] - pointA[0]), (pointC[1] - pointA[1]))
            r = ((pointD[1] - pointC[1]) * vectorAC[0] - (pointD[0] - pointC[0]) * vectorAC[1]) / bunbo
            distance = ((pointB[0] - pointA[0]) * r, (pointB[1] - pointA[1]) * r)
            cross_point.append(int(pointA[0] + distance[0]))
            cross_point.append(int(pointA[1] + distance[1]))
            # cross_point = (int(pointA[0] + distance[0]), int(pointA[1] + distance[1]))
            if (cross_point[1] >  pointD[1] and cross_point[1] < pointC[1] and cross_point[1] >  pointA[1] and cross_point[1] < pointB[1]):
                # print(num, cross_point, 0, j)
                cross = []
                cross.append(num)
                cross.append(cross_point)
                cross.append(a)
                a += 1
                cross.append("a")
                cross_list.append(cross)
            cross_point = []
    # mast_topとmast_pointとの交点
    pointA = mast_list[1]
    pointB = mast_list[2]
    for j in range(len(reach_list) - 1):
        pointC = reach_list[j]
        pointD = reach_list[j + 1]
        bunbo = (pointB[0] - pointA[0]) * (pointD[1] - pointC[1]) - (pointB[1] - pointA[1]) * (pointD[0] - pointC[0])
        if bunbo != 0:
            vectorAC = ((pointC[0] - pointA[0]), (pointC[1] - pointA[1]))
            r = ((pointD[1] - pointC[1]) * vectorAC[0] - (pointD[0] - pointC[0]) * vectorAC[1]) / bunbo
            distance = ((pointB[0] - pointA[0]) * r, (pointB[1] - pointA[1]) * r)
            cross_point.append(int(pointA[0] + distance[0]))
            cross_point.append(int(pointA[1] + distance[1]))
            # cross_point = (int(pointA[0] + distance[0]), int(pointA[1] + distance[1]))
        # print(cross_point[1])
            if (cross_point[1] >  pointD[1] and cross_point[1] < pointC[1] and cross_point[1] >  pointA[1] and cross_point[1] < pointB[1]):
                # print(num, cross_point, 1, j)
                cross = []
                cross.append(num)
                cross.append(cross_point)
                cross.append(a)
                a += 1
                cross.append("b")
                cross_list.append(cross)
            cross_point = []
        # print(a)
        # a += 1



    mast_top = []
    mast_point = []
    mast_bottom = []
    boom_edge = []
    reach_point3 = []
    reach_point2 = []
    reach_point1 = []
    reach_top = []
    mast_list = []
    reach_list = []

# print(cross_list)
# print(len(cross_list))
# print(cross_list[10])

# num_m = 0
delete_list = []

# 同じ画像でふたつの交点があった場合、座標が上の方を採用する
# popする番号を取得
for i in range(len(cross_list) - 1):
    # print(i)
    # print(cross_list[i - num_m])
    if cross_list[i][0] == cross_list[i + 1][0]:
        # if cross_list[i][2] == cross_list[i + 1][2]:
            if cross_list[i][3] != cross_list[i + 1][3]:
                delete_list.append(i+1)
                # cross_list.pop(i + 1)
            else:
                if cross_list[i][1][1] < cross_list[i + 1][1][1]:
                    delete_list.append(i+1)

                    # cross_list.pop(i + 1)
                else:
                    delete_list.append(i)
                    # cross_list.pop(i)
# print(delete_list)
# delete_list = [4,5,2,1,2]
# 被りを消して昇順に
delete_list = list(set(delete_list))
# print(delete_list)

for i in range(len(delete_list)):
    cross_list.pop(int(delete_list[len(delete_list) - i - 1]))

# print(cross_list)


# 塗りつぶす範囲[testnumber,書かれる順番,交点]
color_list_1 = []
color_list = []

for i, imgPath in enumerate(file_list):
    # print(imgPath[14], imgPath[15])

    num = imgPath[14]

    if imgPath[15] != '.':
        num = num + imgPath[15]
    # print(num)
    color_list_1.append(int(num))

    for j in range(len(list_param)):
        # print(imgPath, list_param[j][0])
        if int(num) == int(list_param[j][0]):
            # print(num, list_param[j][0])
            num_a = j
    
    num_a = int(num_a)
    
    # print(num, imgPath, list_param[num][0])

    color_list_1.append(num_a)

    # print(color_list_1)

    for j in range(len(cross_list)):
        if cross_list[j][0] == int(num):
            color_list_1.append(cross_list[j][1])
            color_list_1.append(cross_list[j][3])

    # print(color_list_1)
    color_list.append(color_list_1)
    color_list_1 = []
# print(color_list)


for i in range(len(color_list)):
    # print(i)
    if len(color_list[i]) == 2:
        for j in range(len(alllist[color_list[i][1]])):
            # print(j)
            color_list[i].append(alllist[color_list[i][1]][j])
    else:
        for j in range(len(alllist[color_list[i][1]])):
            # print(j)
            # print(alllist[color_list[i][1]][j][1], color_list[i][2][1])
            if alllist[color_list[i][1]][j][1] < color_list[i][2][1]:
                color_list[i].append(alllist[color_list[i][1]][j])
print(color_list)

                    
for i in range(len(color_list)):
    if color_list[i][3] == 'a':
        # print(1)
        color_list[i][2], color_list[i][4] = color_list[i][4], color_list[i][2]
        color_list[i].pop(3)
    elif color_list[i][3] == 'b':
        # print(2)
        color_list[i][2], color_list[i][4] = color_list[i][4], color_list[i][2]
        color_list[i][4], color_list[i][5] = color_list[i][5], color_list[i][4]
        color_list[i].pop(3)

# print(alllist)
# print(len(alllist))
# print(len(alllist[0]))

print(color_list)

# 色塗り
for i, imgPath in enumerate(file_list):
    # print(imgPath[14], imgPath[15])

    num = imgPath[14]

    if imgPath[15] != '.':
        num = num + imgPath[15] 

    for j in range(len(list_param)):
        # print(imgPath, list_param[j][0])
        if int(num) == int(list_param[j][0]):
            # print(num, list_param[j][0])
            num_a = j
    
    num = int(num_a)


    
    # print(num, imgPath, list_param[num][0])

    img = cv2.imread(imgPath)
    file_name = os.path.basename(imgPath).split('.', 1)[0]
    shape = img.shape
    height = shape[0]
    width = shape[1]
    blank = np.zeros((height, width, 3))
    blank += 255

    # mast_top
    count = num_point
    # for l in range(count):
    #     if l == 0 or  l == 1 or l == 2:
    #         cv2.circle(img,
    #                 center=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
    #                 radius=5,
    #                 color=(255, 0, 0),
    #                 thickness=-1,
    #                 lineType=cv2.LINE_4,
    #                 shift=0)
            
    #         cv2.circle(blank,
    #                 center=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
    #                 radius=5,
    #                 color=(255, 0, 0),
    #                 thickness=-1,
    #                 lineType=cv2.LINE_4,
    #                 shift=0)
    #     else:
    #         cv2.circle(img,
    #                 center=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
    #                 radius=5,
    #                 color=(0, 255, 0),
    #                 thickness=-1,
    #                 lineType=cv2.LINE_4,
    #                 shift=0)
            
    #         cv2.circle(blank,
    #                 center=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
    #                 radius=5,
    #                 color=(0, 255, 0),
    #                 thickness=-1,
    #                 lineType=cv2.LINE_4,
    #                 shift=0)
    
    # for l in range(count):
    #     if l != num_point - 1:
    #         cv2.line(img,
    #                 pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
    #                 pt2=(int(list_param[num][l * 2 + 4]), int(list_param[num][l * 2 + 5])),
    #                 color=(0, 0, 0),
    #                 thickness=3,
    #                 lineType=cv2.LINE_4,
    #                 shift=0)
    #         cv2.line(blank,
    #                 pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
    #                 pt2=(int(list_param[num][l * 2 + 4]), int(list_param[num][l * 2 + 5])),
    #                 color=(0, 0, 0),
    #                 thickness=3,
    #                 lineType=cv2.LINE_4,
    #                 shift=0)
    #     else:
    #         cv2.line(img,
    #                 pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
    #                 pt2=(int(list_param[num][0 * 2 + 2]), int(list_param[num][0 * 2 + 3])),
    #                 color=(0, 0, 0),
    #                 thickness=3,
    #                 lineType=cv2.LINE_4,
    #                 shift=0)
    #         cv2.line(blank,
    #                 pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
    #                 pt2=(int(list_param[num][0 * 2 + 2]), int(list_param[num][0 * 2 + 3])),
    #                 color=(0, 0, 0),
    #                 thickness=3,
    #                 lineType=cv2.LINE_4,
    #                 shift=0)
    
    # print(color_list)
    # color_list = [[0, 4, [53, 19], [48, 145],[49, 308], [39, 203], [39, 100], [51, 19]], [1, 10, [40, 14], [60, 147],[81, 307], [28, 224], [19, 107], [36, 14]], [10, 7, [63, 454], [31, 26], [41, 193], [88, 395], [50, 186], [47, 127], [32, 26]], [11, 6, [40, 9], [74, 185], [132, 528], [145, 592], [94, 435], [47, 290], [29, 164], [36, 31]], [12, 9, [57, 416], [46, 26], [51, 165], [51, 368], [27, 237], [26, 121], [45, 28]], [2, 12, [78, 208], [100, 12], [82, 171], [85, 168], [104, 120], [102, 31]], [3, 3, [74, 23], [54, 172], [36, 496], [54, 532], [54, 532], [99, 250], [102, 121], [75, 23]], [4, 1, [106, 665], [50, 7], [80, 259], [89, 580], [36, 381], [24, 174], [47, 7]], [5, 5, [51, 501], [45, 41], [46, 188], [43, 407], [26, 265], [28, 133], [44, 43]], [6, 2, [49, 340], [40, 11], [44, 130], [44, 291], [20, 200], [19, 101], [35, 26]], [7, 0, [75, 369], [28, 9], [53, 167], [29, 266], [15, 36], [27, 9]], [8, 8, [47, 311], [21, 15], [33, 134], [42, 282], [12, 123], [15, 87], [21, 15]], [9, 11, [43, 444], [65, 21], [56, 185], [51, 407], [71, 266], [80, 117], [68, 21]]]

    # for l in range(len(color_list)):
    #     if color_list[l][1] == num:
    #         list_c = []
    #         for k in range(2, len(color_list[l])):
    #             list_c.append(color_list[l][k])
    #         # print(list_c)
    #         pts = np.array(list_c, np.int32)
    #         # pts = pts.reshape((-1, 1, 2))
    #         cv2.fillPoly(img, [pts], (100, 100, 0))
    
        
    for l in range(count):
        if l != num_point - 1:
            cv2.line(img,
                    pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
                    pt2=(int(list_param[num][l * 2 + 4]), int(list_param[num][l * 2 + 5])),
                    color=(0, 0, 0),
                    thickness=3,
                    lineType=cv2.LINE_4,
                    shift=0)
            cv2.line(blank,
                    pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
                    pt2=(int(list_param[num][l * 2 + 4]), int(list_param[num][l * 2 + 5])),
                    color=(0, 0, 0),
                    thickness=3,
                    lineType=cv2.LINE_4,
                    shift=0)
        else:
            cv2.line(img,
                    pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
                    pt2=(int(list_param[num][0 * 2 + 2]), int(list_param[num][0 * 2 + 3])),
                    color=(0, 0, 0),
                    thickness=3,
                    lineType=cv2.LINE_4,
                    shift=0)
            cv2.line(blank,
                    pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
                    pt2=(int(list_param[num][0 * 2 + 2]), int(list_param[num][0 * 2 + 3])),
                    color=(0, 0, 0),
                    thickness=3,
                    lineType=cv2.LINE_4,
                    shift=0)
    




    
    cv2.imwrite('rean/a' + file_name + '_c.jpg', img)
    # print(file_name)
    cv2.imwrite('rean/ablank_' + file_name + '_c.jpg', blank)