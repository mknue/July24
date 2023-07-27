

with open("../../DATA/alice.txt", 'r', encoding='excel') as file_in:
    counter = 0
    for line in file_in:
        if 'Alice' in line:
            counter += 1

print(f"Alice is in {counter} lines.")
