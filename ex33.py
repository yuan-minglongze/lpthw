i = 0
number = []

while i < 6:
    print(f"At the top i is {i}")
    number.append(i)
    
    i += 1
    print("Numbers now: ", number)
    print(f"At the bottom i is {i}")
print("The number: ")
    
for num in number:
    print(num)