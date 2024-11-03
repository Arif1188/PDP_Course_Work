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
    

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) +1):
        print(i, 'is i')
        print(n, 'is n')
        if n % i == 0:
            return False
    return True

# Example usage
numbers = [k for k in range(1, 11)]
for number in numbers:
    if is_prime(number):
        print(f"{number} is a prime number.")