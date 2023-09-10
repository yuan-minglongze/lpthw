def main(top, step):
    i = 0
    number = []
    
    
    while i < top:
        print(f"At the top i is {i}")
        number.append(i)
        
        i += step
        print("Number now: ", number)
        print(f"At the bottom i is {i}")
    print("The number: ")
    
    for num in number:
        print(num)

main(int(input("> ")),int(input("> ")))

'''
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
'''