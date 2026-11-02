
# Example of a simple class representing a Book
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title} by {self.author}, Price: Rs.{self.price}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, price={self.price!r})"        



book1 = Book("Uswa-e-Rasool", "Muhammad Nouman", 1500)
print(book1.title)
print(book1.author)
print(book1.price)
print(book1)
print(book1.__dict__)



class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, (Roll No: {self.roll_no}, Marks: {self.marks})"

    def __repr__(self):
        return f"Student(name={self.name!r}, roll_no={self.roll_no!r}, marks={self.marks!r})"
    



s1 = Student("Nouman", 101, 85)
s2 = Student("Usama", 102, 90)
s3 = Student("Shanzy", 103, 95)
print(s1)
print(s2)
print(s3)

students = [s1, s2, s3]
print(students)
for student in students:
    print(student)