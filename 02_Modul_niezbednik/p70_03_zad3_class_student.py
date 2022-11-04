import csv

class Student:
    def __init__(self, name, surname, school_class, year_of_birth, grade_avg):
        self.name = name
        self.surname = surname
        self.school_class = school_class
        self.year_of_birth = year_of_birth
        self.grade_avg = grade_avg

    @classmethod
    def from_file(cls, file, class_name=None):
        students = []
        with open(file) as students_file:
            for row in csv.reader(students_file):
                if class_name is None or class_name == row[2]:
                    students.append(
                        cls(row[0], row[1], row[2], int(row[3]), float(row[4]))
                    )
        return students

    def __str__(self):
        return f"{[self.name, self.surname, self.school_class, self.year_of_birth, self.grade_avg]}"


john = Student('John', 'Smith', '1A', 2012, 4.78)
jane = Student('Jane', 'Adams', '2C', 2011, 5.11)

print(john)
print(jane)

ob1 = Student.from_file('students.csv')
print(ob1)

ob2 = Student.from_file('students.csv', '2C')
print(ob2)

ob3 = Student.from_file('students.csv', '1A')
print(ob3)

# Pytanie jak odczytać - zapytać