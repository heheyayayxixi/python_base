import numpy as np
import pandas as pd

#4 数据清洗

#缺失值处理
#dropna:根据标签中的缺失值进行过滤，删除缺失值
#fillna:对缺失值进行填充
#isnull:返回一个布尔值对象，判断哪些值是缺失值
#notnull:

df_mv=pd.read_excel(r'.\豆瓣电影数据.xlsx',header=0,index_col=0)
#print(df_mv.head())

#判断缺失值
#print(df_mv[df_mv['名字'].isnull()].head())
#填充缺失值
df_mv['名字'].fillna('未知电影',inplace=True,axis=0)
#print(df_mv[df_mv['名字'].isnull()].head())
dit={'名字':'复仇者联盟3',
     '投票人数':123456,
     '类型':'剧情/科幻',
     '产地':'美国',
     '上映时间':'2017-05-04 00:00:00',
     '时长':142,
     '年代':2017,
     '评分':np.nan,
     '首映地点':'美国'}
s=pd.Series(dit)
s.name=38738
df_mv=df_mv.append(s)
df_mv['评分'].fillna(np.mean(df_mv['评分']),inplace=True)
#print(df_mv['评分'][-5:])
#df1=df_mv.fillna('未知电影',inplace=False)
#print(df1[df1['名字'].isnull()].tail())

#删除缺失值
#print(len(df_mv))
df2=df_mv.dropna()
#print(len(df2))

#处理异常值
#print(df_mv[df_mv['投票人数']<0])
#print(df_mv[df_mv['投票人数']%1!=0])
df_mv=df_mv[df_mv['投票人数']>0]
df_mv=df_mv[df_mv['投票人数']%1==0]
print(df_mv[df_mv['投票人数']<0])

#数据保存
df_mv.to_excel('movie_data.xlsx')