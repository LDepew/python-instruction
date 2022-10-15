import csv
from cs50 import get_string

name = get_string("Name: ")
number = get_string("Number: ")


#file = open("phonebook.csv", "a") / same as below, but use file.close
with open("phonebook.csv", "a") as file:

    

    writer = csv.writer(file)

    writer.writerow([name, number])

#file.close() / no need to close if using with open
