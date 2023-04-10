import sys


class Person:
    def __init__(self, name, gender):
        if gender not in {"m", "f"}:
            raise ValueError("Invalid gender choice!")
        self._name = name
        self._gender = gender.upper()

    def __str__(self):
        return "Name: " + self._name + " Gender: " + self._gender
