
import re

s = """lorem ipsum M302 dolor sit amet, consectetur r99 adipiscing elit, sed do
 eiusmod tempor incididunt H476 ut labore et dolore magna Q51 aliqua. Ut enim 
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex  
ea commodo z883  consequat. Duis aute irure dolor in reprehenderit in
voluptate velit esse cillum dolore U901 eu fugiat nulla pariatur. 
Excepteur sint occaecat A110 cupidatat non proident, sunt in H332 culpa qui 
officia deserunt Y45 mollit anim id est laborum"""

pattern = r"(?P<code>[a-z])(?P<id>\d{2,3})"
regex = re.compile(pattern, re.I)

def update(match):
    letter = match.group("code")
    id = match.group('id')
    return f'{letter.upper()}-{id}'

new_text = regex.sub(update, s)
print(new_text)
# print(f"{count} changes made")

# m = re.search(regex, s)
# print(m.group())
# print(m.group(0))
# print(m.group(1))
# print(m.group("code"))
# print(m.group(2))
# print(m.group("id"))


# for match in re.finditer(pattern, s):
#     print(match)
# print()
#
# matches = re.findall(pattern, s)
# print(matches)

x = r'\d(?st|nd|rd|th)(?=street)'