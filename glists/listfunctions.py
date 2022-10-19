lucky_numbers = [42, 8, 15, 16, 23, 4]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)

friends.insert(3, "Jim")
print(friends.count("Jim"))
friends.remove("Jim")

friends.sort()
print(friends)

friends.append("Creed")
friends.extend(lucky_numbers)
friends.insert(1, "Kelly")
friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kevin"))

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)