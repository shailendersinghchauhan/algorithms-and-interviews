import random


class Simulation:
    def __init__(self, duration, time_step):
        self.duration = duration
        self.time_step = time_step
        self.current_time = 0

    def run(self):
        while self.current_time < self.duration:
            self.step()
            self.current_time += self.time_step

    def step(self):
        # Implement your simulation logic here
        pass


class SimpleSimulation(Simulation):
    def __init__(self, duration, time_step, initial_value):
        super().__init__(duration, time_step)
        self.value = initial_value

    def step(self):
        # Simulate a random change in the value
        self.value += random.randint(-1, 1)
        print(f'Time: {self.current_time}, Value: {self.value}')


# Example usage
simulation = SimpleSimulation(duration=10, time_step=1, initial_value=0)
simulation.run()
