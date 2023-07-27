

students = {}
with open("../../DATA/testscores.dat", 'r') as file_in:
    for line in file_in:
        name, score = line.strip().split(":")
        students[name] = int(score)

for name, score in sorted(students.items(), key=lambda e: e[1], reverse=True):
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 75:
        grade = 'D'
    else:
        grade = 'F'

    print(f"{name:20s} {score} {grade}")

score_list = students.values()
total = sum(score_list)
average = total/len(score_list)

print(f"Average Score: {average}")