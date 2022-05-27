import pymysql as x
import random

def basic():
    # u=input('enter sql username:')
    # p=input('enter sql password:')
    try:
        db=x.connect(host='localhost',user='root',passwd='arnav')
        cur=db.cursor()
        cur.execute("create database air")
        cur.execute("use air")
        cur.execute("create table data(f_name varchar(30),l_name varchar(30),gender varchar(1),ph_no int,email_id varchar(30),d_date varchar(30),r_date varchar(30),origin varchar(30),destination varchar(30),PNR varchar(5),status varchar(10))")
        cur.execute("create table classes(SNo int,name varchar(10),price int)")
        cur.execute("insert into classes values(1,'Economy',2000)")
        cur.execute("insert into classes values(2,'Business',4000)")
        cur.execute("insert into classes values(3,'First',6000)")
        db.commit()
        cur.execute("create table menu(SNo int,item varchar(20),price int)")
        cur.execute("insert into menu values(1,'Tea',20)")
        cur.execute("insert into menu values(2,'Coffee',20)")
        cur.execute("insert into menu values(3,'Soft Drink',30)")
        cur.execute("insert into menu values(4,'Soup',30)")
        cur.execute("insert into menu values(5,'Sandwich',50)")
        cur.execute("insert into menu values(6,'Salad',30)")
        cur.execute("insert into menu values(7,'Noodles',100)")
        cur.execute("insert into menu values(8,'Wrap',80)")
        cur.execute("insert into menu values(9,'Pastry',100)")
        cur.execute("insert into menu values(10,'Ice Cream',50)")
        db.commit()
        cur.execute("create table luggage(SNo int,weight varchar(10),price int)")
        cur.execute("insert into luggage values(1,'15Kg',1000)")
        cur.execute("insert into luggage values(2,'20Kg',2000)")
        cur.execute("insert into luggage values(3,'25Kg',3000)")
        cur.execute("insert into luggage values(4,'30Kg',4000)")
        db.commit()
        print('Database Created...')
        print('All Tables Created...')

    except:
        db=x.connect(host='localhost',user='root',passwd='arnav',db='air')
        cur=db.cursor()
        print("Database Already Exists...")

        try:
            cur.execute("desc data")
            print('Table - Data Exists...')
        except:
            cur.execute("create table data(f_name varchar(30),l_name varchar(30),gender varchar(1),ph_no int,email_id varchar(30),d_date varchar(30),r_date varchar(30),origin varchar(30),destination varchar(30),PNR varchar(5),status varchar(10))")
            print('Table - Data Created...')
      
        try:
            cur.execute("desc classes")
            print('Table - Class Exists...')
        except:
            cur.execute("create table classes(SNo int,name varchar(10),price int")
            cur.execute("insert into classes values(1,'Economy',2000)")
            cur.execute("insert into classes values(2,'Business',4000)")
            cur.execute("insert into classes values(3,'First',6000)")
            db.commit()
            print('Table - Class Created...')
        
        try:
            cur.execute("desc menu")
            print('Table - Menu Exists...')
        except:
            cur.execute("create table menu(SNo int,item varchar(10),price int)")
            cur.execute("insert into menu values(1,'Tea',20)")
            cur.execute("insert into menu values(2,'Coffee',20)")
            cur.execute("insert into menu values(3,'Soft Drink',30)")
            cur.execute("insert into menu values(4,'Soup',30)")
            cur.execute("insert into menu values(5,'Sandwich',50)")
            cur.execute("insert into menu values(6,'Salad',30)")
            cur.execute("insert into menu values(7,'Noodles',100)")
            cur.execute("insert into menu values(8,'Wrap',80)")
            cur.execute("insert into menu values(9,'Pastry',100)")
            cur.execute("insert into menu values(10,'Ice Cream',50)")
            db.commit()
            print('Table - Menu Created...')

        try:
            cur.execute("desc luggage")
            print('Table - Luggage Exists...')
        except:
            cur.execute("create table luggage(SNo int,weight varchar(10),price int)")
            cur.execute("insert into luggage values(1,'15Kg',1000)")
            cur.execute("insert into luggage values(2,'20Kg',2000)")
            cur.execute("insert into luggage values(3,'25Kg',3000)")
            cur.execute("insert into luggage values(4,'30Kg',4000)")
            db.commit()
            print('Table - Luggage Created...')
       
    finally:
        cur.close()
        db.close() 
       

def PNR_generator():
    characters="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    result="".join(random.sample(characters,5))
    return result


def bill_maker():
    amount=0
    db=x.connect(host='localhost',user='root',passwd='arnav',db='air')
    cur=db.cursor()
    cur.execute("select * from classes")
    f1=cur.fetchall()
    print("Choose the class you want to travel in")
    for a in range(len(f1)):
        for b in range(3):
            print(f1[a][b],end="|")
        print("\n")
    o1=int(input("Enter your choice: "))
    q1="select price from classes where SNo='%d'"%(o1)
    cur.execute(q1)
    r1=cur.fetchone()
    for g in r1:
        amount+=int(g)
    print('-'*100)

    cur.execute("select * from luggage")
    f2=cur.fetchall()
    print("Choose the weight of your luggage")
    for c in range(len(f2)):
        for d in range(3):
            print(f2[c][d],end="|")
        print("\n")
    o2=int(input("Enter your choice: "))
    p2=int(input("Enter quantity: "))
    q2="select price from luggage where SNo='%d'"%(o2)
    cur.execute(q2)
    r2=cur.fetchone()
    for h in r2:
        amount+=int(g)*p2
    print('-'*100)

    z1=input('Would you like to order something from the menu ? (Y/N): ').upper()
    if z1=="Y":
        cur.execute("select * from menu")
        f3=cur.fetchall()
        for e in range(len(f3)):
            for f in range(3):
                print(f3[e][f],end="|")
            print("\n")
        while True:
            o3=int(input("Enter your choice: "))
            p3=int(input("Enter quantity: "))
            q3="select price from menu where SNo='%d'"%(o3)
            cur.execute(q3)
            r3=cur.fetchone()
            for h in r3:
                amount+=int(h)*p3
            print('-'*100)
            z2=input('Anything else ? (Y/N): ').upper()
            if z2=="Y":
                continue
            else:
                break

    cur.close()
    db.close()
    return amount


def ticket_booking():
    db=x.connect(host='localhost',user='root',passwd='arnav',db='air')
    cur=db.cursor()
    d_date=input("Date of Departure(DD/MM/YYYY): ")
    r_date=input("Date of Return(DD/MM/YYYY): ")
    origin=input("Origin: ").upper()
    destination=input("Destination: ").upper()
    y=int(input('Number of Passengers: '))
    print('-'*100)
    if y==1:
        for i in range(y):
            f_name=input("First Name: ").upper()
            l_name=input("Last Name: ").upper()
            gender=input("Gender(M/F): ").upper()
            ph_no=int(input("Phone Number: "))
            email_id=input("Email Id: ").upper()
            status="BOOKED"
            PNR=PNR_generator()
            print('-'*100)
            q="insert into data values('%s','%s','%s','%d','%s','%s','%s','%s','%s','%s','%s')"%(f_name,l_name,gender,ph_no,email_id, d_date,r_date,origin,destination,PNR,status)
            cur.execute(q)
            db.commit()
            print('-'*100)
            print("PNR Number - ",PNR)
            print('-'*100)
            result=bill_maker()
            charge=random.randrange(20000,90000,1000)
            print('-'*100)
            print("Base Charge - ",charge)
            print('-'*100)
            print("Surcharge - ",result)
            print('-'*100)
            print("Total Amount - ",result+charge)
            print('-'*100)

    else:
        charge=random.randrange(20000,90000,1000)
        for j in range(y):
            print("Passenger",j+1)
            print("-"*100)
            f_name=input("First Name: ").upper()
            l_name=input("Last Name: ").upper()
            gender=input("Gender(M/F): ").upper()
            ph_no=int(input("Phone Number: "))
            email_id=input("Email Id: ").upper()
            status="BOOKED"
            PNR=PNR_generator()
            print('-'*100)
            q="insert into data values('%s','%s','%s','%d','%s','%s','%s','%s','%s','%s','%s')"%(f_name,l_name,gender,ph_no,email_id, d_date,r_date,origin,destination,PNR,status)
            cur.execute(q)
            db.commit()
            print('-'*100)
            print("PNR Number - ",PNR)
            print('-'*100)
            result=bill_maker()
            print('-'*100)
            print("Billing Amount - ",charge)
            print('-'*100)
            print("Surcharge - ",result)
            print('-'*100)
            print("Total - ",result+charge)
            print('-'*100)

    print("Ticket(s) Booked")
    print('*'*100)
    cur.close()
    db.close()


def ticket_status():
    db=x.connect(host='localhost',user='root',passwd='arnav',db='air')
    cur=db.cursor()
    cur.execute("select * from data")
    r=cur.fetchall()

    while True:
        print("Choose a method to retrieve your ticket status")
        print("1. PNR")
        print("2. Email Id")
        print("3. Phone Number")
        print("4. Exit")

        z=int(input("Enter your choice: "))
        f=0

        if z==1:
            a=input("Enter your PNR number: ").upper()
            for i in range(len(r)):
                if a == r[i][-2]:
                    result=r[i][-1]
                    f=f+1
                    break
                else:
                    f=0
            if f==1:
                print("Ticket Status -",result)
                print('*'*100)
                break

            if f==0:
                print("Not Found")
                print('-'*100)
                break


        elif z==2:
            b=input("Enter your Email Id: ").upper()
            for j in range(len(r)):
                if b == r[j][4]:
                    result=r[j][-1]
                    f=f+1
                    break
                else:
                    f=0
            if f==1:
                print("Ticket Status -",result)
                print('*'*100)
                break
                
            if f==0:
                print("Not Found")
                print('-'*100)
                break

        elif z==3:
            c=int(input("Enter your phone number: "))
            for k in range(len(r)):
                if c == r[k][3]:
                    result=r[k][-1]
                    f=f+1
                    break
                else:
                    f=0
            if f==1:
                print("Ticket Status -",result)
                print('*'*100)
                break
                
            if f==0:
                print("Not Found")
                print('-'*100)
                break

        elif z==4:
            break

        else:
            print("Please choose a valid option")
            print("-"*100)

    cur.close()
    db.close()


def ticket_cancelling():
    db=x.connect(host='localhost',user='root',passwd='arnav',db='air')
    cur=db.cursor()
    cur.execute("select * from data")
    r=cur.fetchall()
    while True:
        print("Choose a method to cancel your ticket")
        print("1. PNR")
        print("2. Email Id")
        print("3. Phone Number")
        print("4. Exit")

        z=int(input("Enter your choice: "))
        f=0

        if z==1:
            a=input("Enter your PNR number: ").upper()
            for i in range(len(r)):
                if a == r[i][-2]:
                    q="update data set status='%s' where PNR='%s'"%('CANCELLED',a)
                    r=cur.execute(q)
                    db.commit()
                    f=f+1
                    break
                else:
                    f=0
            if f==1:
                print("Ticket CANCELLED")
                print('*'*100)
                break
            if f==0:
                print("Not Found")
                print('-'*100)
                break

        elif z==2:
            b=input("Enter your Email Id: ").upper()
            for j in range(len(r)):
                if b == r[j][4]:
                    q="update data set status='%s' where email_id='%s'"%('CANCELLED',b)
                    r=cur.execute(q)
                    db.commit()
                    f=f+1
                    break
                else:
                    f=0
            if f==1:
                print("Ticket CANCELLED")
                print('*'*100)
                break
            if f==0:
                print("Not Found")
                print('-'*100)
                break

        elif z==3:
            c=int(input("Enter your phone number: "))
            for k in range(len(r)):
                if c == r[k][3]:
                    q="update data set status='%s' where ph_no='%d'"%('CANCELLED',c)
                    r=cur.execute(q)
                    db.commit()
                    f=f+1
                    break
                else:
                    f=0
            if f==1:
                print("Ticket CANCELLED")
                print('*'*100)
                break
            if f==0:
                print("Not Found")
                print('-'*100)
                break

        elif z==4:
            break

        else:
            print("Please choose a valid option")
            print("-"*100)

    cur.close()
    db.close()


def main_menu():
    basic()
    print("Welcome to Central Airlines".center(100,'-'))
    while True:
        print("1. Book Ticket(s)")
        print("2. Check Ticket Status")
        print("3. Cancel Ticket")
        print("4. Exit")
        print('*'*100)

        n=int(input("Enter your choice: "))

        if n==1:
            ticket_booking()

        elif n==2:
            ticket_status()

        elif n==3:
            ticket_cancelling()

        elif n==4:
            print("Goodbye".center(100,"-"))
            break

        else:
            print("Please choose a valid option")
            print('-'*100)

main_menu()