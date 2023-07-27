

x = 5
y = 10

try:
    z = x + y
    # print("Total:", z)
except (TypeError, IOError) as err:
    # pass
    print(err.args)
    print("Invalid values to add...")
    quit(123)
else:
    print("Total:", z)

finally:
    print("Finally!")
print("END")