

value = 5

def double():
    global value
    value = 10
    print(value)


print(value)
double()
print(value)