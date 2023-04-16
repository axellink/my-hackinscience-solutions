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