class Animal :
    age = 5
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        self.is_alive =True
        print(f"{self.name} are {self.weight}kg.")
    def eat(self):
        print(f"{self.name} are eating their food.")

    def sleep(self):
        print(f"{self.name} are sleeping.")

class Dog(Animal):
    def sound(self):
        print("Woof")

class Cat(Animal):
    def sounds(self):
        print("Meow")

class friend(Dog,Cat):
    def is_friend(self):
        print(f"Me and {self.name} are friend.")
print(f"They all are {Animal.age} years old.")

dog1 = Dog("David","10")
dog2 = Dog("Victor","8")
cat1 = Cat("Cinn","3")
cat2 = friend("Linn","5")

dog1.eat()
dog2.sleep()
dog1.sound()
cat2.is_friend()
cat2.sounds()