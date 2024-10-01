import pytest
from service.school import Classroom, Teacher, Student, TooManyStudentsError  # replace 'your_module' with the actual module name

@pytest.fixture
def setup_classroom():
    teacher = Teacher(name="Kaka Sungura")
    classroom = Classroom(teacher=teacher)
    return classroom

@pytest.fixture
def students():
    return [Student(name=f"Student {i}", grade=i) for i in range(1, 25)]  # 24 students

def test_add_student(setup_classroom):
    classroom = setup_classroom
    student = Student(name="Kaka Dubu", grade=10)
    
    classroom.add_student(student)
    
    assert student in classroom.students
    assert len(classroom.students) == 1

def test_add_student_max_limit(setup_classroom, students):
    classroom = setup_classroom
    
    # Add 20 students to reach the limit
    for student in students[:20]:
        classroom.add_student(student)
    
    # Ensure adding one more student raises TooManyStudentsError
    with pytest.raises(TooManyStudentsError):
        classroom.add_student(students[20])

def test_remove_student(setup_classroom):
    classroom = setup_classroom
    student1 = Student(name="Bi Buibui", grade=1)
    student2 = Student(name="Kaka Tai", grade=2)
    
    classroom.add_student(student1)
    classroom.add_student(student2)
    
    classroom.remove_student(student1)
    
    assert student1 not in classroom.students
    assert student2 in classroom.students

def test_change_teacher(setup_classroom):
    classroom = setup_classroom
    new_teacher = Teacher(name="Paka the Cat")
    
    classroom.change_teacher(new_teacher)
    
    assert classroom.teacher == new_teacher

@pytest.mark.parametrize("course_title", ["Maths 101", "History 202", "Science 303"])
def test_course_title(setup_classroom, course_title):
    classroom = setup_classroom
    classroom.course_title = course_title
    assert classroom.course_title == course_title

def test_remove_student_not_found(setup_classroom):
    classroom = setup_classroom
    student = Student(name="Mzee Kobe", grade=99)
    
    # Test removing a student not in the classroom
    classroom.remove_student(student)
    
    assert student not in classroom
    
def test_person_initialization():
    person = Person(name="Kaka Mbweha")
    assert person.name == "Kaka Mbweha"

def test_teacher_initialization():
    teacher = Teacher(name="Kaka Mbwamwitu")
    assert teacher.name == "Kaka Mbwamwitu"
    assert teacher.subject == []

def test_student_initialization():
    student = Student(name="Goat Matata", grade=10)
    assert student.name == "Goat Matata"
    assert student.grade == 10
    assert student.courses == []

