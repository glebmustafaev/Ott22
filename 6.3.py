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
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.z += dz * self.speed
        if dz < 0:
            print("It's too deep, i can't dive :(")
        return self._cords

    def get_cords(self):
        print(f"X: {self.x}, Y: {self.y}, Z: {self.z}")
        return self._cords
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        Animal.z=(Animal.z/2)-abs(dz)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird,PoisonousAnimal,AquaticAnimal):
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

db.lay_eggs()

