# https://www.hackinscience.org/exercises/student-class

class Student:
    """
    Class representing a student
    """
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_exam(self, grade):
        self.grades.append(grade)
        
    def get_mean(self) -> int:
        return sum(self.grades)/len(self.grades)


class School:
    """
    Class representing a school
    """
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        
    def get_mean(self) -> int:
        return sum(x.get_mean() for x in self.students)/len(self.students)
        
    def get_best_student(self) -> Student:
        return max(self.students, key=lambda x : x.get_mean())
        
class City:
    """
    Class representing a city
    """
    def __init__(self, name):
        self.name = name
        self.schools = []
    
    def add_school(self, school):
        self.schools.append(school)
        
    def get_mean(self) -> int:
        return sum(x.get_mean() for x in self.schools)/len(self.schools)
        
    def get_best_school(self) -> School:
        return max(self.schools, key=lambda x : x.get_mean())
        
    def get_best_student(self) -> Student:
        return max(
            [school.get_best_student() for school in self.schools],
            key=lambda x : x.get_mean()
        )
    
if __name__ == "__main__":
    paris = City('paris')
    hkis = School('hkis')
    paris.add_school(hkis)
    for student_name, student_grades in (('alice', (1, 2, 3)),
                                         ('bob', (2, 3, 4)),
                                         ('catherine', (3, 4, 5)),
                                         ('daniel', (4, 5, 6))):
        student = Student(student_name)
        for grade in student_grades:
            student.add_exam(grade)
        hkis.add_student(student)
    print(paris.get_best_school().name)
    print(paris.get_best_student().name)