

with open("../../DATA/alt.txt", 'r') as file_in:
    with open("a.txt", 'w') as a_out:
        with open("b.txt", 'w') as b_out:
            for word in file_in:
                if word[0] == 'a':
                    a_out.write(word)
                elif word[0] == 'b':
                    b_out.write(word)