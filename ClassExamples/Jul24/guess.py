

max_value = 26
min_value = 0

while True:
    guess = (max_value + min_value)//2
    successful = input(f"Was your guess {guess}?")
    if successful.casefold() == 'l':
        min_value = guess
        continue
    elif successful.casefold() == 'h':
        max_value = guess
        continue
    elif successful.casefold() == 'y':
        print(f"Congrats! The guess was {guess}")
        break

    print("Please enter only l, h, or y")


