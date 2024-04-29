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

# print(list_keypoints)
# print(len(list_keypoints))
# print(list_keypoints[0])

boom_keypoints = []

for i in range(len(list_keypoints)):
    boom = list_keypoints[i]
    # print(boom)
    del boom[:6]
    del boom[6:]
    # print(boom)
    boom_keypoints.append(boom)

print(boom_keypoints[0])

# boomのjsonファイルを書き込み形式で読み込む
boom_file = open('ans_boom_annotation.json', 'r')
boom_object = json.load(boom_file)

# keyname取得
boom_keys = list(boom_object.keys())
# print(boom_keys)

# annotation情報取得
boom_annotation = boom_object["annotations"]
# print(boom_annotation)
# print(len(boom_annotation))

# keypoint座標取得
boom_keypoints = []
for i in range(len(boom_annotation)):
    boom_keypoints.append(boom_annotation[i]['keypoints'])
    boom_annotation[i]['keypoints'] = list_keypoints[i]
    # print(dict_annotation[i]['keypoints'])
    # boom_keypoints.append(boom_annotation[i]['keypoints'])
# print(boom_keypoints)
# print(len(boom_keypoints))

# キーポイントの比較
for i in range(len(boom_keypoints)):
    print(boom_keypoints[i], list_keypoints[i])

# キーポイントの比較
# for i in range(len(boom_keypoints)):
#     print(boom_keypoints[i], list_keypoints[i])

# jsonファイルへの書き込み
output_json = open('ans_boom.json', 'w')
json.dump(boom_object, output_json)
