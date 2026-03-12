  -----OOPS IN PYTHON -----------------
# We define a class named Car to represent a car.
class Car:
    # __init__ runs when you create a new Car. It sets up (initializes) the object.
    def __init__(self, make, model, year):
        # Save the 'make' (brand) on the object, e.g., "Toyota".
        self.make = make
        # Save the 'model' on the object, e.g., "Corolla".
        self.model = model
        # Save the manufacturing 'year' on the object, e.g., 2022.
        self.year = year
        # Track whether the car engine is running; start as False (off).
        self.running = False

    # Method to start the car.
    def start(self):
        # Only start if it's not already running.
        if not self.running:
            # Flip running state to True.
            self.running = True
            # Print a friendly message.
            print(f"{self.year} {self.make} {self.model} started.")
        else:
            # If it was already running, say so.
            print(f"{self.year} {self.make} {self.model} is already running.")

    # Method to stop the car.
    def stop(self):
        # Only stop if it's currently running.
        if self.running:
            # Flip running state to False.
            self.running = False
            # Print a friendly message.
            print(f"{self.year} {self.make} {self.model} stopped.")
        else:
            # If it was already stopped, say so.
            print(f"{self.year} {self.make} {self.model} is already stopped.")
# ---------- demo (you can run this) ----------
# Create a Car object with make/model/year values.
my_car = Car("Toyota", "Corolla", 2022)
# Try starting the car.
my_car.start()
# Try starting again to see the "already running" path.
my_car.start()
# Now stop the car.
my_car.stop()
# Stop again to see the "already stopped" path.
my_car.stop()
-------------------------------------------------------------------
  # Base class: a generic Animal.
class Animal:
    # __init__ lets every Animal have a name.
    def __init__(self, name):
        # Store the animal's name.
        self.name = name

    # A common behavior: move. This is the default version.
    def move(self):
        print(f"{self.name} moves around.")

    # A generic speak method (can be overridden by subclasses).
    def speak(self):
        print(f"{self.name} makes a sound.")

# Dog inherits from Animal: it gets name, move, speak by default.
class Dog(Animal):
    # Dogs can override speak to be more specific.
    def speak(self):
        print(f"{self.name} says: Woof!")

    # A behavior specific to dogs.
    def fetch(self, item):
        print(f"{self.name} fetches the {item}.")

# Cat also inherits from Animal.
class Cat(Animal):
    # Cats override speak too.
    def speak(self):
        print(f"{self.name} says: Meow!")

    # A behavior specific to cats.
    def scratch(self):
        print(f"{self.name} scratches the post.")

# ---------- demo ----------
# Create a Dog named "Buddy".
d = Dog("Buddy")
# Create a Cat named "Misty".
c = Cat("Misty")

# Both can move (inherited from Animal).
d.move()
c.move()

# Each has its own speak implementation.
d.speak()
c.speak()

# Use their specific behaviors.
d.fetch("ball")
c.scratch()
------------------------------------------------
# Base class with a method all animals will implement in their own way.
class Animal:
    # make_sound defined here, but base version is generic.
    def make_sound(self):
        print("Some generic animal sound")

# Dog overrides make_sound.
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Cat overrides make_sound.
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Bird overrides make_sound.
class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

# A function that accepts ANY Animal and calls make_sound.
# This shows polymorphism: the SAME call behaves differently

# ---------- demo ----------
# Make one of each animal.
animals = [Dog(), Cat(), Bird()]

# Call the same method on each; each prints its own sound.

for a in animals:
    print(f"an animal can make sound : {a.make_sound()}")
  ---------------------------------------------------------
# A small function to divide two numbers safely.
def safe_divide(a, b):
    # 'try' the risky operation (division).
    try:
        # This line might fail if b is 0.
        result = a / b
        # If it works, print and return the result.
        print(f"{a} / {b} = {result}")
        return result
    # If b is 0, Python raises ZeroDivisionError; we catch it here.
    except ZeroDivisionError:
        # Explain the error nicely.
        print("Error: Cannot divide by zero.")
        # Optionally, return None to indicate failure.
        return None
    except TypeError:
        print("Error: Invalid input types.please provide numbers.")
    except Exception as e:
        print(f"An unexpected error occurred : {e}")

# ---------- demo ----------
safe_divide(10, 2)   # OK
safe_divide(10, 0)   # Triggers the except block
-----------------------------------------------------------
