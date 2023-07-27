

name = "Kaylee"
salary = 20000

print(name, " makes $", salary, sep='' , end='. ')
print()
# print(name, " makes $", salary)

pattern = "{:>10s} makes ${:.2f}"
print(pattern.format(name, salary))

print(f"{name:<10s} makse ${salary:,.2f}")