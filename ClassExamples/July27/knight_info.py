

from knight import Knight
import sys

names = sys.argv[1:]
for name in names:
    k = Knight(name)
    print(f"Name: {k.title} {k.name}")
    print(f"Favorite Color: {k.favorite_color}")
    print(f"Quest: {k.quest}")
    print(f"Comment: {k.comment}")