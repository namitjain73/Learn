import pandas as pd
l1= [10,20,30,40,50]
s = pd.Series(l1,index=['A','B','C','D','E'])
print(s)

# create a dataframe from a dictionare data  attr = alife , bomb , charli , 
# 25 30 35
# newyork paris london tokio

l2 = {
    'Name' : ['Alice',"bob",'chali'],
    'age' : [25,30,35],
    'city' : ['NewYork','Paris','London']
}
s2 = pd.DataFrame(l2 , index = ['A','B','C'])
s2['salary'] = [500000,700000,600000]
print(s2)
