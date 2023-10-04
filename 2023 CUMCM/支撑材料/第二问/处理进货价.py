import pandas as pd

# 读取Excel数据到DataFrame
df = pd.read_excel("进货价.xlsx")

# 按日期和单品分组，并计算批发价格的均值
result = df.groupby(["日期", "单品"])["批发价格(元/千克)"].mean()

# 按日期和分类名称分组，并计算批发价格的均值
result = df.groupby(["日期", "分类名称"])["批发价格(元/千克)"].mean().unstack()

# 将结果保存到新的Excel文件
result.to_excel("品类的进货价.xlsx", index=True)

# 将结果转换为DataFrame格式
result_df = result.reset_index()
result_df.to_excel("处理后的进货价.xlsx", index=True)

