Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> info=np.array(['p','a','n','d','a','s'])
>>> a=pd.Series(info)
... 
>>> print(a)
0    p
1    a
2    n
3    d
4    a
5    s
dtype: object
>>> x=['Python','pandas']
>>> df=pd.DataFrame(x)
>>> print(df)
        0
0  Python
1  pandas
>>> b=pd.Series(['Java','C','C++',np.nan])
\
>>> 
>>> b.map({'Java':'Core'})
0    Core
1     NaN
2     NaN
3     NaN
dtype: object
>>> c=pd.Series(['java','C','C++',np.nan])
>>> c.map({'java':'core'})
0    core
1     NaN
2     NaN
3     NaN
dtype: object
>>> c.map('i like {}'.format, na_action='ignore')
0    i like java
1       i like C
2     i like C++
3            NaN
dtype: object
s=pd.Series(["a","b","c"],name="vals")
s.to_frame()
  vals
0    a
1    b
2    c
info={'ID':[101,102,103],'Department':['B.Sc','B.Tech','M.Tech']}
df=pd.DataFrame(info)
print(df)
    ID Department
0  101       B.Sc
1  102     B.Tech
2  103     M.Tech
infor={'one':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f']),'two':pd.Series([1,2,3,4,5,6,7,8],index=['a','b','c','d','e','f','g','h'])}
d1=pd.DataFrame(infor)
print(d1['one'])
a    1.0
b    2.0
c    3.0
d    4.0
e    5.0
f    6.0
g    NaN
h    NaN
Name: one, dtype: float64
inff={'one':pd.Series([1,2,3,4,5],index=['a','b','c','d','e']),'two':pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])}
df=pd.DataFrame(inff)
print("Add new column by passing series")
Add new column by passing series
df['three']=pd.Series([20,40,60],index=['a','b','c'])
print(df)
   one  two  three
a  1.0    1   20.0
b  2.0    2   40.0
c  3.0    3   60.0
d  4.0    4    NaN
e  5.0    5    NaN
f  NaN    6    NaN
print("Add new column using existing DataFrame columns")
Add new column using existing DataFrame columns
df['four']=df['one']+df['three']
print(df)
   one  two  three  four
a  1.0    1   20.0  21.0
b  2.0    2   40.0  42.0
c  3.0    3   60.0  63.0
d  4.0    4    NaN   NaN
e  5.0    5    NaN   NaN
f  NaN    6    NaN   NaN
