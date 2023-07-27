
from temp_conv import c2f
# import temp_conv

c_str = input("Enter the temperature in Celsius: ")
f = c2f(c_str)
# f = temp_conv.c2f(c_str)
print(f"{c_str}C is {f}F")