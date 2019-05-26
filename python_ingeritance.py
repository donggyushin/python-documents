class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print('move')

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print('bark')


class Duck(Animal):
    def speak(self):
        print('quack')


if __name__ == '__main__':
    deabak = Dog('daebak')
    sixduck = Duck('sixduck')
    print('daebak\'s name:', deabak.name)
    print('daebak: ')
    deabak.speak()
    print('sixduck\'s name: ', sixduck.name)
    print('sixduck: ')
    sixduck.speak()
    deabak.move()
    sixduck.move()
