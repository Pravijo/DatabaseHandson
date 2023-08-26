from mysql import connector
dbconnection = connector.connect(host='localhost',user='root',password='root',database='Pythonmagnus')
print(dbconnection)
c = dbconnection.cursor()


class Table:
    def create(self):
        c.execute("create table grocerylist(ino int,iname varchar(20),idept varchar(20),icount int)")
        dbconnection.commit()

    def insert(self):
        itemno=int(input("enter ino: "))
        itemname=input("enter iname: ")
        itemdept=input("enter idept: ")
        itemcount=int(input("enter icount: "))
        c.execute("insert into grocerylist(ino, iname, idept, icount) values(%s, %s, %s, %s)", (itemno, itemname, itemdept, itemcount))
        dbconnection.commit()
        dbconnection.close()

    def update(self):
        c.execute("update grocerylist set iname='silverware', icount=12 where ino=8")
        dbconnection.commit()
        dbconnection.close()

    def delete(self):
        c.execute("delete from grocerylist where ino=7")
        dbconnection.commit()
        dbconnection.close()

    def alter(self):
        c.execute("alter table grocerylist add icost float")
        c.execute("alter table grocerylist change ino iid int")
        dbconnection.close()

    def select(self):
        sqlquery = "select * from grocerylist where icount=6"
        c.execute(sqlquery)
        result = c.fetchall()
        for i in result:
            print(i)
        dbconnection.close()


obj1 = Table()
# obj1.create()
# obj1.insert()
# obj1.update()
# obj1.delete()
# obj1.alter()
obj1.select()

