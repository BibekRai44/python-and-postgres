import os
import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="flask_db",
    user=os.environ['bibek'],
    password=os.environ['broke']
)
cur=conn.cursor()
cur.execute('drop table if exists pl;')
cur.execute(''' create table pl(
                          id  int ,
                          name varchar(30) not null,
                          planguage varchar(20),
                          info varchar(70))''')
                                 
cur.execute('INSERT INTO pl (id,name, planguage, info)'
            'VALUES (%s,%s, %s, %s)',
            (1,'sagar','python','powerful language in automation and ml'),
           )


conn.commit()
cur.close()
conn.close()                            