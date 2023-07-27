

fruit_list = []
with open("../../DATA/fruit.txt", 'r') as file_in:
    for line in file_in:
        fruit_list.append(line.strip())

# fruit_list = [line.strip() for line in file_in]

# fruit1 = sorted(fruit_list)
# print(fruit1)

fruit_list.sort()
print(fruit_list)

fruit_list.sort(key=str.lower)
print(fruit_list)

fruit_list.sort(key=lambda e:(len(e), e.lower()))
print(fruit_list)

fruit_list.sort(key=lambda e:(e[1].lower(), e[0].lower()))
print(fruit_list)