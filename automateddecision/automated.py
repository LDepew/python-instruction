import random

choices = []

for i in range(3):
    i = input("Enter choices: ")
    choices.append(i)
    
print(random.choice(choices))
