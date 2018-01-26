#this program handles all the operations while returning of the book
import time
from datetime import date
import datetime
import MySQLdb as m
import serial
import types
import rfidreader1
def fine(d1,m1,y1,d2,m2,y2):
    a=0
    d=date(y1,m1,d1)
    e=date(y2,m2,d2)
    delta=e-d
    a=delta.days
    return a+8
db=m.connect("localhost","root","","cap")
import RPi.GPIO as gpio
sql="""CREATE TABLE IF NOT EXISTS d(id varchar(10) not null,name varchar(20) not null,bookid varchar(10) not null,bookname varchar(30) not null,issuedate varchar(10),returndate varchar(10),status varchar(5))"""
cur=db.cursor()
cur.execute(sql)
while True:
	res=rfidreader1.reading()
        if res!=None:
            sql="select id,name,bookname,issuedate,returndate from d where bookid='%s' and status='1';" %res
            cur.execute(sql)
            result=cur.fetchall()
            if result==():
                print "None"
            else:
                for row in result:
                    Id=row[0]
                    name=row[1]
                    bookname=row[2]
                    issuedate=row[3]
                    returndate=row[4]
                print "Registration Number='%s'"%Id,
                print "Name='%s'"%name,
                print "Book Name='%s'"%bookname
                q=1
                l=returndate.split('/')
                now=time.strftime("%d/%m/%Y")
                k=[]
                k=now.split("/")
                j=map(int,k)
                p=map(int,l)
                g=fine(p[0],p[1],p[2],j[0],j[1],j[2])
                if g<0:
                    g=0
                print "Fine=Rs.%s"%g
                sql="update d set status='0' where bookid='%s';"%res
                try:
                    cur.execute(sql)
                    db.commit()
                except:
                    db.rollback()
                
                print "Book Returned Successfully"
                
                sql="select bookname from d where id='%s' and status='%s'"%(Id,q)
                cur.execute(sql)
                h=cur.fetchall()
                if h==():
                    print "No Books Left"
                else:
                    print "Books Left=%s"%h
                
        else:
            break
        time.sleep(1)
        
