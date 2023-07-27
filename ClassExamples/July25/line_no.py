
import sys

files = sys.argv[1:]
for a_file in files:
    with open(a_file, 'r') as file_in:
        for index, line in enumerate(file_in, 1):
            print(f"{index}: {line.strip()}")
    print()