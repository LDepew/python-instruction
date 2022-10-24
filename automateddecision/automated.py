import random

choices = []
while True:
    try:
        n = input("Enter number of choices: ")
        n = n(int)

        if n < 2:
            print("Not enough choices")

    except:
        continue
        break
        

for i in range(n):
    i = input("Enter choices: ")
    choices.append(i)
    
print(random.choice(choices))
