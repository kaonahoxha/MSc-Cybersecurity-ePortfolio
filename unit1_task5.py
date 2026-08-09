class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} has been created.")

    def __del__(self):
        print(f"Goodbye, {self.name}!")


person = Person("Kaona")

print("Person's name:", person.name)

del person
