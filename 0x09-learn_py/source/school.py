class TooManyStudentsError(Exception):
    pass


class Classroom:
    def __init__(self, teacher, students=None, course_title_title=None):
        self.teacher = teacher
        self.students = []
        self.course_title = ""

    def add_student(self, student):
        if len(self.students) < 20:
            self.students.append(student)
        else: 
            raise TooManyStudentsError()
        
    def remove_student(self, student):
        self.students = [self.students[i] for i in len(self.students) if student != self.students[i]]
    
    def change_teacher(self, new_teacher):
        self.teacher = new_teacher


class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subjects=None):
        super().__init__(name)
        self.subject = []


class Student(Person):
    def __init__(self, name, grade, courses=None):
        super().__init__(name)
        self.grade = grade
        self.courses = []