import json
from matplotlib import pyplot

json_file = open('3sepa/metrics_reach.json', 'r')
json_object = json.load(json_file)

list_data = []


for i in range(len(json_object)):
    list_data.append(json_object[i]['loss_keypoint'])
print(list_data)
print(len(list_data))

pyplot.plot(range(len(list_data)), list_data)
pyplot.show()
