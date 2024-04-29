import glob, cv2, os
import numpy as np

# テストデータの数
num_data = 13
# キーポイントの数
num_point = 8

f = open('scoretest_noval_result', 'r')
datalist = f.readlines()
count = len(datalist)
# print(count)

list_param = []
param = []

for i in range(count):
    data = datalist[i]
    # print(data)
    split_data = data.split()
    if len(split_data) == 1:
        # print(split_data[0][4])
        number = split_data[0][4]
        if split_data[0][5] != '.':
            number = number + split_data[0][5]
        param.append(number)
    if len(split_data) > 1:
        param.append(split_data[2])
    if len(param) == 2 + 2 * num_point:
        list_param.append(param)
        param = []
if len(list_param) == num_data:
    print("OK")
else:
    print("FALSE")
f.close()

# print(list_param)


dir_Path = "scoretest/"
file_list = glob.glob(os.path.join(dir_Path, "*.jpg"))
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
    for l in range(count):
        if l == 0 or  l == 1 or l == 2:
            cv2.circle(img,
                    center=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
                    radius=5,
                    color=(255, 0, 0),
                    thickness=-1,
                    lineType=cv2.LINE_4,
                    shift=0)
            
            cv2.circle(blank,
                    center=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
                    radius=5,
                    color=(255, 0, 0),
                    thickness=-1,
                    lineType=cv2.LINE_4,
                    shift=0)
        else:
            cv2.circle(img,
                    center=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
                    radius=5,
                    color=(0, 255, 0),
                    thickness=-1,
                    lineType=cv2.LINE_4,
                    shift=0)
            
            cv2.circle(blank,
                    center=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
                    radius=5,
                    color=(0, 255, 0),
                    thickness=-1,
                    lineType=cv2.LINE_4,
                    shift=0)
    
    for l in range(count):
        if l != num_point - 1:
            # cv2.line(img,
            #         pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
            #         pt2=(int(list_param[num][l * 2 + 4]), int(list_param[num][l * 2 + 5])),
            #         color=(0, 0, 0),
            #         thickness=3,
            #         lineType=cv2.LINE_4,
            #         shift=0)
            cv2.line(blank,
                    pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
                    pt2=(int(list_param[num][l * 2 + 4]), int(list_param[num][l * 2 + 5])),
                    color=(0, 0, 0),
                    thickness=3,
                    lineType=cv2.LINE_4,
                    shift=0)
        else:
            # cv2.line(img,
            #         pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
            #         pt2=(int(list_param[num][0 * 2 + 2]), int(list_param[num][0 * 2 + 3])),
            #         color=(0, 0, 0),
            #         thickness=3,
            #         lineType=cv2.LINE_4,
            #         shift=0)
            cv2.line(blank,
                    pt1=(int(list_param[num][l * 2 + 2]), int(list_param[num][l * 2 + 3])),
                    pt2=(int(list_param[num][0 * 2 + 2]), int(list_param[num][0 * 2 + 3])),
                    color=(0, 0, 0),
                    thickness=3,
                    lineType=cv2.LINE_4,
                    shift=0)

    
    cv2.imwrite('a/' + file_name + '.jpg', img)
    cv2.imwrite('a/blank_' + file_name + '.jpg', blank)