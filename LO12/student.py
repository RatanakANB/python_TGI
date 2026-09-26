"""Standalone student module."""

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display_info(self):
        print("Name  :", self.name)
        print("Score :", self.score)

    def get_result(self):
        return "Pass" if self.score >= 50 else "Fail"
