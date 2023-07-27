
class Person:
    _numberOfPeople = 0

    # first name, last name
    def __init__(self, firstName, lastName):
        self._firstName = firstName
        self._lastName = lastName
        Person._numberOfPeople += 1
        # print("Person created!")

    def get_full_name(self):
        return ("{} {}").format(self._firstName, self._lastName)


    @property
    def firstName(self):
        return self._firstName.title()

    @firstName.setter
    def firstName(self, firstName):
        self._firstName = firstName

    @classmethod
    def getNumberOfPeople(cls):
        return cls._numberOfPeople


if __name__ == "__main__":
    p1 = Person("Sven", "Reindeer")
    firstName = p1.firstName
    print(firstName)
    p1.firstName = "daisy"
    print(p1.firstName)

    p2 = Person("Olaf", "Snowman")
    print(p2.get_full_name())

    print(f"Number of people: {Person.getNumberOfPeople()}")