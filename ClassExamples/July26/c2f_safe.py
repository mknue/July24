

c_str = input("Enter the temperature in Celsius: ")
try:
    c = float(c_str)
    # f = ((9*c)/5)+32
    # print(f"{c}C is {f}F")
except ValueError as err:
    print("Please enter only valid numbers.")
else:
    f = ((9*c)/5)+32
    print(f"{c}C is {f}F")