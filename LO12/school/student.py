"""Student class module."""

class Student:
    institution = "Technical Training Center"

    def __init__(self, student_id, name, course, scores):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.scores = scores

    def display_info(self):
        print("ID     :", self.student_id)
        print("Name   :", self.name)
        print("Course :", self.course)
        print("Scores :", self.scores)

    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def get_result(self):
        return "Pass" if self.get_average() >= 50 else "Fail"

    def update_course(self, new_course):
        self.course = new_course
