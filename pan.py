import numpy as n
import pandas as p
import matplotlib.pyplot as m
f=p.read_csv("Chemistry.csv")
print(f)
s=f.iloc[:,0]

print(s)
t=f.iloc[:,2]
print(t)
#print(f.isnull().sum())
m.bar(s,t)
m.show()
