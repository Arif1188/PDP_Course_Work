# n = [2 7 1 5 4 17 6 3 8]
# eng kichigini va eng kattasini toping


n = [2, 7, 1, 5, 4, 17, 6, 3, 8,]

smallest_number = n[0]
biggest_number = n[-1]
for num in n[1:]:
    if num < smallest_number:
        smallest_number = num

for num2 in n[1:]:
    if num2 > biggest_number:
        biggest_number = num2

print(f"Smallest number = {smallest_number}\n"
      f"Biggest number = {biggest_number}")