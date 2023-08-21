from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.model_selection import cross_val_score,StratifiedKFold
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, VotingClassifier
import pandas as pd

from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.neural_network import MLPClassifier

from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier

from sklearn.ensemble import GradientBoostingClassifier

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

from xgboost import XGBClassifier
from xgboost import XGBRFClassifier

if __name__ == '__main__':
    # 母亲身体指标
    mother_physics = ['mother_age', 'marriage', 'education', 'pregnant', 'birth_method']
    # 母亲心理指标
    mother_mental = ['CBTS', 'EPDS', 'HADS']
    # 婴儿睡眠质量,
    sleep_quality = ['wake_times', 'sleep_way', 'sleep_time']
    #婴儿信息
    baby = ['baby_gender',	'baby_age']
    # 婴儿行为模式
    action_mode = ['mode']
    #导入训练集
    data = pd.read_excel('data.xlsx')
    #导入预测集
    target = pd.read_excel('predict.xlsx')
    X = data[mother_mental+mother_physics+baby]
    y = data[action_mode]
    x = target[mother_mental+mother_physics+baby]

    #切分训练集和验证集
    #X_train, X_test, y_train, y_test = train_test_split(X, y,train_size=0.75,shuffle=True)

    #更换各种模型进行预测
    MLP =MLPClassifier()

    rf = RandomForestClassifier()
    dt = DecisionTreeClassifier()
    logic = LogisticRegression()
    KNN = KNeighborsClassifier()
    xgb = XGBRFClassifier()


    #投票分类器
    vote = VotingClassifier(estimators=[('MLP',MLP),('rf',rf),('xgb',xgb),('logic',logic),('KNN',KNN)],voting='hard')
    model = xgb
    #model.fit(X,y)
    #print(model.predict(x))
    '''
    #分层k折交叉验证
    #更换k值以求得最佳比例
    stratifiedkf = StratifiedKFold(n_splits=5)
    #计算准确率
    score = cross_val_score(model,X,y,cv=stratifiedkf)
    print(score)
    score=pd.DataFrame(score)
    score.to_csv("result.csv",index=False,mode='a')
    #rf.fit(X_train,y_train)
'''
    #模型训练
    model.fit(X,y)
    #预测未知婴儿模式
    result = pd.DataFrame(model.predict(x))
    print(result)
    #result.to_csv('presume.csv',index=False,mode='a')
    #print(rf.score(X_test,y_test))

