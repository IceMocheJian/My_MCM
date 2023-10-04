import sys
import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.tsa.api as smt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.graphics.api import qqplot
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pylab as plt
from matplotlib.pylab import style

style.use('ggplot')
from arch.unitroot import ADF
import warnings

warnings.filterwarnings("ignore")
pd.set_option('display.float_format', lambda x: '%.5f' % x)
np.set_printoptions(precision=5, suppress=True)
pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)
import datetime as dt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

dataframe = pd.read_excel('品类销量按天汇总.xlsx')
# dataframe=dataframe[0:19]
columns = dataframe.columns
data = dataframe.set_index('销售日期')
data.index = pd.to_datetime(data.index)


def choose(df, Ddf, col):
    df = df.astype(float)
    # 定阶
    pmax = int(len(Ddf) / 10)  # 一般阶数不超过length/10
    qmax = int(len(Ddf) / 10)  # 一般阶数不超过length/10
    bic_matrix = []  # bic矩阵
    for p in range(pmax + 1):
        tmp = []
        for q in range(qmax + 1):
            try:  # 存在部分报错，所以用try来跳过报错。
                tmp.append(sm.tsa.arima.ARIMA(df, order=(p, 1, q)).fit().aic)
            except:
                tmp.append(None)
        bic_matrix.append(tmp)
    bic_matrix = pd.DataFrame(bic_matrix)  # 从中可以找出最小值
    p, q = bic_matrix.stack().idxmin()  # 先用stack展平，然后用idxmin找出最小值位置。
    print(u'BIC最小的p值和q值为：%s、%s' % (p, q))
    return


for col in columns[1:]:
    df_d1 = data.diff(1).dropna()
    # choose_model(data,col)
    choose(data[str(col)], df_d1[str(col)], col)
