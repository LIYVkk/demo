from unittest import result
import psycopg2

class User:
   
    def getUserData(self):
        conn = psycopg2.connect(database='postgres', user='postgres',password='123456',host='127.0.0.1',port='5432')
        cur = conn.cursor()
        cur.execute('select * from public."USER"')
        result = cur.fetchall()
        conn.close()
        return result

    def deleteUser(username):
        conn = psycopg2.connect(database='postgres', user='postgres',password='123456',host='127.0.0.1',port='5432')
        cur = conn.cursor()
        cur.execute('update public."USER" set is_deleted = true where username = '+ username)
        conn.close()

    def addUser(userData):
        conn = psycopg2.connect(database='postgres', user='postgres',password='123456',host='127.0.0.1',port='5432')
        cur = conn.cursor()
        cur.execute('insert into public."USER" values ('+userData+')')
        conn.close()


    def updateUserData(userData):
        conn = psycopg2.connect(database='postgres', user='postgres',password='123456',host='127.0.0.1',port='5432')
        cur = conn.cursor()
        cur.excute('update public."USER" set ')
        conn.close()

    
    def commit():
        cur.commit()

    def test(self):
        print('1')


