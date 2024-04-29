import glob, cv2, os
import numpy as np

imgPath = "scoretest/test8.jpg"

img = cv2.imread(imgPath)
file_name = os.path.basename(imgPath).split('.', 1)[0]
shape = img.shape
height = shape[0]
width = shape[1]
blank = np.zeros((height, width, 3))
blank += 255

# mast_top

list_param = [25, 22, 34, 132, 51, 381, 68, 404, 43, 290, 24, 190, 15, 94, 22, 26]


# 塗りつぶす範囲[testnumber,書かれる順番,交点]
color_list_1 = []
color_list = []

for i, imgPath in enumerate(file_list):
    # print(imgPath[14], imgPath[15])

    num = imgPath[14]

    if imgPath[15] != '.':
        num = num + imgPath[15]
    
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
# print(color_list)

                    
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

print(alllist)
print(len(alllist))
print(len(alllist[0]))

print(color_list)


count = 8
for l in range(count):
    if l == 0 or  l == 1 or l == 2:
        cv2.circle(img,
                center=(int(list_param[l * 2]), int(list_param[l * 2 + 1])),
                radius=5,
                color=(255, 0, 0),
                thickness=-1,
                lineType=cv2.LINE_4,
                shift=0)
            
        cv2.circle(blank,
                center=(int(list_param[l * 2]), int(list_param[l * 2 + 1])),
                radius=5,
                color=(255, 0, 0),
                thickness=-1,
                lineType=cv2.LINE_4,
                shift=0)
    else:
        cv2.circle(img,
                center=(int(list_param[l * 2]), int(list_param[l * 2 + 1])),
                radius=5,
                color=(0, 255, 0),
                thickness=-1,
                lineType=cv2.LINE_4,
                shift=0)
            
        cv2.circle(blank,
                center=(int(list_param[l * 2]), int(list_param[l * 2 + 1])),
                radius=5,
                color=(0, 255, 0),
                thickness=-1,
                lineType=cv2.LINE_4,
                shift=0)
    
# for l in range(count):
#     if l != count - 1:
#         cv2.line(img,
#                 pt1=(int(list_param[l * 2]), int(list_param[l * 2 + 1])),
#                 pt2=(int(list_param[l * 2 + 2]), int(list_param[l * 2 + 3])),
#                 color=(0, 0, 0),
#                 thickness=3,
#                 lineType=cv2.LINE_4,
#                 shift=0)
#         cv2.line(blank,
#                 pt1=(int(list_param[l * 2]), int(list_param[l * 2 + 1])),
#                 pt2=(int(list_param[l * 2 + 2]), int(list_param[l * 2 + 3])),
#                 color=(0, 0, 0),
#                 thickness=3,
#                 lineType=cv2.LINE_4,
#                 shift=0)
#     else:
#         cv2.line(img,
#                 pt1=(int(list_param[l * 2]), int(list_param[l * 2 + 1])),
#                 pt2=(int(list_param[0 * 2]), int(list_param[0 * 2 + 1])),
#                 color=(0, 0, 0),
#                 thickness=3,
#                 lineType=cv2.LINE_4,
#                 shift=0)
#         cv2.line(blank,
#                 pt1=(int(list_param[l * 2]), int(list_param[l * 2 + 1])),
#                 pt2=(int(list_param[0 * 2]), int(list_param[0 * 2 + 1])),
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




    
cv2.imwrite('r/' + file_name + '_c.jpg', img)
# print(file_name)
cv2.imwrite('r/blank_' + file_name + '_c.jpg', blank)