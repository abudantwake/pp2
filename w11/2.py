"""
create or replace procedure insert_new_user(name varchar, number varchar)
as $$
begin
	insert into myphonebook(username, phonenumber) values (name, number);	
end;
$$
language plpgsql;
"""

"""
create or replace procedure update_number(name varchar, number varchar)
as $$
begin
	update myphonebook set phonenumber = number where username = name;
end;
$$
language plpgsql;
"""
import psycopg2

username = input()
phonenumber = input()

def insert(name, number):
    global phonenumber
    conn = psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='superuser123'
    )
    sql = """
    SELECT exists(select * from myphonebook where username=%s);
    """
    cur = conn.cursor()
    cur.execute(sql, (name, ))
    result = cur.fetchone()
    
    if result[0]:
        sql = """select phonenumber from myphonebook where username=%s;"""
        cur.execute(sql, (name, ))
        conn.commit()
        numbers = cur.fetchone()
        if number != numbers[0]:
            print('dkfjg')
            cur.execute('call update_number(%s, %s)', (name, number))
            conn.commit()
            cur.close()
    else:
        cur.execute('call insert_new_user(%s, %s)', (name, number))
        conn.commit()
        cur.close()
insert(username, phonenumber)

