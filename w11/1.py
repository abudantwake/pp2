"""
create or replace function get_by_pattern(user_id integer)
returns TABLE(id integer, username varchar, phonenumber varchar) as
$$
begin
	return query
	select myphonebook.id, myphonebook.username, myphonebook.phonenumber from myphonebook where myphonebook.id=id;
end;
$$
language plpgsql;
"""

import psycopg2

def get_by(id):
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='superuser123'
        )
        cur = conn.cursor()
        cur.callproc('get_by_pattern', (id, ))
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
id = int(input())
get_by(id)
