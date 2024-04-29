import numpy as np
import matplotlib.pyplot as plt

# 平均 50, 標準偏差 10 の正規乱数を1,000件生成
x = np.random.normal(50, 10, 10)
print(x)
 
# ヒストグラムを出力
plt.hist(x)
plt.savefig("images/plt.png")
plt.show()