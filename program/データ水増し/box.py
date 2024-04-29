import json
from matplotlib import pyplot

json_file = open('test_box_annotation.json', 'r')
json_object = json.load(json_file)


# print(json_object.keys())
# print(len(json_object['images']))

list_name = []

for i in range(len(json_object['images'])):
    # print(i)
    list_name.append(json_object['images'][i]['file_name'])

# print(list_name)
print(len(list_name))
    
    
list_data = []

for i in range(len(json_object['annotations'])):
    list_data.append(json_object['annotations'][i]['bbox'])
# print(list_data)
print(len(list_data))

list_1 = []
list_box = []

for i in range(len(list_data)):
    list_1.append(list_name[i])
    list_1.append(list_data[i])
    # print(list_1)
    list_box.append(list_1)
    list_1 = []

print(list_box)

txtname = 'box_ans_a.txt'
f = open(txtname, 'a')
for i in range(len(list_box)):
    f.write(str(list_box[i][0]))
    f.write(',')
    f.write(str(list_box[i][1][0]))
    f.write(',')
    f.write(str(list_box[i][1][1]))
    f.write(',')
    f.write(str(list_box[i][1][2]))
    f.write(',')
    f.write(str(list_box[i][1][3]))
    f.write('\n')
f.close()