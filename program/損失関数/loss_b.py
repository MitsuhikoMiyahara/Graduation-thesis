import json
from matplotlib import pyplot

json_file = open('test_key_ans.json', 'r')
json_object = json.load(json_file)

# print(json_object.keys())

list_name = []

for i in range(len(json_object['images'])):
    list_name.append(json_object['images'][i]['file_name'])
# print(list_name)
# print(len(list_name))

list_keypoints = []

for i in range(len(json_object['annotations'])):
    list_keypoints.append(json_object['annotations'][i]['keypoints'])
print(list_keypoints)
print(len(list_keypoints))

list_ans = []
ans = []

for i in range(len(list_keypoints)):
    ans.append(list_name[i])
    for j in range(len(list_keypoints[i])):
        if j % 3 == 0 or j % 3 == 1:
            ans.append(list_name[i][j])