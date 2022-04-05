import psycopg2

hostname='localhost'
database='information'
port_id=5432
username='postgres'
pwd='bibek'

try:
    conn=psycopg2.connect(
              host=hostname,
              dbname=database,
              user=username,
              password=pwd,
              port=port_id)
    cur=conn.cursor()

    cur.execute('drop table if exists employee')

    create_script=''' create table if not exists employee(
                          id  int ,
                          name varchar(30) not null,
                          salary int,
                          dept_id varchar(30))'''
    
    cur.execute(create_script)

    insert_script='insert into employee (id,name,salary,dept_id) values(%s,%s,%s,%s)'
    insert_values=[(1,'Bibek',5000,'D1'),(2,'Sagar',8000,'D2'),(3,'Kishor',10000,'D3')]
    for record in insert_values:
        cur.execute(insert_script,record)

    update_script='update employee set salary=salary+(salary*0.4)'
    cur.execute(update_script)
    
    cur.execute('select*from employee')
    for record in cur.fetchall():
        print(record)
    conn.commit()

except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()



