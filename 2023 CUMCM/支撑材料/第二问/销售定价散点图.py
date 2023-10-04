import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

pricing_data = pd.read_excel('weighted_prices.xlsx')
sales_data = pd.read_excel('总销售.xlsx')

# 茄类散点图
pricing_tomato = pricing_data['水生根茎类']
sales_tomato = sales_data['水生根茎类']
plt.scatter(pricing_tomato, sales_tomato, s=5)
plt.xlabel('定价')
plt.ylabel('销量')
plt.title('')
plt.show()

# 辣椒类散点图
pricing_pepper = pricing_data['辣椒类']
sales_pepper = sales_data['辣椒类']
plt.scatter(pricing_pepper, sales_pepper)
plt.xlabel('定价')
plt.ylabel('销量')
plt.title('辣椒类')
plt.show()

# 花叶类散点图
pricing_leafy = pricing_data['花叶类']
sales_leafy = sales_data['花叶类']
plt.scatter(pricing_leafy, sales_leafy)
plt.xlabel('定价')
plt.ylabel('销量')
plt.title('花叶类')
plt.show()

# 花菜类散点图
pricing_cauliflower = pricing_data['花菜类']
sales_cauliflower = sales_data['花菜类']
plt.scatter(pricing_cauliflower, sales_cauliflower)
plt.xlabel('定价')
plt.ylabel('销量')
plt.title('花菜类')
plt.show()
