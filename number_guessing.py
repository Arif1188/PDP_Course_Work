from random import randint
lenth = 0

random_num = randint(1,10)
print(f"Random number: {random_num}")
user = ''
while user != random_num:
    user = int(input("Enter num: "))
    lenth+=1
    if user > random_num:
        print("Man o'ylagan son kichkina edi")
    elif user < random_num:
        print("Man uylagan son katta edi")
    else:
        print(f"Tabriklaymiz siz {lenth} ta urinishda topdingiz")
        
        
        



