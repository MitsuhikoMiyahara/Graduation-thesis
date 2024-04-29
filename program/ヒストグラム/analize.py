import glob, cv2, os

# 各実験ごとの誤差の合計
list_sum = []
# ファイルから取得した値の格納場所
list_txt = []
# 核実験ごとの誤差の数
list_pieces = []
# 数値の合計
num_sum = 0.0
# 誤差数の合計
num_pieces = 0

dir_Path = "result/"
file_list = glob.glob(os.path.join(dir_Path, "*.txt"))
for i, txtpath in enumerate(file_list):
    # print(i, txtpath)
    with open(txtpath) as f:
        l_strip1 = [s.strip() for s in f.readlines()]
        for j in range(len(l_strip1)):
            if j != 0 and j != 1:
                list_txt.append(l_strip1[j])
    # print(list_txt)
    for k in range(len(list_txt)):
        list_num = list_txt[k].split(",")
        list_num.pop(0)
        list_num.pop(len(list_num) - 1)
        # print(list_num)
        # num = 0.0
        for l in range(len(list_num)):
            num_sum += float(list_num[l])
            num_pieces += 1
            # num += float(list_num[l])
        # print(num_sum)
        # print(num)
        # print(num_pieces)
    list_sum.append(num_sum)
    list_pieces.append(num_pieces)

    #初期化
    list_txt = []
    num_sum = 0.0
print(list_sum, list_pieces)