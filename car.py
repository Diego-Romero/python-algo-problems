
class Car:
    def __init__(self, speed = 0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def say_state(self):
        print("im going at ")



if __name__ == '__main__':

    my_car = Car()

    print("im a car")

    my_car.accelerate()
    my_car.accelerate()
    my_car.accelerate()

    print("the car has driven {} km ".format(my_car.speed))

    my_car.brake()
    my_car.brake()

    print(" the car is driving at {} km".format(my_car.speed))
