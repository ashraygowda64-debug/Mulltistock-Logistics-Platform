import sqlite3
import os

db_path = 'db.sqlite3'
if not os.path.exists(db_path):
    print(f"Database file {db_path} not found!")
else:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    tables = [
        'permissions_accesslog',
        'permissions_permission',
        'permissions_rolepermission',
        'permissions_userpermissionoverride',
        'user_roles',
        'permissions_userrole'
    ]
    
    for table in tables:
        try:
            cursor.execute(f"DROP TABLE IF EXISTS {table};")
            print(f"Dropped table '{table}'")
        except Exception as e:
            print(f"Error dropping table '{table}': {e}")
            
    conn.commit()
    conn.close()
