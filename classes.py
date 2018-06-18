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


bolaji = Student('Bolaji')
print(bolaji)

try:
    new_student = Student()
except TypeError:
    print('Something went wrong')

print(students)
print(Student.school_name)
print(bolaji.get_name_capitalize())


class HighSchoolStudent(Student):
    school_name = "Roshallom High"

    # Override
    def get_school_name(self):
        return "This is a high school"

    # Inheritance
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return "{0}-HS".format(original_value)


hstudent = HighSchoolStudent.school_name
print(hstudent)

james = HighSchoolStudent('james')
print(james.get_school_name())
print(james.get_name_capitalize())
