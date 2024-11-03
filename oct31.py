# res = open("info.txt", 'r')
# print(res.read())
# res.close()


# try: 
#     res = open("info.txt", 'r')
#     print(res.read())
# except FileNotFoundError:
#     print("File not Found")
# finally:
#     res.close()



# def example(string):
#     try:
#         with open('info.txt', 'w') as res:
#             print(res.write(string.upper()))
#     except FileNotFoundError:
#         print("File not found")
        
# example("maestro booooom")
 
 
# def example():
#     for i in range(1,11):
#         yield i
        
# l = example()
# print(next(l),next(l))
# for s in l:
#     print(s)
    

def example():
    for i in range(1,101):
        yield i
        
prime_num = example()
for num in prime_num:
    if num <=1:
        print(f"{num} is not prime")
    elif num >1 and num <=3:
        print(f"{num} is prime")
        for i in range(2,int(num**0.5)+1):
            if num % i==0:
                print(num)