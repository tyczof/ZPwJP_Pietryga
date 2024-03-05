class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks) if len(self.marks) > 0 else 0
        return average_marks > 50

# Przykładowe obiekty klasy Student
student1 = Student("Jan Kowalski", [60, 75, 80, 90])
student2 = Student("Anna Nowak", [40, 30, 45, 50])

# Sprawdzenie czy studenci zaliczyli
result1 = student1.is_passed()
result2 = student2.is_passed()

# Wyświetlenie wyników
print(f"{student1.name} zaliczył/a: {result1}")
print(f"{student2.name} zaliczył/a: {result2}")
