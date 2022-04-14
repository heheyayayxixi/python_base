import pandas as pd
import numpy as np
#1 Series数据类型
#初始化
a=pd.Series([1,3,2,np.nan,6,5])
print(a)
b=pd.Series([1,3,2,np.nan,6,5],index=['a','b','c','d','e','f'])
print(b)
#标签
print(a.index)
print(b.index)
#取值
print(a.values)
print(a[0])
#切片
print(a[2:5:2])
print(b['b':'f':2])#这里可以取到右括号的值
#索引赋值
a.index.name="索引"
print(a)
a.index=list('abcdef')
print(a)