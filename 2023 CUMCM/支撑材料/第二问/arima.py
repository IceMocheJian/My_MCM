import statsmodels.api as sm
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox
import warnings
warnings.filterwarnings("ignore")


dataframe=pd.read_excel('品类销量按天汇总.xlsx')
dataframe=dataframe[936:1086]
columns = dataframe.columns
data = dataframe.set_index('销售日期')
data.index = pd.to_datetime(data.index)
P=[1,	3,	3,	3,	4,	1]
Q=[6,	0,	1,	0,	2,	1]

def AR(data,p,q):
    model = sm.tsa.arima.ARIMA(data, order=(p,1,q))
    result = model.fit()
    print(result.summary()) #给出模型报告
    yc=result.forecast(7)#作为期7天的预测
    print("作为期7天的预测:")
    print(yc)
    cc=result.resid
    #白噪声检验
    print(u'残差序列的白噪声检验结果为：', acorr_ljungbox(cc, lags=1)) #返回统计量和p值
    return yc

def score(X,Y):
    return

for i in range(1,7):
    col=columns[i]
    p=P[i-1]
    q=Q[i-1]
    print(str(col))
    AR(data[str(col)],p,q)
