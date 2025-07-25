import sqlite3
import functools
from datetime import datetime
#### decorator to lof SQL queries
def log_queries(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if 'query' in kwargs:
            print(f"Executing SQL query:{kwargs['query']}")
        elif len(args) > 0:
            print(f"Executing SQL query:{args[0]}")
        else:
            print('No query provided)
        return func(*args, **kwargs)
    return wrapper
        
@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
