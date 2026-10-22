import sqlite3
import os

db_path = 'db.sqlite3'
if not os.path.exists(db_path):
    print(f"Database file {db_path} not found!")
else:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    tables = ['user_roles', 'permissions_userrole']
    for table in tables:
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}';")
        result = cursor.fetchone()
        if result:
            print(f"Table '{table}' EXISTS")
        else:
            print(f"Table '{table}' DOES NOT EXIST")
            
    conn.close()
