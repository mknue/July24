

class Knight:

    def __init__(self, name):
        with open("../../DATA/knights.txt") as file_in:
            for line in file_in:
                knight = line.split(":")
                if name == knight[0]:
                    self._name = knight[0]
                    self._title = knight[1]
                    self._color = knight[2]
                    self._quest = knight[3]
                    self._comment = knight[4]
                    break

    @property
    def name(self):
        return self._name

    @property
    def title(self):
        return self._title

    @property
    def favorite_color(self):
        return self._color

    @property
    def quest(self):
        return self._quest

    @property
    def comment(self):
        return self._comment

