import random

choices = []
n = input("Enter number of choices: ")

for i in range(int(n)):
    i = input("Enter choices: ")
    choices.append(i)
    
print(random.choice(choices))
