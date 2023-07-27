

with open("../../DATA/parrot.txt", 'r') as file_in:
    with open("parrot_copy.txt", 'w') as file_out:
        for index, line in enumerate(file_in, 1):
            file_out.write(f"{index}: {line}")

with open("../../DATA/tyger.txt", 'r') as file_in:
    text = file_in.readlines()

with open("tyger_copy.txt", 'w') as file_out:
    file_out.writelines(text)
