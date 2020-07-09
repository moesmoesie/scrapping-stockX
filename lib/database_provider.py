import sqlite3
from models.shoe import Shoe
from models.shoe import Shoe
import queries as queries

class DatabaseProvider:
    def __init__(self,name = "stockx_database_jordans.db"):
        self.name = name
        self.conn = self.connect_database()
        self.create_table(queries.create_shoes_table)
        self.create_table(queries.create_sales_table)

    def __del__(self):
        print("Database is closed!")
        self.conn.close()

    def connect_database(self):
        conn = None
        try:
            conn = sqlite3.connect(self.name)
            return conn
        except sqlite3.Error as e:
            print(e)

    def insert_values(self,sql,values):
        try:
            cur = self.conn.cursor()
            cur.execute(sql,values)
            self.conn.commit()
            cur.close()
            return True
        except sqlite3.IntegrityError:
            return False
            # print(f"This item already exists --------- {values[0]}")
        except sqlite3.Error as e:
            print(e)     
        
        return False
    
    def get_values(self,sql):
        try:
            cur = self.conn.cursor()
            result = cur.execute(sql)
            values = result.fetchall()
            return values
        except sqlite3.Error as e:
            print(e)

    def create_table(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            cur.close()
        except sqlite3.Error as e:
            print(e)