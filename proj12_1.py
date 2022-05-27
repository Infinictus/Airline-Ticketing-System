import pymysql as x
from proj12_2 import *
from proj12_3 import *  

def f_cdb():
    q=input('enter username:')
    w=input('enter password:')
    try:
        db=x.connect(host='localhost',user=q,passwd=w,db='q')
        cur=db.cursor()
        try:
            r=cur.execute("desc stu")
            print("table exists",r)
        except:
            print("Creating new table")
            cur.execute("create table stu(roll int primary key,name char(20),m1 float,m2 float,m3 float, tot float, per float)")
            print("table created")
        finally:
            print("Database Already Exists")
            cur.close()
            db.close()
    except:
        print("Database Not Available- Creating Now")
        try:
            db=x.connect(host='localhost',user='root',passwd='root')
            cur=db.cursor()
            cur.execute("create database q")
            cur.execute("use q")
            cur.execute("create table stu(roll int primary key,name char(20),m1 float,m2 float,m3 float, tot float, per float)")
        except:
                print("Error in code")
    
        cur.close()
        db.close()
                



def menu():
    while True:
        print()
        print("\t\t\t1. Admin View")
        print("\t\t\t2. User View")
        print("\t\t\t3. Exit")
        c=int(input("\t\t\tEnter Choice:"))
        if c==1:
            f_cdb()
            menu1()
        elif c==2:
            menu2()
        else:
            break

menu()



        
              


