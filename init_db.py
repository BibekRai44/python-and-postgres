import os
import psycopg2

conn=psycopg2.connect(
    host="localhost",
    database="flask_db",
    user="bibek",
    password="broke"
)
cur=conn.cursor()
cur.execute('drop table if exists pl;')
cur.execute(''' create table pl(
                          id  int ,
                          name varchar(30) not null,
                          planguage varchar(20),
                          info varchar(100))''')
                               
cur.execute('INSERT INTO pl (id,name, planguage, info)'
            'VALUES (%s,%s, %s, %s)',
           (1,'bibek','Python','powerful language in automation and ml')
           )
cur.execute('INSERT INTO pl (id,name, planguage, info)'
            'VALUES (%s,%s, %s, %s)',
           (2,'sagar','Java','Java is a high-level, class-based, object-oriented programming language')
           )
cur.execute('INSERT INTO pl (id,name, planguage, info)'
            'VALUES (%s,%s, %s, %s)',
           (3,'kishor','Go','Go is a statically typed, compiled programming language')
           )
cur.execute('INSERT INTO pl (id,name, planguage, info)'
            'VALUES (%s,%s, %s, %s)',
           (4,'asmit','Dart','Dart is a programming language designed for client development')
           )
cur.execute('INSERT INTO pl (id,name, planguage, info)'
            'VALUES (%s,%s, %s, %s)',
           (5,'nawaraj','Java','Java is a high-level, class-based, object-oriented programming language')
           )


conn.commit()
cur.close()
conn.close()                         