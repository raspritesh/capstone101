import datetime
import time
from datetime import date
def fine(d1,m1,y1,d2,m2,y2):
    d=date(y1,m1,d1)
    e=date(y2,m2,d2)
    delta=e-d
    a=delta.days
    return a
p=[7,11,2017]            
now=time.strftime("%x")
print now
k=[]
k=now.split("/")
print k
l=map(int,k)
print l
l[2]=2017
g=fine(p[0],p[1],p[2],l[1],l[0],l[2])
print g
