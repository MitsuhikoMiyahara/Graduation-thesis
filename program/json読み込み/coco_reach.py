# jsonファイルからキーポイントの座標を取得し、ほかのjsonファイルに書き込むことを目的とする
import json

# 教師ファイルを読む専用で開く
json_file = open('ans_annotation.json', 'r')
json_object = json.load(json_file)

# keyname取得
list_keys = list(json_object.keys())
# print(list_keys)

# annotation情報取得
dict_annotation = json_object["annotations"]
# print(dict_annotation)
# print(len(dict_annotation))

# keypoint座標取得
list_keypoints = []
for i in range(len(dict_annotation)):
    # print(dict_annotation[i]['keypoints'])
    list_keypoints.append(dict_annotation[i]['keypoints'])

# # print(list_keypoints)
# print(len(list_keypoints))
# print(list_keypoints[0])

reach_keypoints = []

for i in range(len(list_keypoints)):
    reach = list_keypoints[i]
    # print(reach)
    del reach[:9]
    # print(reach)
    reach_keypoints.append(reach)


reach_0 = []
reach_1 = []
reach_2 = [] 
reach_value = []
all_reach = []

# boom➡reachの順番を逆にしたい
# 別々にリスト化
for i in range(len(reach_keypoints)):
    for j in range(len(reach_keypoints[i])):
        if j % 3 == 0:
            reach_0.append(reach_keypoints[i][j])
        elif j % 3 == 1:
            reach_1.append(reach_keypoints[i][j])
        else:
            reach_2.append(reach_keypoints[i][j])
    reach_value.append(reach_0)
    reach_value.append(reach_1)
    reach_value.append(reach_2)
    reach_0 = []
    reach_1 = []
    reach_2 = []
    all_reach.append(reach_value)
    reach_value = []

# print(all_reach)
# print(len(all_reach))

# print(reach_keypoints[0])

num_0 = 0
num_1 = 0
num_2 = 0

# 順番変更後のリスト
for i in range(len(reach_keypoints)):
    for j in range(len(reach_keypoints[i])):
        if j % 3 == 0:
            reach_keypoints[i][j] = all_reach[i][0][4 - num_0]
            num_0 += 1
        elif j % 3 == 1:
            reach_keypoints[i][j] = all_reach[i][1][4 - num_1]
            num_1 += 1
        else:
            reach_keypoints[i][j] = all_reach[i][2][4 - num_2]
            num_2 += 2
        
    num_0 = 0
    num_1 = 0
    num_2 = 0


# print(reach_keypoints[0])

# reachのjsonファイルを書き込み形式で読み込む
reach_file = open('reach_an.json', 'r')
reach_object = json.load(reach_file)

# keyname取得
reach_keys = list(reach_object.keys())
# print(reach_keys)

# annotation情報取得
reach_annotation = reach_object["annotations"]
# print(reach_annotation)
# print(len(reach_annotation))

# keypoint座標取得
reach_keypoints = []
for i in range(len(reach_annotation)):
    # print(i, reach_annotation[i]['keypoints'])
    reach_keypoints.append(reach_annotation[i]['keypoints'])
    reach_annotation[i]['keypoints'] = list_keypoints[i]
    # print(dict_annotation[i]['keypoints'])
    # reach_keypoints.append(reach_annotation[i]['keypoints'])
# print(reach_keypoints)
# print(len(reach_keypoints))

# キーポイントの比較
for i in range(len(reach_keypoints)):
    print(reach_keypoints[i], list_keypoints[i])

# jsonファイルへの書き込み
output_json = open('reach.json', 'w')
json.dump(reach_object, output_json)
