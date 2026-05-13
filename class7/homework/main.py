from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicule):
    def move(self):
        print("The car drive on the road")

class Bycicle(Vehicule):
    def move(self):
        print("The Bycicle Tire is flat")


car = Car()
byke = Bycicle()
car.move()
byke.move()


class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

class TextFilehandler(FileHandler):
    def read(self):
        print("red file")
    def write(self):
        print("written file")

class JsonFilehandler(FileHandler):
    def read(self):
        print("red JSON file")
    def write(self):
        print("written JSON file")

text = TextFilehandler()
json = JsonFilehandler()

text.read()
text.write()

json.read()
json.write()

class Account(ABC):
    @abstractmethod
    def calculate_fee(self):
        pass

class SavingAccount(Account):
    def calculate_fee(self):
        return .05

class PremiumAccount(Account):
    def calculate_fee(self):
        return  .20
    
sav = SavingAccount()
prem = PremiumAccount()

print(sav.calculate_fee())
print(prem.calculate_fee())

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FulltimeEmployee(Employee):
    def __init__ (self, monthly_salary):
       self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary 
    

class PartTimeEmployee(Employee):
    def __init__(self, hours_rate, hours_worked):
        self.hours_rate = hours_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        return self.hour_rate * self. hours_worked
    

class Media(ABC):
    @abstractmethod
    def play(self):
        pass

class Song(Media):
    def Song(self):
        print("Playing the song")
        

class Video(Media):
    def Video(self):
        print("Playing Video")




