import pandas as pd
import numpy  as np

df=pd.read_excel('movie_data.xlsx',header=0,index_col=0)
#print(df[:5])

#数据格式转换

#查看格式
#print(df['投票人数'].dtype)
#df['投票人数']=df['投票人数'].astype('float64')
#print(df['投票人数'].dtype)
#print(df['产地'].dtype)
#df['产地']=df['产地'].astype('str')
#print(df['产地'].dtype)#pandas没有区别str和object

#将年份转化为整数格式
#print(df['年代'].dtype)
#df['年代']=df['年代'].astype('int')#报错，因为数据中有一个格式有问题 ValueError: invalid literal for int() with base 10: '2008\u200e'
#print(df[df['年代']=='2008\u200e'])
#print(df[df['年代']=='2008\u200e']['年代'].values)
#df.loc[15205,'年代']=2008
#df['年代']=df['年代'].astype('int')
#print(df['年代'][:5])

#将时长转化为整数格式
#df['时长']=df['时长'].astype('int64')#invalid literal for int() with base 10: '8U'
#print(df[df['时长']=='8U'])
df.drop(labels=31644,inplace=True)
#print(df.iloc[31644])
#print(df[df['时长']=='12J'])
df.drop(labels=32949,inplace=True)
df['时长']=df['时长'].astype('int64')
#print(df['时长'][:5])
#######################################################

#排序
#print(df.sort_values(by='投票人数',ascending=False,inplace=False)[:5])
#多个值排序
#print(df.sort_values(by=['评分','投票人数'],ascending=False,inplace=False))

#######################################################

#基本统计分析
#描述性统计
#print(df.describe())
#print(df[df['年代']=='2008\u200e'])
df.drop(labels=15205,inplace=True)
df['年代']=df['年代'].astype('int')
df.drop(labels=df[df['年代']>2018].index,inplace=True)
df.drop(labels=df[df['时长']>1000].index,inplace=True)
#print(df[df['年代']>2018])
#print(df[df['时长']>1000])
df.index=range(len(df))#经过之前步骤的删除，index已经不连续了
#最值
#print(df['投票人数'].max())
#print(df['投票人数'].min())
#均值和中值
#print(df['投票人数'].mean())
#print(df['投票人数'].median())
#方差和标准差
#print(df['投票人数'].var())
#print(df['投票人数'].std())
#求和
#print(df['投票人数'].sum())
#相关系数和协方差
#print(df[['投票人数','评分']].corr())
#print(df[['投票人数','评分']].cov())
#计数
#print(len(df))
df['产地'].replace('USA','美国',inplace=True)
df['产地'].replace(['西德','苏联'],['德国','俄罗斯'],inplace=True)
#print(df['产地'].unique())
#print(len(df['产地'].unique()))
#计算每一年电影的产量
print(df['年代'].value_counts())

df.to_excel('movie_data2.xlsx')
