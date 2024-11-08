import random

name = str(input("What's your name:  "))
print(f"Good Luck! {name}")
word = 'geeks'
asa = ''
while asa !=word:
    character = input("Guess a character: ")
    print(asa)
    for i in word:
        if character == i:
            asa+=character
        if i in asa:
            print(i)
        else:
            print("_")





print(asa)

#Word guessing game


# def is_fibonacci(n):
#     if n < 0:
#         return False
    
#     a, b = 0, 1
#     while a < n:
#         a, b = b, a + b
    
#     return a == n

# # Example usage
# numbers = [i for i in range(100)]
# for number in numbers:
#     if is_fibonacci(number):
#         print(f"{number} is a Fibonacci number.")





















            

        
