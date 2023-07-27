

# dictionary = dict()
# dictionary2 = {}

# airports = {'IAD': 'Dulles',
#             'SEA': 'Seattle-Tacoma',
#             'RDU': 'Raleigh-Durham',
#             'LAX': 'Los Angeles'}

# d3 = dict(red=5, blue=10, yellow=1, brown=5, black=12)
#
# pairs = [('Washington', 'Olympia'), ('Virginia', 'Richmond'),
#          ('Oregon', 'Salem'), ('California', 'Sacramento')]
#
# airport = airports.setdefault('SEA', 'No Such Airport')
# print(airport)
# airport2 = airports.setdefault('ORD', 'No Such Airport')
# print(airport2)
#
# for code, city in airports.items():
#     print(f"{code} :: {city}")

counts = {}
with open("../../DATA/breakfast.txt", 'r') as file_in:
    for line in file_in:
        item = line.strip()
        if item not in counts:
            counts[item] = 0

        counts[item] += 1 # counts[item] = counts[item] + 1