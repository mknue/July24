
from pprint import pprint
# fruit = ["pomegranate  ", "  cherry", "  apricot  ", "date", "Apple", "lemon", "Kiwi",
#          "ORANGE", "lime", "Watermelon", "guava", "  papaya  ", "FIG", "pear", "banana",
#          "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
#          "grape"]

# def normalize_strings(word):
#     return (len(word), word.lower().strip())
#
# # lambda <parameters>: <expression>
# fruit1 = sorted(fruit, key=lambda word:((len(word), word.lower().strip())))
# print(fruit1)
# print()
# print(fruit)

# people = [
#     ('Melinda', 'Gates', 'Gates Foundation'),
#     ('Steve', 'Jobs', 'Apple'),
#     ('Larry', 'Wall', 'Perl'),
#     ('Paul', 'Allen', 'Microsoft'),
#     ('Larry', 'Ellison', 'Oracle'),
#     ('Bill', 'Gates', 'Microsoft'),
#     ('Mark', 'Zuckerberg', 'Facebook'),
#     ('Sergey', 'Brin', 'Google'),
#     ('Larry', 'Page', 'Google'),
#     ('Linus', 'Torvalds', 'Linux'),
# ]
#
# sorted_people = sorted(people, key=lambda p:(p[1], p[0]))
# pprint(sorted_people)
#
# airports = {'IAD': 'Dulles', 'SEA': 'Seattle-Tacoma',
#             'RDU': 'Raleigh-Durham', 'LAX': 'Los Angeles', 'ORD': 'Chicago OHare'}
#
# sorted_airports = sorted(airports.items(), key=lambda a:a[1], reverse=True)
# print(sorted_airports)

fruits = ['apple', 'Cherry', 'orange', 'KIWI', 'banana', 'pear', 'fig']
fruits.sort(key=str.lower)
fruits.reverse()
print(fruits)