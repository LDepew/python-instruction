from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

z = x / y
#z = x // y (division without truncation, returns whole number)

print(f"{z:.50f}")