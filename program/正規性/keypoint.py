import json
from matplotlib import pyplot
import glob, cv2, os

json_file = open('test_key_ans.json', 'r')
json_object = json.load(json_file)

# print(json_object.keys())

list_name = []

for i in range(len(json_object['images'])):
    file_name = json_object['images'][i]['file_name'].split('.', 1)[0]
    list_name.append(file_name)
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
            ans.append(list_keypoints[i][j])
    list_ans.append(ans)
    ans = []
print(list_ans)
print(len(list_ans))