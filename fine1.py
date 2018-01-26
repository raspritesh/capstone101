from datetime import date
import time
d1=int(raw_input())
m1=int(raw_input())
y1=int(raw_input())
d2=int(raw_input())
m2=int(raw_input())
y2=int(raw_input())
d=date(y1,m1,d1)
e=date(y2,m2,d2)
delta=e-d
a=delta.days
print a
