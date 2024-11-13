import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    x = 0
    y = 0
    z = 0
    _cords = [x, y, z]

    def __init__(self, speed):

        self.speed = speed

    def speak(self):
        print(self.sound)

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        if dz < 0:
            print("It's too deep, i can't dive :(")
        return self._cords

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


def lay_eggs():
    print(f"Here are(is) {random.randint(1, 4)} eggs for you")


class Bird(Animal):
    beak = True


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        Animal.z=(Animal.z/2)-abs(dz)



class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

lay_eggs()

