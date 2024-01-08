import random

class Vehicle:
    def __init__(self, pilot_name, max_speed, color):
        self.pilot_name = pilot_name
        self.max_speed = max_speed
        self.color = color
        self.is_broken = False
        self.distance = 0

    def move(self):
        if not self.is_broken:
            random_speed = random.randint(0, self.max_speed)
            distance_covered = random_speed / 20
            self.distance += distance_covered

    def crash(self):
        if random.randint(1, 100) == 55:
            self.is_broken = True

class Race:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def start(self):
        while True:
            for vehicle in self.vehicles:
                vehicle.move()
                vehicle.crash()

            if all(vehicle.is_broken for vehicle in self.vehicles):
                print("All vehicles crashed. Race over.")
                break

            for vehicle in self.vehicles:
                if vehicle.distance >= 100:
                    break
                    

car1 = Vehicle("test1", 10, "Red")
car2 = Vehicle("test2", 20, "Blue")
car3 = Vehicle("test3", 30, "Green")
car4 = Vehicle("test4", 40, "Yellow")
car5 = Vehicle("test5", 50, "Orange")

race1 = Race([car1, car2, car3, car4, car5])
race2 = Race([car1, car2, car3, car4, car5])
race3 = Race([car1, car2, car3, car4, car5])

print("Race 1:")
race1.start()
print("Race 2:")
race2.start()
print("Race 3:")
race3.start()

winners = list(filter(lambda vehicle: vehicle.distance >= 100, [car1, car2, car3, car4, car5]))
if winners:
    winner = min(winners, key=lambda x: x.distance)
    print(f"The winner is {winner.pilot_name}, {winner.color} vehicle with a distance of {winner.distance} miles!")
else:
    print("No winners in any race.")
