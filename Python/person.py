class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
            print(f"Hi, my name is {self.name}. I am {self.age} years young and I identify as {self.gender}.")


person1 = Person("Caesar", 15, "male")
person1.introduce()
