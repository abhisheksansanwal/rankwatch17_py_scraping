import re
import urllib.request
#https://www.babynamesdirect.com/baby-names/
url="https://www.babynamesdirect.com/baby-names/"
word=input("enter your category:")
word2=input("enter gender:")
word3=input("enter the word:")
url=url+word+word2+word3
data=urllib.request.urlopen(url).read()
#decode the data
data1=data.decode("utf-8")
m=research('metaname="description""content=s"',data1)
start=m.end()
end=start+300
newsting=data1[start:end]
print(newstring)
m=research("seemore",new string)
end=m.start()-1
babyname=newstring(0:end)
print(babyname)
#first to analysing data install package pandas
#Then import that package
import pandas as pd
users=pd.read_csv('name_gender',sep="|",names=["name","gender"])
pd.read_csv('name_gender.csv')
#the data is so large so we us head() to give first 5 line
user.head()


