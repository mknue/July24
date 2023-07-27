

fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig']

# sorted_Fruits = sorted(fruits)
# print(fruits)
# print(sorted_Fruits)

upper_fruits = []
for f in fruits:
    word = f.upper()
    upper_fruits.append(word)


print(upper_fruits)

upper_fruits2 = [f.upper() for f in fruits]
print(upper_fruits2)

upper_fruits3 = (f.upper() for f in fruits)
print(upper_fruits3)
for f2 in upper_fruits3:
    print(f2)