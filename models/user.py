from unittest import result
# import psycopg2

class User:
   
    def getUserData():
        cur.execute('select * from public."USER"')
        result = cur.fetchall()
        return result

    def deleteUser(username):
        cur.execute('update public."USER" set is_deleted = true where username = '+ username)
    
    def addUser(userData):
        cur.execute('insert into public."USER" values ('+userData+')')
    
    def updateUserData(userData):
        cur.excute('update public."USER" set ')
    
    def commit():
        cur.commit()

    def test():
        print(1)


