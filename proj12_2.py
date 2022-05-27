import pymysql as x
def ir():
    try:
        db=x.connect(host='localhost',user='root',passwd='root',db='q')
        cur=db.cursor()
        r=int(input("Enter roll no.:"))
        n =input("Enter Name:")
        m1=int(input("Enter marks1:"))
        m2=int(input("Enter marks2:"))
        m3=int(input("Enter marks3:"))
        t=m1+m2+m3
        p=t/3
        q="insert into stu values('%d','%s','%f','%f','%f','%f','%f')"%(r,n,m1,m2,m3,t,p)
        cur.execute(q)
        db.commit()
        cur.close()
        db.close()
    except:
        print("error in code")



def dr():
    try:
        db=x.connect(host='localhost',user='root',passwd='root',db='q')
        cur=db.cursor()
        q="select * from stu"
        r=cur.execute(q)
        rr=cur.fetchall()
        print("_"*75)
        print("{0:<5}{1:^20}{2:^10}{3:^10}{4:^10}{5:^10}{6:^10}"\
              .format('Roll','Name','Marks1','Marks2','Marks3','Total','Per'))
        print("_"*75)
        for i in rr:
            print("{0:<5}{1:^20}{2:^10}{3:^10}{4:^10}{5:^10}{6:^10}"\
                  .format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
            print("_"*75)  
        cur.close()
        db.close()
    except:
        print("error in code")

def dsr():
    try:
        db=x.connect(host='localhost',user='root',passwd='root',db='q')
        cur=db.cursor()
        x1=input("enter name:")
        q="select * from stu where name='%s'"%(x1)
        r=cur.execute(q)
        print(r)
        if r>0:
            rr=cur.fetchall()
            print("--------------------------------------------------------------")
            print("Roll\t  Name\t\tMarks1\tMarks2\tMarks3\tTotal\tPer")
            print("--------------------------------------------------------------")
            for i in rr:
                print(i[0],'\t',i[1],'\t',i[2],'\t',i[3],'\t',i[4],'\t',i[5],'\t',i[6])
                print("--------------------------------------------------------------")  
        else:
            print("No Record Found")
        cur.close()
        db.close()
    except:
        print("error in code")

def ur():
    try:
        db=x.connect(host='localhost',user='root',passwd='root',db='q')
        cur=db.cursor()
        r1=int(input("Enter RollNo:"))
        x1=input("enter name:")
        q="update stu set name='%s' where roll='%d'"%(x1,r1)
        r=cur.execute(q)
        db.commit()
        cur.close()
        db.close()
    except:
        print("error in code")

def delr():
    try:
        db=x.connect(host='localhost',user='root',passwd='root',db='q')
        cur=db.cursor()
        r1=int(input("Enter RollNo:"))
        q="delete from stu where roll='%d'"%(r1)
        r=cur.execute(q)
        db.commit()
        cur.close()
        db.close()
    except:
        print("error in code")


def menu1():
    while True:
        print()
        print("\t\t\t1. Insert Record")
        print("\t\t\t2. Display Records")
        print("\t\t\t3. Display Sp. Record")
        print("\t\t\t4. Update Record")
        print("\t\t\t5. Delete Record")
        print("\t\t\t6. Return to previous menu")
        c=int(input("\t\t\tEnter Choice:"))
        if c==1:
            ir()
        elif c==2:
            dr()
        elif c==3:
            dsr()
        elif c==4:
            ur()
        elif c==5:
            delr()
        else:
            break

#menu1()


#ir()
#dr()
#dsr()
#ur()
#delr()        
#dr()
