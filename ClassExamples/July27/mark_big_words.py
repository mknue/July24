import re


def star_words(match):
    word = match.group()
    return ("***{}***").format(word)

with open("../../DATA/parrot.txt", 'r') as file_in:
    parrot = file_in.read()

pattern = r"\b[a-z]{8,}\b"
regex = re.compile(pattern, re.I)
new_text = regex.sub(star_words, parrot)

with open("bigwords.txt", 'w') as file_out:
    file_out.write(new_text)
