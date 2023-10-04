import pandas as pd

# 读取Excel文件
df = pd.read_excel('附2按秒记录删去退货补充品名的完整数据.xlsx')

# 将销售日期转换为日期类型
df['销售日期'] = pd.to_datetime(df['销售日期'])

# 按日期、单品编码和品类分组，对销量进行求和，保留单价和品类
df_grouped = df.groupby(['销售日期', '单品编码', '品类']).agg({'销量(千克)': 'sum', '销售单价(元/千克)': 'first'}).reset_index()

# 将累加后的数据写回Excel文件
df_grouped.to_excel('完整数据2.xlsx', index=False)
