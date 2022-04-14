import pandas as pd
import numpy as np

# Pandas读取数据和数据操作

#读取数据
df_mv=pd.read_excel(r'.\豆瓣电影数据.xlsx',header=0,index_col=0)#r是表示不进行转义,header=0表示第一行数据做colunms，index_col同理
#print(df_mv.head())

#行操作
#print(df_mv.iloc[0])
#print(df_mv.iloc[0:5])
#print(df_mv.loc[0:5])#有六行
#添加一行
dit={'名字':'复仇者联盟3',
     '投票人数':123456,
     '类型':'剧情/科幻',
     '产地':'美国',
     '上映时间':'2017-05-04 00:00:00',
     '时长':142,
     '年代':2017,
     '评分':8.7,
     '首映地点':'美国'}
s=pd.Series(dit)
s.name=38738#数据不完整居然添加不了
#print(s)
df_mv=df_mv.append(s)
#print(df_mv.tail())
#删除一行
df_mv=df_mv.drop([38738])#默认axis是0
#print(df_mv.tail())

#列操作
#print(df_mv.columns)
#print(df_mv['名字'][0:5])
#print(df_mv[['名字','类型']][:5])
#增加一列
df_mv['序号']=range(1,len(df_mv)+1)
#print(df_mv.head())
#删除一列
df_mv=df_mv.drop('序号',axis=1)
#print(df_mv.head())

#通过标签选择数据 df.loc[[index],[column]]通过标签选择数据
#print(df_mv.loc[[1,3,4],['名字','类型']])
#print(df_mv.loc[1,'名字'])
#条件选择
print(df_mv[df_mv['产地']=='中国大陆'].head())
print(df_mv[(df_mv.产地=='美国')&(df_mv.评分>9)].head())# & |且和或