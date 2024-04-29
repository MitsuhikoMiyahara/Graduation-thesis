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
# print(list_ans)
# print(len(list_ans))
# print(len(list_ans[0]))
for i in range(len(list_ans)):
    list_ans[i][0] = list_ans[i][0].split('.', 1)[0]
    list_ans[i][1] = int(list_ans[i][1])
    list_ans[i][2] = int(list_ans[i][2])
    list_ans[i][3] = int(list_ans[i][3]) + list_ans[i][1]
    list_ans[i][4] = int(list_ans[i][4]) + list_ans[i][2]
# print(list_ans)
f.close()
dir_Path = "original/"
file_list = glob.glob(os.path.join(dir_Path, "*.jpg"))
for i, path in enumerate(file_list):
    img = cv2.imread(path)
    file_name = os.path.basename(path).split('.', 1)[0]
    for j in range(len(list_ans)):
        if file_name == list_ans[j][0]:
            cv2.circle(img,
                center=(int(list_ans[j][1]), int(list_ans[j][2])),
                radius=5,
                color=(255, 0, 0),
                thickness=-1,
                lineType=cv2.LINE_4,
                shift=0)
            cv2.circle(img,
                center=(int(list_ans[j][3]), int(list_ans[j][4])),
                radius=5,
                color=(255, 0, 0),
                thickness=-1,
                lineType=cv2.LINE_4,
                shift=0)
            if file_name == 'flipped_test1_-5':

                print(int(list_ans[j][1]), int(list_ans[j][2]))
    cv2.imwrite(file_name + '.jpg', img)
# print(list_ans)



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

dir_Path = "original/"
file_list = glob.glob(os.path.join(dir_Path, "*.jpg"))
for i, path in enumerate(file_list):
    img = cv2.imread(path)
    file_name = os.path.basename(path).split('.', 1)[0]
    for j in range(len(list_pre)):
        if file_name == list_pre[j][0]:
            cv2.circle(img,
                center=(int(list_pre[i][1]), int(list_pre[i][2])),
                radius=5,
                color=(255, 0, 0),
                thickness=-1,
                lineType=cv2.LINE_4,
                shift=0)
            cv2.circle(img,
                center=(int(list_pre[i][3]), int(list_pre[i][4])),
                radius=5,
                color=(255, 0, 0),
                thickness=-1,
                lineType=cv2.LINE_4,
                shift=0)
    cv2.imwrite(file_name + '_p.jpg', img)

# list_ansに正解座標，list_preに検出座標が入っている
# 精度確認

list_result = []
result_a = []
result_b = []

for i in range(len(list_ans)):
    # print(list_ans[i][0])
    for j in range(len(list_pre)):
        # print(list_ans[i][0])
        if list_ans[i][0] == list_pre[j][0]:
            if list_ans[i][1] >= list_pre[j][1] and list_ans[i][2] >= list_pre[j][2]:
                if list_ans[i][3] <= list_pre[j][3] and list_ans[i][4] <= list_pre[j][4]:
                    result_a.append(list_ans[i][0])
                else:
                    # print(list_ans[i][0], list_ans[i][3], list_pre[j][3],list_ans[i][4], list_pre[j][4])
                    result_b.append(list_ans[i][0])
            else:
                # print(list_ans[i][3], list_pre[j][3],list_ans[i][4], list_pre[j][4])
                result_b.append(list_ans[i][0])
list_result.append(result_a)
list_result.append(result_b)
print(list_result)
print(len(result_a))
print(len(result_b))