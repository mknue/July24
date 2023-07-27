

shells = {}
with open("../../DATA/passwd", 'r') as file_in:
    for line in file_in:
        # line2 = line.strip().split(":")
        # shell = line2[-1]
        # shell = line.strip().split(":")[-1]
        *_, shell = line.strip().split(":")
        if shell == '':
            shell = 'NONE'

        if shell in shells:
            shells[shell] += 1
        else:
            shells[shell] = 1

for s, c in shells.items():
    print(f"{s} - {c}")