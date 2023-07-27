

# list1 = list()
# list2 = []
# fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig']

# tuple1 = tuple()
# tuple2 = ()
# fruits = 'apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig'
# print(fruits)
#
# person = 'John', 'Dough', 'Unknown Company'
#
# today = 24, "July", 2023, 'AD'
#
# print(f"{today[1]} {today[0]}, {today[2]}")
#
# day, month, year = today
# print(f"{month} {day}, {year}")

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]


#for person in people:
for first, last, org in people:
    # first, last, org = person
    print(f"{last}, {first} -- {org}")
    line = '-' * 20
    print(line)