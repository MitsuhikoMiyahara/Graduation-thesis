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

mast_keypoints = []

for i in range(len(list_keypoints)):
    mast = list_keypoints[i]
    # print(mast)
    del mast[9:]
    # print(mast)
    mast_keypoints.append(mast)

# print(mast_keypoints[0])

# mastのjsonファイルを書き込み形式で読み込む
mast_file = open('mast_annotation.json', 'r')
mast_object = json.load(mast_file)

# keyname取得
mast_keys = list(mast_object.keys())
# print(mast_keys)

# annotation情報取得
mast_annotation = mast_object["annotations"]
# print(mast_annotation)
# print(len(mast_annotation))

# keypoint座標取得
mast_keypoints = []
for i in range(len(mast_annotation)):
    # print(i, mast_annotation[i]['keypoints'])
    mast_keypoints.append(mast_annotation[i]['keypoints'])
    mast_annotation[i]['keypoints'] = list_keypoints[i]
    # print(dict_annotation[i]['keypoints'])
    # mast_keypoints.append(mast_annotation[i]['keypoints'])
# print(mast_keypoints)
# print(len(mast_keypoints))

# キーポイントの比較
for i in range(len(mast_keypoints)):
    print(mast_keypoints[i], list_keypoints[i])

# jsonファイルへの書き込み
output_json = open('a.json', 'w')
json.dump(mast_object, output_json)
