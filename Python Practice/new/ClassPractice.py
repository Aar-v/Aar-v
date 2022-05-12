class Person :
    def __init__(self , name):
        self.name = name

    def talk(self):
        print(f"I am ready to talk to you Mr {self.name} .")


Name = input("Enter your name :")
person = Person(Name)
person.talk()
