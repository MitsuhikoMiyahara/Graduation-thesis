# yoloの精度確認

import glob, cv2, os
import numpy as np

# まずは正解を求める

# 名前と左上の座標と右下の座標を入れる(要素は5つ)
list_ans = []

f = open('box_ans_a.txt', 'r')
list_ans = f.readlines()

for i in range(len(list_ans)):
    list_ans[i] = list_ans[i].replace('\n', '')
    list_ans[i] = list_ans[i].split(',')
    # print(i)
# print(list_ans)
# print(len(list_ans))
# print(len(list_ans[0]))
for i in range(len(list_ans)):
    list_ans[i][0] = list_ans[i][0].split('.', 1)[0]
    list_ans[i][1] = int(list_ans[i][1])
    list_ans[i][2] = int(list_ans[i][2])
    list_ans[i][3] = int(list_ans[i][3]) + list_ans[i][1]
    list_ans[i][4] = int(list_ans[i][4]) + list_ans[i][2]
    # print(i)
# print(list_ans)
# print(len(list_ans))
f.close()



# 検出座標(要素は5つ)
list_pre = []

dir_Path = "exp24/labels/"
file_list = glob.glob(os.path.join(dir_Path, "*.txt"))
for i, Path in enumerate(file_list):
    file_name = os.path.basename(Path).split('.', 1)[0]
    # file_name = os.path.basename(Path)
    f = open(Path, 'r')
    datalist = f.readlines()
    # print(datalist)
    data = datalist[0]
    # print(data)
    data = data.split()
    data.pop(0)
    data.insert(0, file_name)
    # print(data)
    list_pre.append(data)
# print(list_pre)

# 画像の幅，高さを取得
list_image = []
list_i = []

dir_Path = "exp24"
file_list = glob.glob(os.path.join(dir_Path, "*.jpg"))
for i, Path in enumerate(file_list):
    file_name = os.path.basename(Path).split('.', 1)[0]
    img = cv2.imread(Path)
    shape = img.shape
    height = shape[0]
    width = shape[1]
    # print(height, width)
    list_i.append(file_name)
    list_i.append(width)
    list_i.append(height)
    list_image.append(list_i)
    list_i = []
# print(list_image)
# print(len(list_image))

for i in range(len(list_pre)):
    for j in range(len(list_image)):
        if list_pre[i][0] == list_image[j][0]:
            list_pre[i][1] = float(list_pre[i][1]) * list_image[j][1]
            list_pre[i][2] = float(list_pre[i][2]) * list_image[j][2]
            list_pre[i][3] = float(list_pre[i][3]) * list_image[j][1]
            list_pre[i][4] = float(list_pre[i][4]) * list_image[j][2]
# print(list_pre)


# 左上，右下に合わせる
for i in range(len(list_pre)):
    w = list_pre[i][3]
    h = list_pre[i][4]
    center_x = list_pre[i][1]
    center_y = list_pre[i][2]
    list_pre[i][1] = round(center_x - w / 2)
    list_pre[i][2] = round(center_y - h / 2)
    list_pre[i][3] = round(center_x + w / 2)
    list_pre[i][4] = round(center_y + h / 2)
# print(list_pre)
# print(len(list_pre))

# list_ansに正解座標，list_preに検出座標が入っている
# 精度確認

list_result = []
result_a = []
result_b = []

num = 0

for i in range(len(list_ans)):
    # print(list_ans[i][0])
    for j in range(len(list_pre)):
        # print(list_ans[i][0])
        if list_ans[i][0] == list_pre[j][0]:
            # print(i, list_ans[i][0], list_pre[j][0])
            if list_ans[i][1] >= list_pre[j][1] and list_ans[i][2] >= list_pre[j][2]:
                if list_ans[i][3] <= list_pre[j][3] and list_ans[i][4] <= list_pre[j][4]:
                    result_a.append(list_ans[i][0])
                else:
                    print(list_ans[i][0], list_ans[i][3], list_pre[j][3],list_ans[i][4], list_pre[j][4], "a")
                    result_b.append(list_ans[i])
            else:
                print(list_ans[i][0], list_ans[i][1], list_pre[j][1],list_ans[i][2], list_pre[j][2], "b")
                result_b.append(list_ans[i])
list_result.append(result_a)
list_result.append(result_b)
# print(list_result)
print(len(result_a))
print(result_b)
print(num)

# 正しく検出できなかった画像を元画像から切り取りなおす
dir_Path = "original/"
file_list = glob.glob(os.path.join(dir_Path, "*.jpg"))
for i, path in enumerate(file_list):
    img = cv2.imread(path)
    img1 = cv2.imread(path)

    file_name = os.path.basename(path).split('.', 1)[0]
    for j in range(len(result_b)):
        if file_name == result_b[j][0]:
            print(file_name)
            shape = img.shape
            height = shape[0]
            hei = round(height / 50)
            a1 = result_b[j][2] - hei
            a2 = result_b[j][4] + hei
            a3 = result_b[j][1] - hei
            a4 =result_b[j][3] + hei
            if a1 < 0:
                a1 = 0
            if a3 < 0:
                a1 = 0
            img = img[a1 : a2, a3 : a4]
            cv2.imwrite(file_name + "_cut.jpg", img)
            cv2.circle(img1,
            center=(int(result_b[j][1]), int(result_b[j][2])),
            radius=5,
            color=(255, 0, 0),
            thickness=-1,
            lineType=cv2.LINE_4,
            shift=0)
            cv2.circle(img1,
            center=(int(result_b[j][3]), int(result_b[j][4])),
            radius=5,
            color=(255, 0, 0),
            thickness=-1,
            lineType=cv2.LINE_4,
            shift=0)
            cv2.imwrite(file_name + "_point.jpg", img1)