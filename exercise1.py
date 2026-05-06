class Friend:
    
    def __init__(self, name, surname, age, sport, origins):
        self.name = name
        self.her_surname = surname 
        self.full_identity = name + " " + surname
        self.the_age = age
        self.sport = sport
        self.origins = origins
    def print_info(self):
        print(self.name, self.surname, self.age, self.sport, self.origins)

    def greet(self):
        print("Hello my friend" + self.name + "we call you " + self.her_surname)


friend1 =  Friend("laura", "Lau", 22, "tennis", "Europe")
friend2 =  Friend("Paul", "Polo", 25, "basket", "Asia")
friend3 =  Friend("Regie", "Reg", 19, "soccer", "Africa")

print(friend1.name)

print(friend2.the_age)

print(friend3.sport)

friend1.greet()
friend2.greet()
friend3.greet()