import re

pattern = r'\b(\d{3}-)?(\d{3}\-\d{4})\b'

with open("../../DATA/custinfo.dat", 'r') as file_in:
    for line in file_in:
        if re.search(pattern, line):
            print(line)