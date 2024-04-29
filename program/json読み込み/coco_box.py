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

box_keypoints = []

for i in range(len(list_keypoints)):
    box = list_keypoints[i]
    # print(box)
    box_keypoints.append(box)

# print(box_keypoints[0])

# boxのjsonファイルを書き込み形式で読み込む
box_file = open('box_annotation.json', 'r')
box_object = json.load(box_file)

# keyname取得
box_keys = list(box_object.keys())
# print(box_keys)

# annotation情報取得
box_annotation = box_object["annotations"]
# print(box_annotation)
# print(len(box_annotation))

# keypoint座標取得
box_keypoints = []
for i in range(len(box_annotation)):
    # print(i, box_annotation[i]['keypoints'])
    box_keypoints.append(box_annotation[i]['keypoints'])
    box_annotation[i]['keypoints'] = list_keypoints[i]
    # print(dict_annotation[i]['keypoints'])
    # box_keypoints.append(box_annotation[i]['keypoints'])
# print(box_keypoints)
# print(len(box_keypoints))

# キーポイントの比較
for i in range(len(box_keypoints)):
    print(box_keypoints[i], list_keypoints[i])

# jsonファイルへの書き込み
output_json = open('a.json', 'w')
json.dump(box_object, output_json)
