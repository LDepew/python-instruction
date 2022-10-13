from cs50 import get_int

MINE = 2
points = get_int("How many points did you lose? ")

if points < MINE:
    print("You lost fewer points than me.")
elif points > MINE:
    print("You lost more points than me.")
else:
    print("You lost the same number of points as me.")