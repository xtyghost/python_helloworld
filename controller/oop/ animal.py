class Animal(object):
    def run(self):
        print('Animal is running')

    def list(self):
        print("test")


k = Animal()
k.run()


class Dog(Animal):
    def run(self):
        print("%s is running..." % 'dog')


class Cat(Animal):
    def run(self):
        print("%s is running..." % 'cat')


cat = Cat()
dog = Dog()

cat.run()
dog.run()
