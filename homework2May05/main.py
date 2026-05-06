class Book:
    counter = 0 
    def __init__(self):
        Book.counter +=1

b1 = Book()
b2 = Book()
b3 = Book()


print(Book.counter)

class Student:
    school_name = "Vanier College"
    student_count = 0

    def __init__(self, name, program, grade):
        self.name = name
        self.program = program
        self.grade = grade
        Student.student_count += 1

    def display_info(self):
        print(f"{self.name}, studies {self.program}, at {Student.school_name}, with grade {self.grade} ")

s1 = Student("Alice", "Web Dev", 87)
s2 = Student("Mark","Computer Science", 90)
s3 = Student("Ash", "Engeniering", 92)
s4 = Student("San", "Garden", 95)
print(Student.student_count)

s1.display_info()
s2.display_info()
s3.display_info()
s4.display_info()

class Product:
    category = "Electronics"
    tax_rate = 0.15

    def __init__(self, name, price):
         self.name = name
         self.price = price

    def price_with_tax(self):
        return self.price + (self.price * self.tax_rate)
        

p1 = Product("Soap", 8.50)
p2 = Product("Mousse", 7.25)
p3 = Product("Shampoo",10.00)

print(p1.price_with_tax())
print(p2.price_with_tax())
print(p3.price_with_tax())

Product.tax_rate = 0.20

print(p1.price_with_tax())
print(p2.price_with_tax())
print(p3.price_with_tax())


class Employee:
    company_name = "TechNova"
    bonus_rate = 0.10
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count +=1 

    def calculate_bonus(self):
        return self.salary * self.bonus_rate
    
    def display_employee(self):
        print(f"{self.name} works at {self.company_name}. Salary:  {self.salary}. Bonus: {self.calculate_bonus()}"
              )
        
e1 = Employee("Henry", 50)
e2 = Employee("Sean", 35)
e3 = Employee("Laura", 25)

e1.display_employee()
e2.display_employee()
e3.display_employee()

Employee.bonus_rate = 0.20

e1.display_employee()
e2.display_employee()
e3.display_employee()

e1.bonus_rate = 0.50 #e1 (Henry has shadowed bonus_rate of 0.50)
# His instance attribute overrides the class attribute


e1.display_employee()
e2.display_employee()
e3.display_employee()

Employee.bonus_rate = 0.05

e1.display_employee() 
e2.display_employee()
e3.display_employee()#e2 and e3 still use Employee.bonus_rate







         