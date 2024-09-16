import random
#the data provided are simulated not the actual data, we still need to work on it
class RefrigeratorSensor:
    def __init__(self):
        self.temperature = 0.0
        self.energy_consumption = 0.0
        self.door_open = False

    def read_temperature(self):
        self.temperature = random.uniform(2.0, 8.0)
        return self.temperature

    def read_energy_consumption(self):
        self.energy_consumption = random.uniform(0.5, 2.0)
        return self.energy_consumption

    def read_door_status(self):
        self.door_open = random.choice([True, False])
        return self.door_open
