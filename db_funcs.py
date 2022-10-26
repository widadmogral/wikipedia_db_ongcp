
import psycopg2
import os
import sys
def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='postgres',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'],
                            port ='5432')
    return conn

def create_table():
    try:
        conn = get_db_connection()
    except Exception as e:
        print(e)
        sys.exit()
    cursor = conn.cursor()
    try:
        cursor.execute( """
        CREATE TABLE IF NOT EXISTS wikipedia(
            keyword_id SERIAL PRIMARY KEY,
            keyword VARCHAR(255) UNIQUE NOT NULL,
            summary VARCHAR,
            img_link VARCHAR
        )
        """)

    except Exception as e:
        print(e)
    conn.commit()
    conn.close()
    cursor.close()

def insert_row(topic, summary,img_link):

    try:
        conn = get_db_connection()
    except Exception as e:
        print(e)
    cursor = conn.cursor()
    try:
        cursor.execute( """
        INSERT INTO wikipedia(
            keyword,
            summary,
            img_link
        ) VALUES(%s,%s,%s)""", (topic,summary,img_link)
                        )

    except Exception as e:
        print(e)
    conn.commit()
    conn.close()
    cursor.close()

def search_db(keyword):
    row_dict = {"title": '', "summary": '', "img_link": ''}
    try:
        conn = get_db_connection()
    except Exception as e:
        print(e)
    cursor = conn.cursor()
    try:
        #cursor.execute("SELECT * from wikipedia")
        cursor.execute("SELECT keyword,summary,img_link from wikipedia WHERE keyword = %s", (keyword,))
        row_dict.update(zip(row_dict, cursor.fetchone()))
    except TypeError as e:
        return None
    conn.commit()
    conn.close()
    cursor.close()
    return row_dict


create_table()
print(search_db("ello"))
#search_db("hello")



