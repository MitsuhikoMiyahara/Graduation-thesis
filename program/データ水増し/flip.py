import numpy as np
import glob, cv2, os


dir_Path = "original/"
file_list = glob.glob(os.path.join(dir_Path, "*.jpg"))

for i, imgPath in enumerate(file_list):

    # 画像を読み込む
    img = cv2.imread(imgPath)  # 画像のパスを指定
    file_name = os.path.basename(imgPath).split('.', 1)[0]


    # 画像を水平方向（axis=1）に反転する
    flipped_img = np.flip(img, axis=1)

    # 反転した画像を保存
    cv2.imwrite('original/flipped_' + file_name  + '.jpg', flipped_img)