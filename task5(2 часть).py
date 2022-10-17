class Student:
    def __init__(self, name, surname, rec_book, grades):
        if not isinstance(name, str):
            raise Exception("Given name isn't a string")
        if not isinstance(surname, str):
            raise Exception("Given surname isn't a string")
        if not isinstance(grades, list) and not isinstance(grades, tuple):
            raise Exception("Grades parameter must be a tuple or list")
        total_grade = 0
        for elem in grades:
            if not isinstance(elem, int):
                raise Exception("Given list contains non integer values")
            total_grade += elem
        if not isinstance(rec_book, str):
            raise Exception("Given record book number isn't a string")
        self._name = name
        self._surname = surname
        self._rec_book = rec_book
        self._grades = list(grades)
        self._average = self.eval_average(total_grade)

    def eval_average(self, total):
        return total/len(self.grades)

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def rec_book(self):
        return self._rec_book

    @property
    def grades(self):
        return self._grades

    @property
    def average(self):
        return self._average

    def add_grade(self, new_grade):
        if not isinstance(new_grade, int):
            raise Exception("Given grade isn't a string")
        self._grades.append(new_grade)
        total = 0
        for grade in self.grades:
            total += grade
        self._average = self.eval_average(total)

    def __str__(self):
        return f"Student №{self.rec_book} - {self.surname} {self.name} has average grade {self.average}"


class Group:
    def __init__(self, list_of_students=None):
        if list_of_students is None:
            list_of_students = []
        if not isinstance(list_of_students, list) and not isinstance(list_of_students, tuple):
            raise Exception("Given list of students isn't a list or tuple")
        if len(list_of_students) > 20:
            raise Exception("Given list of students has capacity more than 20")
        for student in list_of_students:
            if not isinstance(student, Student):
                raise Exception("Every element of list must be an instance of Student class")
        self._list_of_students = list(list_of_students)

    def add_student(self, new_student):
        if not isinstance(new_student, Student):
            raise Exception("Given argument isn't an instance of Student class")
        if len(self._list_of_students) == 20:
            raise Exception("Amount of students cannot be more than 20")
        self._list_of_students.append(new_student)

    def sort_students_list(self):
        self._list_of_students.sort(key=lambda x: x.average, reverse=True)

    def __str__(self):
        self.sort_students_list()
        result = "Top 5 students of the group:\n"
        result += "\n".join(map(str, self._list_of_students[-5:]))
        return result
