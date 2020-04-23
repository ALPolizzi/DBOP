
# coding: utf-8

# In[1]:


import sys
get_ipython().system('{sys.executable} -m pip install psycopg2')
import psycopg2


def create_tables():
    
    commands = (
        """
        CREATE TABLE x (
            xx PRIMARY KEY,
            yy VARCHAR(255) NOT NULL
        )
        """)
    
    conn = None
    
    try:
        # connect to PostgreSQL
        conn = psycopg2.connect(host="localhost",database="testdb", user="postgres", password="postgres")
        cur = conn.cursor()
        
        # create each table
        for command in commands:
            cur.execute(command)
            
        cur.close()
        conn.commit()
        
    #Handle exceptions    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    #Ensure closed
    finally:
        if conn is not None:
            conn.close()

            
def get_something():
    conn = None
    try:
        conn = psycopg2.connect(host="localhost",database="testdb", user="postgres", password="postgres")
        cur = conn.cursor()
        
        
        cur.execute("SELECT ...")
        
        
        print("The number of rows: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
def insert_X(Y):
"""Insert attribute Y into table X and return row"""
    sql = """INSERT INTO X(Y)
             VALUES(%s) RETURNING Z;"""
    conn = None
    Z = None
    try:
        conn = psycopg2.connect(host="localhost",database="testdb", user="postgres", password="postgres")
        cur = conn.cursor()
        
        
        cur.execute(sql, (Y,))
        
        Z = cur.fetchone()
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return Z
            
if __name__ == '__main__':
    create_tables()

