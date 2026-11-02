class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_no})"

    def __repr__(self):
        return f"Student(name={self.name!r}, roll_no={self.roll_no!r}, marks={self.marks!r})"


s1 = Student("Ali", 1, 85)
s2 = Student("Sara", 2, 92)
s3 = Student("Hamza", 3, 78)

students = [s1, s2, s3]        

print(students)
for student in students:
    print(student)

    