"""
create or replace function querying_data(num integer, numm integer) 
returns TABLE(id integer, username varchar, phonenumber varchar) as
$$
begin 
    return query
    select * from myphonebook limit num offset numm;
end;
$$
language plpgsql;
"""

import psycopg2

def pagination(num, numm):
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='superuser123'
        )
        cur = conn.cursor()
        cur.callproc('querying_data', (num, numm))
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
num = int(input())
numm = int(input())
pagination(num, numm)