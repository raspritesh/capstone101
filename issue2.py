import time
import MySQLdb as m
import serial
import types
import rfidreader1
db=m.connect("localhost","root","","cap")
import RPi.GPIO as gpio
sql="""CREATE TABLE IF NOT EXISTS d(id varchar(10) not null,name varchar(20) not null,bookid varchar(10) not null,bookname varchar(30) not null,issuedate varchar(10),returndate varchar(10),status varchar(5))"""
cur=db.cursor()
cur.execute(sql)
while True:
	res=rfidreader1.reading()
	
	
		
		
        if res!=None :
                print "djd"
                inp1=raw_input("Enter ID").strip('\n')
                inp2=raw_input("Enter name").strip('\n')
                inp3=raw_input("Enter bookname").strip('\n')
                inp4=raw_input("Enter issuedate").strip('\n')
                inp5=raw_input("Enter return date").strip('\n')
                inp6=1
                print "Book Issued"
                sql="insert into d(id,name,bookid,bookname,issuedate,returndate,status) values('%s','%s','%s','%s','%s','%s','%s');"%(inp1,inp2,res,inp3,inp4,inp5,inp6)
                try:
                	
                        cur.execute(sql)
                        db.commit()
			
		except Exception as e:
                	print "Some error occured:",e
                        db.rollback()
	else:
                
		break
                
	time.sleep(1)	
