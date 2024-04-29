import matplotlib.pyplot as plt

f = open('histgram_m', 'r')

datalist = f.readlines()
count = len(datalist)

list_param = []

for i in range(count):
    # print(datalist[i])
    datalist[i] = datalist[i].replace('\n', '')
    list_param.append(float(datalist[i]))
print(list_param)
# print(len(list_param))
# plt.xlim(0,50.0)    
plt.hist(list_param, bins = 100, range=(0, 20))
# plt.hist(list_param, bins = 100)
plt.show()