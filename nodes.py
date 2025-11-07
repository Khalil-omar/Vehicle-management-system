class Node:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.vehicle)
