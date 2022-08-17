from typing import Optional
from fastapi import FastAPI
from models.users import User
import psycopg2

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

conn = psycopg2.connect(database='postgres', user='postgres',password='123456',host='127.0.0.1',port='5432')
cur = conn.cursor()

# # # cur.execute('''insert into public."ADMIN"(aid,name, password) values ('2','test2','123')''')
# # # cur.execute('''delete from public."ADMIN" where aid = 2 ''')
# # # cur.execute("""update public."ADMIN" set name = 'test3'""")

# cur.execute('select * from public."USER"')
# result = cur.fetchall()
# print(result)

a = User()
a.test()



















