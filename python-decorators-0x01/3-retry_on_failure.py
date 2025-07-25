import sqlite3
import time
import functools

def with_db_connection(func)
 @functools.wraps(func)
 def wrapper(*args, **kwargs)
   conn = sqlite3.connect(user.db)
   try:
     result = func(conn, *args, **kwargs)
     return result
   finally:
    conn.close()
  return wrapper

def retry_on_failure(retries=3, delay=2)
 def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, retries + 1):
                try:
                    print(f"Attempt {attempt}...")
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    last_exception = e
                    time.sleep(delay)
            print("All retry attempts failed.")
            raise last_exception
        return wrapper
    return decorator

 @with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)
   
 
