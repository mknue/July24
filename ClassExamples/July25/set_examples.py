


fruit1 = {'apple', 'cherry', 'orange', 'kiwi'}
fruit2 = {'kiwi', 'banana', 'pear', 'fig', 'apple'}

# fruit1.add('plum')
# print(fruit1)

intersection = fruit1 & fruit2
print(intersection)

union = fruit1 | fruit2
print(union)

exclusive_or = fruit1 ^ fruit2
print(exclusive_or)

diff1 = fruit1 - fruit2
print(diff1)

diff2 = fruit2 - fruit1
print(diff2)

f1 = frozenset(diff2)
