import pymysql as x
db=x.connect(host='localhost',user='root',passwd='arnav',db='airline')
cur=db.cursor()
cur.execute("select * from class")
r=cur.fetchall()
for i in range(len(r)):
    for j in range(3):
        print(r[i][j],end="|")
    print("\n")
    



cur.close()
db.close()