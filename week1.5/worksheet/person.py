# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        """
        Create a person with a name and date of birth.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if name == "":
            raise ValueError("Name cannot be empty")

        if not isinstance(birth, date):
            raise TypeError("Birth must be a date object")

        self.name = name
        self.birth = birth

    def initials(self):
        """
        Return the initials of the person's name.
        """
        words = self.name.split()
        result = ""

        for word in words:
            result += word[0].upper()

        return result

    def is_birthday(self):
        """
        Check if today is the person's birthday.
        """
        today = date.today()

        return (self.birth.day == today.day and self.birth.month == today.month)

 
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
