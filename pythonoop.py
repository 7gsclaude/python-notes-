class Vehicle():

    def __init__(self, vin, make, model) -> None:
        self.vin = vin
        self.make = make
        self.model = model
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def __str__(self) -> str:
        return f'Vehicle ({self.vin}) is a {self.make} model {self.model}!'


car = Vehicle('TS123', 'Tesla', 'Model S')

car.start()

print(car)
# def __str__(self) => str:
#     return(f"viheicle {start}")
# nums = [1,2,3]

# print (dir(nums)) shows all memebers available to me 

class dog(): #class is typically written as a capitol
    pass

class Dog(): 
    def bark():
        "how how"

next_id = 1 
# this exists outside of the instance 

dog = Dog() 
type(dog)

# this shows the class type 

# dog.bark()

class Dog():
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
        self.id = Dog.next_id
        Dog.next_id += 1
        #when a dog is created it will create a new instance of a dog 
    def bark(self):
        print(f'{self.name} says How how')
    def __str__(self) -> str:
        return f'Vehicle ({self.vin}) is a {self.make} model {self.model}!'
    
    @classmethod 
    def get_total_dogs(cls):
        return cls.next_id-1
# subtracting 1 because the last thing was incrememtned 

# in js we learned about this 
# in pyhton only by convention its called self 

ayans_dog = Dog('zazu', '4 years')
# print(ayans_dog.bark())
# print(ayans_dog)

claudes_dog = Dog('Lina', '12 years')

mickeys_dog = Dog('rogi',2, 'likes to dig')
# print(mickeys_dog.name, mickeys_dog.age)

reinys_dog = Dog('Pawter', 7)
# print (reiny_dog.name, reiny_dog.age)

id(parents_dog.bark)
# this equals the memory id and the print . 

class Sake():
    def __inint__(self):
        pass 

    claude_dog = Dog('zoe',6)
    # building instances of certain dogs 
# this is an ungly output
# <__main__.Dog object at 0x10390bd60 >
# so the dog class was be modified 
# what the dog class is doing is bindind things together

class ShowDog(Dog):
    def __init__(self,name,age = 0, total_earnings = 0):
        Dog.__init__(self,name,age)
        self.total_earnings = total_earnings

    def add_prize_money(self, amount):
        self.total_earnings += amount