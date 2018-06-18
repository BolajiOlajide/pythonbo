from student import Student


class HighSchoolStudent(Student):
    school_name = "Roshallom High"

    # Override
    def get_school_name(self):
        return "This is a high school"

    # Inheritance
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return "{0}-HS".format(original_value)
