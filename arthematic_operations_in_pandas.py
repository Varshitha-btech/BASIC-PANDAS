import pandas as pd
s=pd.Series([10,20,30,40,50])
s1=pd.Series([30,40,50])
#print(s,s1)
print(s+s1)
print(5+s+s1)
print(s*2)
print(s1**2)

import pandas as pd
s=pd.Series([10,20,30])#with same index
s1=pd.Series([1,2,3])
print(s)
print(s1)
print(s+s1)

import pandas as pd
s=pd.Series([10,20,30],index=['a','b','c'])#different index
s1=pd.Series([40,50,60],index=['b','a','d'])
print(s+s1)

import pandas as pd
s=pd.Series([10,20,30],index=['a','b','c'])#handling Nan in operation
s1=pd.Series([40,50,60],index=['b','a','d'])
print(s+s1)
print(s.add(s1,fill_value=0))


