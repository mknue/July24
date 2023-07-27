

while True:
    c_str = input("Enter the temperature in Celsius: ")
    if c_str == "":
        continue
    elif c_str == 'q' or c_str =='Q': # c_str.casefold() == 'q'
        break
    else:
        c = float(c_str)
        f = ((9*c)/5)+32
        print(f"{c}C is {f}F")

print("You have exited the temperature converter...")