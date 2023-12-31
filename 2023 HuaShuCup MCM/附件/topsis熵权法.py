import numpy as np
import pandas as pd
import openpyxl

# 指标属性同向化
def normalize_direction(matrix, reverse_cols):
    normalized_matrix = np.copy(matrix)
    for col in reverse_cols:
        normalized_matrix[:, col] = np.max(normalized_matrix[:, col]) - normalized_matrix[:, col]
    return normalized_matrix

def entropy_weight(x):
    # 处理数组，将0替换为一个较小的非零值
    x_processed = np.where(x == 0, 1e-10, x)
    # 计算每个指标的熵值
    m, n = x.shape
    e = np.zeros((1, n))
    for j in range(n):
        p = x_processed[:, j] / x_processed[:, j].sum()
        e[0][j] = - (p * np.log(p)).sum()
    #print(e)
    # 计算每个指标的权重
    w = np.zeros((1, n))
    for j in range(n):
        w[0][j] = (1 - e[0][j]) / (np.sum(1 - e))
    return w

def topsis(x, w):
    # 将x归一化处理
    m, n = x.shape
    x_norm = np.zeros((m, n))
    for j in range(n):
        x_norm[:, j] = x[:, j] / np.sqrt((x[:, j]**2).sum())
    # 计算加权后的矩阵
    x_weighted = np.zeros((m, n))
    for j in range(n):
        x_weighted[:, j] = w[0][j] * x_norm[:, j]
    # 计算最优解和最劣解
    max_vec = x_weighted.max(axis=0)
    min_vec = x_weighted.min(axis=0)
    # 计算每个评价对象与最优解和最劣解的距离
    d_plus = np.sqrt(((x_weighted - max_vec)**2).sum(axis=1))
    d_minus = np.sqrt(((x_weighted - min_vec)**2).sum(axis=1))
    #print( d_minus)
    # 计算得分
    score = d_minus / (d_minus + d_plus)
    return score

x = np.array([[	3	,	2	,	10	]	,
[	0	,	4	,	11	]	,
[	1	,	2	,	12	]	,
[	2	,	1	,	11	]	,
[	1	,	4	,	10.5	]	,
[	0	,	4	,	12	]	,
[	1	,	4	,	10	]	,
[	1	,	4	,	10	]	,
[	1	,	2	,	10	]	,
[	0	,	4	,	11	]	,
[	3	,	2	,	12	]	,
[	2	,	4	,	10	]	,
[	0	,	4	,	11	]	,
[	0	,	4	,	12	]	,
[	2	,	1	,	10	]	,
[	1	,	4	,	12	]	,
[	0	,	4	,	12	]	,
[	1	,	5	,	8	]	,
[	0	,	4	,	12	]	,
[	2	,	1	,	6	]	,
[	0	,	4	,	12	]	,
[	1	,	4	,	6	]	,
[	0	,	2	,	8	]	,
[	1	,	1	,	11	]	,
[	0	,	4	,	12	]	,
[	0	,	4	,	11	]	,
[	2	,	4	,	10	]	,
[	1	,	4	,	10	]	,
[	2	,	2	,	10	]	,
[	0	,	4	,	12	]	,
[	0	,	1	,	11	]	,
[	0	,	4	,	10	]	,
[	1	,	2	,	10	]	,
[	0	,	4	,	12	]	,
[	0	,	4	,	11	]	,
[	2	,	4	,	9	]	,
[	1	,	1	,	11	]	,
[	3	,	1	,	9	]	,
[	0	,	5	,	7	]	,
[	0	,	2	,	12	]	,
[	2	,	4	,	11	]	,
[	2	,	1	,	10.5	]	,
[	0	,	4	,	10.5	]	,
[	1	,	1	,	9.5	]	,
[	1	,	2	,	10.5	]	,
[	2	,	3	,	11	]	,
[	3	,	2	,	10	]	,
[	0	,	4	,	12	]	,
[	0	,	1	,	11	]	,
[	2	,	2	,	7	]	,
[	1	,	4	,	10	]	,
[	3	,	4	,	9.5	]	,
[	4	,	1	,	10	]	,
[	0	,	4	,	11	]	,
[	5	,	2	,	5	]	,
[	1	,	4	,	10	]	,
[	1	,	4	,	10.5	]	,
[	1	,	4	,	12	]	,
[	3	,	1	,	8	]	,
[	0	,	4	,	12	]	,
[	1	,	5	,	10	]	,
[	0	,	4	,	10	]	,
[	0	,	4	,	10	]	,
[	1	,	1	,	12	]	,
[	1	,	5	,	10.5	]	,
[	0	,	4	,	12	]	,
[	3	,	1	,	9	]	,
[	5	,	1	,	9	]	,
[	1	,	4	,	12	]	,
[	2	,	4	,	10.5	]	,
[	0	,	4	,	11	]	,
[	2	,	2	,	9	]	,
[	5	,	1	,	10	]	,
[	0	,	4	,	11	]	,
[	0	,	4	,	12	]	,
[	2	,	1	,	11.5	]	,
[	1	,	2	,	9	]	,
[	1	,	4	,	12	]	,
[	0	,	4	,	11.5	]	,
[	0	,	4	,	11	]	,
[	0	,	4	,	11	]	,
[	5	,	4	,	11	]	,
[	1	,	4	,	11	]	,
[	0	,	4	,	10.5	]	,
[	6	,	3	,	11	]	,
[	0	,	4	,	12	]	,
[	0	,	4	,	11.5	]	,
[	0	,	2	,	12	]	,
[	1	,	1	,	11	]	,
[	1	,	2	,	12	]	,
[	0	,	5	,	11	]	,
[	3	,	4	,	8	]	,
[	4	,	5	,	10	]	,
[	0	,	4	,	10.5	]	,
[	1	,	4	,	7	]	,
[	6	,	1	,	8	]	,
[	0	,	5	,	11	]	,
[	1	,	4	,	12	]	,
[	2	,	2	,	7	]	,
[	0	,	4	,	12	]	,
[	0	,	4	,	10	]	,
[	4	,	1	,	10	]	,
[	0	,	2	,	8	]	,
[	2	,	1	,	9	]	,
[	1	,	4	,	11	]	,
[	1	,	2	,	9.5	]	,
[	2	,	3	,	10	]	,
[	1	,	4	,	10.5	]	,
[	2	,	3	,	10	]	,
[	2	,	4	,	9	]	,
[	1	,	2	,	10.5	]	,
[	1	,	5	,	11	]	,
[	0	,	4	,	10.5	]	,
[	2	,	5	,	11	]	,
[	1	,	4	,	9.5	]	,
[	1	,	2	,	11	]	,
[	0	,	4	,	12	]	,
[	3	,	5	,	10	]	,
[	1	,	1	,	9	]	,
[	0	,	4	,	11	]	,
[	2	,	5	,	10	]	,
[	0	,	1	,	10	]	,
[	2	,	4	,	11	]	,
[	5	,	1	,	10	]	,
[	2	,	2	,	9	]	,
[	0	,	4	,	12	]	,
[	0	,	4	,	11.25	]	,
[	1	,	1	,	10.5	]	,
[	0	,	1	,	12	]	,
[	1	,	1	,	10	]	,
[	1	,	1	,	7	]	,
[	4	,	2	,	10	]	,
[	1	,	4	,	7	]	,
[	0	,	4	,	11	]	,
[	1	,	3	,	12	]	,
[	2	,	5	,	8	]	,
[	1	,	2	,	10	]	,
[	1	,	4	,	10	]	,
[	0	,	5	,	11.5	]	,
[	1	,	1	,	8	]	,
[	0	,	4	,	10	]	,
[	1	,	4	,	10.5	]	,
[	1	,	4	,	11	]	,
[	1	,	3	,	10	]	,
[	0	,	4	,	10	]	,
[	6	,	1	,	10	]	,
[	3	,	1	,	11	]	,
[	1	,	4	,	12	]	,
[	2	,	1	,	10	]	,
[	0	,	4	,	11	]	,
[	0	,	4	,	10.5	]	,
[	1	,	1	,	11	]	,
[	1	,	4	,	7	]	,
[	0	,	4	,	12	]	,
[	1	,	3	,	10.5	]	,
[	2	,	1	,	12	]	,
[	1	,	2	,	10	]	,
[	3	,	1	,	11	]	,
[	0	,	4	,	10	]	,
[	0	,	1	,	9.5	]	,
[	1	,	3	,	10	]	,
[	4	,	1	,	9.5	]	,
[	1	,	4	,	12	]	,
[	2	,	1	,	10.5	]	,
[	2	,	2	,	9	]	,
[	4	,	4	,	10	]	,
[	1	,	5	,	10	]	,
[	3	,	5	,	10	]	,
[	2	,	4	,	10	]	,
[	2	,	2	,	10	]	,
[	3	,	5	,	10	]	,
[	3	,	4	,	10	]	,
[	0	,	4	,	10	]	,
[	0	,	4	,	12	]	,
[	1	,	4	,	12	]	,
[	3	,	1	,	11	]	,
[	1	,	2	,	7	]	,
[	0	,	4	,	11	]	,
[	1	,	4	,	12	]	,
[	0	,	4	,	12	]	,
[	3	,	4	,	10	]	,
[	0	,	5	,	9	]	,
[	3	,	4	,	10.5	]	,
[	3	,	5	,	11	]	,
[	4	,	1	,	7.5	]	,
[	0	,	2	,	10	]	,
[	4	,	4	,	11	]	,
[	0	,	4	,	10.5	]	,
[	1	,	4	,	11	]	,
[	2	,	5	,	9	]	,
[	1	,	4	,	10	]	,
[	2	,	4	,	11	]	,
[	1	,	5	,	10	]	,
[	0	,	1	,	10	]	,
[	3	,	1	,	11	]	,
[	2	,	1	,	7	]	,
[	0	,	4	,	11	]	,
[	0	,	2	,	10	]	,
[	1	,	5	,	8	]	,
[	0	,	4	,	10.5	]	,
[	0	,	5	,	10	]	,
[	1	,	3	,	11	]	,
[	2	,	1	,	12	]	,
[	3	,	2	,	10	]	,
[	1	,	4	,	9	]	,
[	0	,	1	,	9.5	]	,
[	1	,	1	,	12	]	,
[	1	,	5	,	12	]	,
[	0	,	4	,	11	]	,
[	0	,	4	,	11	]	,
[	0	,	4	,	11	]	,
[	2	,	3	,	9	]	,
[	0	,	1	,	12	]	,
[	1	,	4	,	10	]	,
[	0	,	4	,	11	]	,
[	2	,	4	,	10	]	,
[	3	,	4	,	8	]	,
[	2	,	4	,	12	]	,
[	1	,	2	,	11	]	,
[	0	,	1	,	8	]	,
[	1	,	2	,	10	]	,
[	0	,	4	,	9	]	,
[	2	,	3	,	10	]	,
[	0	,	3	,	9	]	,
[	1	,	4	,	12	]	,
[	2	,	5	,	12	]	,
[	5	,	1	,	6	]	,
[	1	,	3	,	10	]	,
[	4	,	2	,	9	]	,
[	1	,	1	,	9	]	,
[	1	,	4	,	10	]	,
[	1	,	5	,	12	]	,
[	0	,	1	,	10	]	,
[	4	,	1	,	7	]	,
[	0	,	2	,	10	]	,
[	10	,	5	,	10	]	,
[	2	,	3	,	9	]	,
[	3	,	4	,	11	]	,
[	10	,	1	,	11	]	,
[	0	,	2	,	9	]	,
[	1	,	2	,	12	]	,
[	0	,	4	,	10	]	,
[	3	,	2	,	10	]	,
[	0	,	2	,	10	]	,
[	2	,	5	,	11	]	,
[	2	,	2	,	10	]	,
[	1	,	2	,	9	]	,
[	2	,	5	,	10	]	,
[	3	,	1	,	11	]	,
[	0	,	4	,	11	]	,
[	1	,	2	,	11	]	,
[	1	,	2	,	9.5	]	,
[	2	,	2	,	10	]	,
[	2	,	5	,	10.5	]	,
[	1	,	5	,	10	]	,
[	2	,	2	,	10.5	]	,
[	1	,	2	,	9	]	,
[	1	,	1	,	9	]	,
[	5	,	3	,	11	]	,
[	1	,	1	,	7.5	]	,
[	2	,	4	,	12	]	,
[	3	,	5	,	9.5	]	,
[	1	,	2	,	8	]	,
[	4	,	4	,	11	]	,
[	0	,	4	,	12	]	,
[	5	,	1	,	10	]	,
[	5	,	1	,	12	]	,
[	1	,	4	,	10	]	,
[	1	,	2	,	10	]	,
[	2	,	4	,	9	]	,
[	5	,	1	,	9	]	,
[	2	,	1	,	10	]	,
[	3	,	4	,	10	]	,
[	3	,	1	,	10	]	,
[	2	,	1	,	8.5	]	,
[	3	,	4	,	11	]	,
[	2	,	2	,	10	]	,
[	4	,	5	,	8	]	,
[	8	,	1	,	8	]	,
[	3	,	4	,	11	]	,
[	1	,	1	,	7	]	,
[	0	,	3	,	10	]	,
[	2	,	1	,	10	]	,
[	1	,	5	,	10	]	,
[	1	,	4	,	10	]	,
[	2	,	1	,	10	]	,
[	4	,	2	,	11.5	]	,
[	4	,	5	,	12	]	,
[	0	,	2	,	10	]	,
[	1	,	4	,	10	]	,
[	4	,	1	,	6	]	,
[	0	,	4	,	11	]	,
[	2	,	2	,	9	]	,
[	0	,	1	,	10	]	,
[	2	,	2	,	11	]	,
[	4	,	5	,	12	]	,
[	2	,	1	,	11	]	,
[	1	,	2	,	12	]	,
[	1	,	5	,	9	]	,
[	3	,	1	,	11	]	,
[	2	,	4	,	10.5	]	,
[	3	,	2	,	8	]	,
[	0	,	2	,	10	]	,
[	0	,	2	,	12	]	,
[	2	,	1	,	8	]	,
[	5	,	4	,	10.5	]	,
[	1	,	2	,	9	]	,
[	2	,	3	,	10	]	,
[	1	,	3	,	9	]	,
[	0	,	2	,	11	]	,
[	5	,	5	,	10	]	,
[	2	,	4	,	10	]	,
[	0	,	4	,	10	]	,
[	0	,	1	,	9	]	,
[	0	,	4	,	10	]	,
[	0	,	4	,	12	]	,
[	0	,	4	,	12	]	,
[	1	,	3	,	11	]	,
[	3	,	2	,	10.5	]	,
[	5	,	4	,	7	]	,
[	1	,	1	,	10	]	,
[	0	,	4	,	12	]	,
[	1	,	5	,	8	]	,
[	0	,	4	,	11	]	,
[	7	,	1	,	5	]	,
[	1	,	4	,	12	]	,
[	0	,	4	,	11.5	]	,
[	1	,	4	,	10	]	,
[	1	,	4	,	7	]	,
[	0	,	2	,	11	]	,
[	0	,	4	,	11	]	,
[	0	,	5	,	11.5	]	,
[	1	,	4	,	11	]	,
[	0	,	4	,	10.5	]	,
[	1	,	4	,	10.5	]	,
[	1	,	1	,	10	]	,
[	0	,	4	,	12	]	,
[	5	,	1	,	8	]	,
[	5	,	4	,	10	]	,
[	0	,	4	,	12	]	,
[	0	,	4	,	12	]	,
[	4	,	1	,	9	]	,
[	0	,	2	,	9	]	,
[	0	,	4	,	10	]	,
[	2	,	4	,	11	]	,
[	0	,	4	,	8.5	]	,
[	0	,	4	,	10.5	]	,
[	0	,	4	,	12	]	,
[	1	,	4	,	11	]	,
[	1	,	3	,	8	]	,
[	0	,	4	,	12	]	,
[	2	,	5	,	10	]	,
[	1	,	4	,	10.5	]	,
[	0	,	1	,	9.5	]	,
[	1	,	2	,	10	]	,
[	0	,	4	,	11	]	,
[	1	,	4	,	12	]	,
[	0	,	4	,	11.5	]	,
[	1	,	2	,	8	]	,
[	3	,	1	,	10	]	,
[	6	,	1	,	12	]	,
[	0	,	4	,	12	]	,
[	2	,	1	,	6	]	,
[	3	,	1	,	8	]	,
[	0	,	5	,	10	]	,
[	1	,	2	,	10	]	,
[	5	,	1	,	7	]	,
[	1	,	4	,	11	]	,
[	1	,	5	,	9	]	,
[	0	,	2	,	12	]	,
[	2	,	1	,	11	]	,
[	2	,	2	,	10	]	,
[	0	,	4	,	12	]	,
[	3	,	2	,	5	]	,
[	0	,	1	,	11	]	,
[	2	,	1	,	8	]	,
[	1	,	4	,	11	]	,
[	0	,	4	,	10	]	,
[	2	,	5	,	7	]	,
[	0	,	5	,	9	]	,
[	1	,	4	,	10	]	,
[	1	,	5	,	11	]	,
[	0	,	4	,	9	]	,
[	2	,	1	,	10	]	,
[	1	,	2	,	9	]	,
[	2	,	4	,	11	]	,
[	2	,	1	,	10.5	]	,
[	2	,	1	,	6	]	,
[	0	,	4	,	9	]
])
reverse_cols = [0, 1]  # 第一列和第二列是负指标
x = normalize_direction(x, reverse_cols)

# 计算熵权法得到的权重
w = entropy_weight(x)

# 计算TOPSIS得分
score = topsis(x, w)
#print(w)

#df = pd.DataFrame(score, columns=['Score'])
# Export the DataFrame to an Excel file
#df.to_excel('score.xlsx', index=False)