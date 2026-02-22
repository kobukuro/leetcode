# Tags: Design, Simulation, Counting
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = {1: big,
                       2: medium,
                       3: small}

    def add_car(self, car_type: int) -> bool:
        if self.spaces[car_type] == 0:
            return False
        self.spaces[car_type] -= 1
        return True
