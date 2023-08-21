import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 数据
cbts_scores = [0, 5]
cbts_costs = [200, 810.667*5+200]

epds_scores = [0, 5]
epds_costs = [500, 695*5+500]

hads_scores = [0, 5]
hads_costs = [300, 12500]

# 绘制图形
plt.plot(cbts_scores, cbts_costs, label='CBTS')
plt.plot(epds_scores, epds_costs, label='EPDS')
plt.plot(hads_scores, hads_costs, label='HADS')

# 添加标题和标签

plt.xlabel('得分')
plt.ylabel('治疗费用')

# 添加图例
plt.legend()

# 设置横坐标范围
plt.xlim(0, 5)

# 设置纵坐标范围
plt.ylim(0, 13000)

# 显示网格线
plt.grid(True)

# 显示图形
plt.show()