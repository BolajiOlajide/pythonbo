students = []


class Student:

    school_name = "Springfield Elementary"   # Class attribute

    def __init__(self, name, student_id=323):
        self.name = name  # instance attribute
        self.student_id = student_id
        students.append(self)

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

    def __repr__(self):
        return "Student {0}".format(self.name)
