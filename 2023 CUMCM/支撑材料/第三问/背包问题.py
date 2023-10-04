import numpy as np
import pandas as pd
import math
data=pd.read_excel('第三问单品利润及销量.xlsx')
data=data[data['分类名称']=='水生根茎类']
w = list(map(math.ceil, data['平均销量'].values))#单品销量
v = list(map(math.ceil, data['平均利润'].values))#单品利润
m = int(data['类别需求量'].values[0])#背包总载重
n = 7#单品种类
def comlete_1(n,m):
    dp = np.zeros((n+1,m+1))
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i-1] and dp[i][j] < dp[i-1][j-w[i-1]]+v[i-1]:
                dp[i][j] = dp[i-1][j - w[i-1]] + v[i-1]
    j = m
    x = [False for i in range(n)]
    for i in range(n,0,-1):
        if dp[i][j]>dp[i-1][j]:
            j-=w[i-1]
            x[i - 1] = True
            print('i=',i+1)#记录选择的物品
    return 0
print("水生根茎类")
comlete_1(n,m)

data=pd.read_excel('第三问单品利润及销量.xlsx')
data=data[data['分类名称']=='食用菌']
w = list(map(math.ceil, data['平均销量'].values))#单品销量
v = list(map(math.ceil, data['平均利润'].values))#单品利润
m = int(data['类别需求量'].values[0])#背包总载重
n = 5#单品种类
def comlete_1(n,m):
    dp = np.zeros((n+1,m+1))
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i-1] and dp[i][j] < dp[i-1][j-w[i-1]]+v[i-1]:
                dp[i][j] = dp[i-1][j - w[i-1]] + v[i-1]
    j = m
    x = [False for i in range(n)]
    for i in range(n,0,-1):
        if dp[i][j]>dp[i-1][j]:
            j-=w[i-1]
            x[i - 1] = True
            print('i=',i+1)#记录选择的物品
    return 0
print("食用菌")
comlete_1(n,m)

data=pd.read_excel('第三问单品利润及销量.xlsx')
data=data[data['分类名称']=='茄类']
w = list(map(math.ceil, data['平均销量'].values))#单品销量
v = list(map(math.ceil, data['平均利润'].values))#单品利润
m = int(data['类别需求量'].values[0])#背包总载重
n = 5#单品种类
def comlete_1(n,m):
    dp = np.zeros((n+1,m+1))
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i-1] and dp[i][j] < dp[i-1][j-w[i-1]]+v[i-1]:
                dp[i][j] = dp[i-1][j - w[i-1]] + v[i-1]
    j = m
    x = [False for i in range(n)]
    for i in range(n,0,-1):
        if dp[i][j]>dp[i-1][j]:
            j-=w[i-1]
            x[i - 1] = True
            print('i=',i+1)#记录选择的物品
    return 0
print("茄类")
comlete_1(n,m)


data=pd.read_excel('第三问单品利润及销量.xlsx')
data=data[data['分类名称']=='辣椒类']
w = list(map(math.ceil, data['平均销量'].values))#单品销量
v = list(map(math.ceil, data['平均利润'].values))#单品利润
m = int(data['类别需求量'].values[0])#背包总载重
n = 9#单品种类
def comlete_1(n,m):
    dp = np.zeros((n+1,m+1))
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i-1] and dp[i][j] < dp[i-1][j-w[i-1]]+v[i-1]:
                dp[i][j] = dp[i-1][j - w[i-1]] + v[i-1]
    j = m
    x = [False for i in range(n)]
    for i in range(n,0,-1):
        if dp[i][j]>dp[i-1][j]:
            j-=w[i-1]
            x[i - 1] = True
            print('i=',i+1)#记录选择的物品

    return 0
print("辣椒类")
comlete_1(n,m)

data=pd.read_excel('第三问单品利润及销量.xlsx')
data=data[data['分类名称']=='花叶类']
w = list(map(math.ceil, data['平均销量'].values))#单品销量
v = list(map(math.ceil, data['平均利润'].values))#单品利润
m = int(data['类别需求量'].values[0])#背包总载重
n = 5#单品种类
def comlete_1(n,m):
    dp = np.zeros((n+1,m+1))
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i-1] and dp[i][j] < dp[i-1][j-w[i-1]]+v[i-1]:
                dp[i][j] = dp[i-1][j - w[i-1]] + v[i-1]
    j = m
    x = [False for i in range(n)]
    for i in range(n,0,-1):
        if dp[i][j]>dp[i-1][j]:
            j-=w[i-1]
            x[i - 1] = True
            print('i=',i+1)#记录选择的物品
    return 0
print("花叶类")
comlete_1(n,m)

data=pd.read_excel('第三问单品利润及销量.xlsx')
data=data[data['分类名称']=='花菜类']
w = list(map(math.ceil, data['平均销量'].values))#单品销量
v = list(map(math.ceil, data['平均利润'].values))#单品利润
m = int(data['类别需求量'].values[0])#背包总载重
n = 2#单品种类
def comlete_1(n,m):
    dp = np.zeros((n+1,m+1))
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = dp[i - 1][j]
            if j >= w[i-1] and dp[i][j] < dp[i-1][j-w[i-1]]+v[i-1]:
                dp[i][j] = dp[i-1][j - w[i-1]] + v[i-1]
    j = m
    x = [False for i in range(n)]
    for i in range(n,0,-1):
        if dp[i][j]>dp[i-1][j]:
            j-=w[i-1]
            x[i - 1] = True
            print('i=',i+1)#记录选择的物品
    return 0
print("花菜类")
comlete_1(n,m)