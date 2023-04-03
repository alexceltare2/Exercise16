from person import Person


class Employee(Person):
    numEmployees = 0

    def __init__(self, name, gender, dept, idno):
        super().__init__(name, gender)
        self._dept = dept
        self._id = idno
        Employee.numEmployees = Employee.numEmployees + 1

    def __str__(self):
        return super().__str__() + " Dept: " + self._dept + " ID:" + self._id
