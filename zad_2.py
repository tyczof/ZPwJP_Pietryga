class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.city}, {self.street}, {self.zip_code}\n" \
               f"Open hours: {self.open_hours}\n" \
               f"Phone: {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\n" \
               f"Hire date: {self.hire_date}\n" \
               f"Birth date: {self.birth_date}\n" \
               f"Address: {self.city}, {self.street}"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\n" \
               f"Published: {self.publication_date}\n" \
               f"Pages: {self.number_of_pages}\n" \
               f"Library: {self.library}"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f"Order by {self.employee.first_name} {self.employee.last_name}\n" \
               f"Student: {self.student.name}\n" \
               f"Order date: {self.order_date}\n" \
               f"Books: \n{', '.join([str(book) for book in self.books])}"


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks) if len(self.marks) > 0 else 0
        return average_marks > 50



# Tworzenie instancji klas
library1 = Library("City1", "Street1", "12345", "9:00 AM - 5:00 PM", "123-456-789")
library2 = Library("City2", "Street2", "67890", "10:00 AM - 6:00 PM", "987-654-321")

employee1 = Employee("John", "Doe", "2022-01-01", "1990-05-15", "City1", "Street1")
employee2 = Employee("Jane", "Smith", "2022-02-01", "1985-08-20", "City2", "Street2")
employee3 = Employee("Bob", "Johnson", "2022-03-01", "1995-03-10", "City1", "Street1")

book1 = Book(library1, "2021-01-01", "Author1", "Surname1", 200)
book2 = Book(library1, "2022-02-01", "Author2", "Surname2", 250)
book3 = Book(library2, "2020-05-15", "Author3", "Surname3", 180)
book4 = Book(library2, "2019-08-20", "Author4", "Surname4", 300)
book5 = Book(library2, "2023-03-10", "Author5", "Surname5", 150)

student1 = Student("Jan Kowalski", [60, 75, 80, 90])
student2 = Student("Anna Nowak", [40, 30, 45, 50])
student3 = Student("Mark Smith", [40, 30, 45, 50])

order1 = Order(employee1, student1, [book1, book2, book3], "2023-03-05")
order2 = Order(employee2, student2, [book4, book5], "2023-03-05")

# Wyświetlanie zamówień
print(order1)
print("\n-------------------------\n")
print(order2)
