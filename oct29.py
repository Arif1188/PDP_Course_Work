# def example(n):
#     if n == 0:
#         return 0
#     return n%10 + example(n//10)

# print(example(123))





# import psycopg2

# conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password=6636 port='5432'")
# cur = conn.cursor()

# cur.execute("SELECT * FROM employee")

# records = cur.fetchall()
# for i in records:
#     print(i)



# import pandas as pd
# import numpy as np

# # Creating empty series 
# ser = pd.Series() 
# print("Pandas Series: ", ser) 

# # simple array 
# data = np.array(['g', 'e', 'e', 'k', 's']) 
  
# ser = pd.Series(data) 
# print("Pandas Series:\n", ser)

