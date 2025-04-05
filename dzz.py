class Animal:
    def init(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print("Тварина видає звук")
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Dog(Animal):
    def talk(self):
        print("Гав-гав")
class Cat(Animal):
    def talk(self):
        print("Мяу")
animal = Animal("Невідома", 5)
animal.talk()
animal.info()

dog = Dog("Рекс", 3)
dog.talk()
dog.info()

cat = Cat("Мурчик", 2)
cat.talk()
cat.info()
