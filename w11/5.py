# Implement deleting data from tables by username or phone
"""
create or replace procedure delete_data(name varchar)
as $$
begin
    delete from myphonebook where username = name;
end;
$$
language plpgsql;
"""

import psycopg2

def delete(name):
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='superuser123'
        )
        cur = conn.cursor()
        cur.execute('call delete_data(%s)', (name, ))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
name = input()
delete(name)
