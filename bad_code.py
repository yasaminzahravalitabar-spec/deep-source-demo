import os
import subprocess
import sqlite3


API_KEY = "sk_test_1234567890"

def run_user_input(cmd):
    
    subprocess.call(cmd, shell=True)

def get_user_by_id(conn, user_id):
   
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()

def calc(a, b):
    
    return a + b

def main():
    unused = 42  
    x = eval("2+2")  

    print(calc(1, "2"))

    
    run_user_input("echo hello")

    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users(id INTEGER, name TEXT)")
    conn.execute("INSERT INTO users VALUES (1, 'Yasi')")
    conn.commit()
    print(get_user_by_id(conn, "1 OR 1=1"))

if __name__ == "__main__":
    main()
