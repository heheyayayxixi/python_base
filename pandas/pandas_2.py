import pandas as pd
import numpy as np

#2 DataFrame数据类型

#DataFrame的初始化
date=pd.date_range('20220101',periods=6)
print(date)
df=pd.DataFrame(np.random.randn(6,4),index=date,columns=list('ABCD'))#index行索引，columns列索引
print(df)

#字典传入数据
df1=pd.DataFrame({'A':1,'B':pd.Timestamp('20220101'),'C': pd.Series(1,index=list(range(5)),dtype='float')})
print(df1)
print(df1.dtypes)

#DataFrame查看头尾数据
print(df.head())
print(df.tail(2))
#DataFrame查看下标，列表，数据
print(df.index)
print(df.columns)
print(df.values)