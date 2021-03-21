class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display(self):
        print(self.__fields_to_string__())

    def __fields_to_string__(self):
        return "{};{};{}".format(self.first_name, self.last_name, self.age)


class Professor(Person):
    degree = 0
    count = 0

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.professor_ID = Professor.count
        self.degree = Professor.degree

    def __fields_to_string__(self):
        return super().__fields_to_string__() + ";{}".format(self.professor_ID, self.degree)



class Student(Person):
    count = 0

    def __init__(self, first_name, last_name, age, record_book):
        super().__init__(first_name, last_name, age)
        self.student_ID = Student.count
        self.record_book = record_book
        Student.count += 1

    def __fields_to_string__(self):
        return super().__fields_to_string__() + ";{};{}".format(self.student_ID, self.record_book)

    professors = {
        Professor("Name1", "LastName1", 51,),
        Professor("Name2", "LastName2", 32),
        Professor("Name3", "LastName3", 47)
    }

    for professor in professors:
        professor.display(),


students = {
    Student("Name1", "LastName1", 18, "book1"),
    Student("Name2", "LastName2", 19, "book2"),
    Student("Name3", "LastName3", 17, "book3")
}


for student in students:
    student.display()

