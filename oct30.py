# def func_decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
        
#     return wrapper

# @func_decorator
# def some_func():
#     print("This is python")
    
# some_func() 
    
# # res = func_decorator(some_func)
# # res()


# import time

# def time_decorator(func):
#     def wrapper():
#         start_time = time.time()
#         print(f"This is start time: {start_time}")
#         func()
#         end_time = time.time()
#         print(f"This is end time: {(end_time - start_time):.8f} seconds")
#     return wrapper

# @time_decorator
# def example():
#     for i in range(5):
#         print(i)
        
# example()


# import psycopg2

# conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password=6636 port='5432'")
# cur = conn.cursor()
# insert_sql = ("INSERT INTO employee (first_name, last_name, email, gender, date_of_birth, country_of_birth, position)"
#               "VALUES (%s,%s,%s,%s,%s,%s,%s)")

# # cur.execute("SELECT * FROM employee")
# cur.execute(insert_sql, ("Orifjon", "Nabiyev", "Salombek@.gmail.com", "Male", "2016-11-11", "Uzbekistan", "Student"))
# conn.commit()
# cur.close()
# conn.close()

import pandas as pd

df = pd.read_csv("MOCK_DATA.csv")
print(df)