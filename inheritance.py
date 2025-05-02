
#Vehicle bus inheritance
class Vehicle():
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12)

print("Vehicle Name:", school_bus.name, "Speed:", school_bus.max_speed, "Mileage:", school_bus.mileage)



#person Employee inheritance
class Person(object):
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print(self.name)
        print(self.id_number)

class Employee(Person):
    def __init__(self, name, id_number, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, id_number)

a = Employee('Rahul', 886012, 200000, "Intern")
a.display()



#Bird Penguin inheritance
class Bird():
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run faster")

p1 = Penguin()
p1.whoisThis()
p1.swim()
p1.run()



