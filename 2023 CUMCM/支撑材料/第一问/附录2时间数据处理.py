import pandas as pd
import re

data = pd.read_excel("附件2.xlsx")

# 重复行检查
duplicate_rows = data[data.duplicated()]
if duplicate_rows.shape[0] > 0:
    print("附件2中存在重复的行：")
    print(duplicate_rows)
else:
    print("附件2中没有重复的行。")

# 时间异常值检查：正则表达式
pattern = r'^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9](\.\d{1,3})?)$'
invalid_times = data[~data['扫码销售时间'].astype(str).str.match(pattern)]
if invalid_times.shape[0] > 0:
    print("附件2中存在异常时间数据：")
    print(invalid_times)
else:
    print("附件2中没有异常时间数据。")

# 给"附件2预处理.xlsx"加上单品名与分类名
df1 = pd.read_excel('附件1.xlsx')
df2 = pd.read_excel('附件2预处理.xlsx')
# 创建字典
mapping_dict1 = dict(zip(df1['单品编码'], df1['单品名称']))
mapping_dict2 = dict(zip(df1['单品编码'], df1['分类名称']))
# 字典映射
df2['单品名称'] = df2['单品编码'].map(mapping_dict1)
df2['分类名称'] = df2['单品编码'].map(mapping_dict2)
df2.to_excel('按每年的月份分类.xlsx', index=False)
