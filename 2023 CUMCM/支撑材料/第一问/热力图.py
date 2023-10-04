import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 从Excel读取数据
data_frame1 = pd.read_excel('品类热力图.xlsx')
# 提取矩阵数据
matrix_data = data_frame1.values
# 创建热力图
sns.heatmap(matrix_data, annot=True, cmap='RdBu')
# 展示热力图
plt.show()

# 从Excel读取数据
data_frame2 = pd.read_excel('聚类的相关系数矩阵.xlsx')
# 提取矩阵数据
matrix_data = data_frame2.values
# 创建热力图
sns.heatmap(matrix_data, annot=False, cmap='RdBu')
#plt.title("18类单品的斯皮尔曼相关系数热力图")
# 展示热力图
plt.show()