# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery = 100  # Private attribute (encapsulation)

    def call(self, number):
        print(f"{self.model} is calling {number}... 📞")
        self.__battery -= 5

    def charge(self):
        self.__battery = 100
        print(f"{self.model} is fully charged 🔋")

    def get_battery_level(self):
        return f"Battery level: {self.__battery}%"

    def show_specs(self):
        print(f"Brand: {self.brand} | Model: {self.model} | Storage: {self.storage}GB")

# Inherited class
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_color):
        super().__init__(brand, model, storage)
        self.strap_color = strap_color

    def show_specs(self):
        super().show_specs()
        print(f"Strap Color: {self.strap_color} 🎨")

    def call(self, number):  # Polymorphism: same method, different behavior
        print(f"{self.model} (Smartwatch) is calling {number} via Bluetooth... 📲")


# Create objects
phone = Smartphone("Samsung", "Galaxy S22", 128)
watch = Smartwatch("Apple", "Watch Series 9", 32, "Red")

# Use the methods
phone.show_specs()
phone.call("0831234567")
print(phone.get_battery_level())
print()

watch.show_specs()
watch.call("0719876543")
print(watch.get_battery_level())

# 2 Assigment 2 

class Animal:
    def move(self):
        pass 


class Dog(Animal):
    def move(self):
        print("Running on four legs 🐕")


class Bird(Animal):
    def move(self):
        print("Flying in the sky 🕊️")


class Fish(Animal):
    def move(self):
        print("Swimming in the water 🐟")


# Create a list of animals
animals = [Dog(), Bird(), Fish()]

# Loop through and call move() (Polymorphism in action!)
for animal in animals:
    animal.move()

