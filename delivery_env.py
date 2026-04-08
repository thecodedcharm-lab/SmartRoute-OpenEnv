import random

class DeliveryEnv:

    def __init__(self, packages=5, fuel=50, time_limit=100):
        self.initial_packages = packages
        self.initial_fuel = fuel
        self.initial_time = time_limit
        self.reset()

    def reset(self):
        self.packages_remaining = self.initial_packages
        self.fuel = self.initial_fuel
        self.time_left = self.initial_time
        self.traffic = random.uniform(0.1, 0.5)
        self.priority_packages = random.randint(1, 2)
        self.location = 0
        return self.state()

    def state(self):
        return {
            "packages_remaining": self.packages_remaining,
            "fuel": self.fuel,
            "time_left": self.time_left,
            "traffic": round(self.traffic, 2),
            "priority_packages": self.priority_packages,
            "location": self.location
        }

    def step(self, action):
        reward = 0
        done = False

        if self.time_left <= 0 or self.fuel <= 0:
            done = True
            return self.state(), -1, done

        if action == 0:  # deliver nearest
            if self.packages_remaining > 0:
                self.packages_remaining -= 1
                self.fuel -= 5
                self.time_left -= 10
                reward = 1

        elif action == 1:  # deliver priority
            if self.priority_packages > 0:
                self.priority_packages -= 1
                self.packages_remaining -= 1
                self.fuel -= 6
                self.time_left -= 12
                reward = 1.5

        elif action == 2:  # refuel
            self.fuel += 20
            self.time_left -= 5
            reward = -0.2

        elif action == 3:  # avoid traffic
            self.traffic = max(0.1, self.traffic - 0.1)
            self.time_left -= 3
            reward = 0.2

        elif action == 4:  # wait
            self.time_left -= 2
            reward = -0.1

        if self.packages_remaining <= 0:
            done = True
            reward += 2

        return self.state(), reward, done
