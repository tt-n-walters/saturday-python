from arcade import Sprite
from math import sin, cos, radians

class Player(Sprite):
    def __init__(self, x, y, name, colour):
        super().__init__(
            "images/playerShip1_blue.png" if colour == "blue"
            else "images/playerShip1_green.png" if colour == "green"
            else "images/playerShip1_red.png" if colour == "red"
            else "images/playerShip1_orange.png" if colour == "orange"
            else None
        )
        self.center_x = x
        self.center_y = y
        self.name = name

    def turn_left(self):
        self.angle = self.angle + 4

    def turn_right(self):
        self.angle = self.angle - 4

    def move_forward(self):
        angle_in_radians = radians(self.angle)
        self.center_x = self.center_x + cos(angle_in_radians) * 5
        self.center_y = self.center_y + sin(angle_in_radians) * 5

    def move_backward(self):
        pass


