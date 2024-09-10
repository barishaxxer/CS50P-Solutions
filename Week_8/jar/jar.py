class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cant be negative")
        self._capacity = capacity
        self.cookie_number = 0

    def __str__(self):
        return self.cookie_number * "🍪"

    def deposit(self, n):
        if n > (self._capacity - self.cookie_number):
            raise ValueError("Insufficient capacity")
        self.cookie_number += n

    def withdraw(self, n):
        if n > self.cookie_number:
            raise ValueError("Couldnt find that much cookies!")
        self.cookie_number -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookie_number
