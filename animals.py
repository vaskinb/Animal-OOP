class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._heart_beat = "normal"

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def _set_heart_beat(self, beat):
        self._heart_beat = beat


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def description(self):
        return "{} - {}, {} years old".format(self.name, self.breed, self.age)

    def move(self, speed):
        if speed > 10:
            self._set_heart_beat("fast")
        else:
            self._set_heart_beat("slowly")
        return "{} runs {} km/h, heartbeat {}".format(self.name, speed, self._heart_beat)


class Parrot(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def move(self, speed):
        return "{} fly {} km/h".format(self.name, speed)

    def speak(self, sound):
        return "{} says {}, kar".format(self.name, sound)


if __name__ == '__main__':
    Rex = Dog("Rex", 12, "mammal")
    Ricky = Parrot("Ricky", 10, "bird")
    for animal in (Rex, Ricky):
        print(animal.description())
        print(animal.move(15))
        print(animal.speak("hello"))
