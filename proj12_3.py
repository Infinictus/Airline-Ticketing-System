import pymysql as x

def cv():
    try:
        db=x.connect(host='localhost',user='root',passwd='root',db='q')
        cur=db.cursor()

        '''
        q="create view stu1 as(select roll, name from stu)"
        r=cur.execute(q)
        '''
        r1=int(input("Enter Roll No:"))
        n1=input("Enter correct name:")

        q="update stu1 set name='%s' where roll='%d'"%(n1,r1)
        r=cur.execute(q)
        db.commit()
'''
        q="select * from stu1"
        r=cur.execute(q)
        print(cur.fetchall())
'''        
        
    except:
        print("error in code")
    cur.close()
    db.close()

def dusr():
    try:
        db=x.connect(host='localhost',user='root',passwd='root',db='q')
        cur=db.cursor()
        x1=int(input("enter your roll:"))
        q="select * from stu where roll='%d'"%(x1)
        r=cur.execute(q)
        print()
        if r>0:
            rr=cur.fetchall()
            for i in rr:
                print("{0:^35}".format("Delhi Public School, Dwarka"))
                print("_"*40)
                
                print("{0:<5}{1:<3}\t\t{2:<6}{3:<15}"\
                      .format('Roll:',i[0],'Name:',i[1]))
                
                print("_"*40)
                print("{0:<15}\t\t{1:^15}".format("Subject","Marks"))
                print()
                print("{0:<15}\t\t\t{1:^5}".format("English",i[2]))
                print("{0:<15}\t\t\t{1:^5}".format("Maths",i[3]))
                print("{0:<15}\t\t\t{1:^5}".format("Comp Sc",i[4]))
                print("_"*40)
                print("{0:<5}{1:<3}\t\t{2:<6}{3:<15}"\
                      .format('Total:',i[5],'Per:',i[6]))
                print("_"*40)
        else:
            print("No Record Found")
        cur.close()
        db.close()
    except:
        print("error in code")

def totupd():
    try:
        db=x.connect(host='localhost',user='root',passwd='root',db='q')
        cur=db.cursor()
        x1=int(input("enter your roll:"))
        tot1=int(input("enter your new total:"))
        q="insert into ct values('%d','%d')"%(x1,tot1)
        r=cur.execute(q)
        db.commit()
    except:
        print("error in the code")
    
    cur.close()
    db.close()
    
def recupdate():
    try:
        db=x.connect(host='localhost',user='root',passwd='root',db='q')
        cur=db.cursor()
        q="select * from ct"
        r=cur.execute(q)
        rr=cur.fetchall()
        for i in rr:
            q="update stu set tot='%d' where roll='%d'"%(i[1],i[0])
            cur.execute(q)

        db.commit()
        q="delete from ct"
        cur.execute(q)
        db.commit()
        

        
    except:
        print("error in the code")
    
    cur.close()
    db.close()

def menu2():
    while True:
        print()
        print("\t\t\t 1. Display Report Card")
        print("\t\t\t 2. Update Name")
        print("\t\t\t 3. Back to main menu")
        c=int(input("\t\t\t Enter Choice:"))
        if c==1:
            dusr()
        elif c==2:
            cv()
        else:
            break

#menu2()


#dusr()
#cv()
#totupd()
#recupdate()
