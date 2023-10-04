import pandas as pd

# 读取单品销售数据
product_sales = pd.read_excel('完整数据2.xlsx')
# 读取品类总销售量数据
category_sales = pd.read_excel('总销售.xlsx')

# 创建一个空的DataFrame用于保存每天每个品类的加权平均定价
weighted_prices = pd.DataFrame(columns=category_sales.columns[1:])
# 遍历每一天的销售数据
for date in category_sales['销售日期']:
    # 获取该天的品类销售量数据
    daily_sales = category_sales[category_sales['销售日期'] == date].iloc[:, 1:]
    # 获取该天的单品销售数据
    daily_products = product_sales[product_sales['销售日期'] == date]
    # 遍历每个品类
    for category in daily_sales.columns:
        # 获取该品类的销量
        category_sales_volume = daily_sales[category].values[0]
        # 获取该品类的单品数据
        category_products = daily_products[daily_products['品类'] == category]
        # 计算该品类单品的加权平均定价
        weighted_price = sum(
            category_products['销售单价(元/千克)'] * (category_products['销量(千克)'] / category_sales_volume))
        # 添加该品类的加权平均定价到DataFrame中
        weighted_prices.loc[date, category] = weighted_price

# 将结果保存到Excel文档中
weighted_prices.to_excel('weighted_prices.xlsx', index_label='销售日期')
