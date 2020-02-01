from arcade import Sprite, load_texture
from random import choice, randint

class Meteor(Sprite):
    def __init__(self, x, y, colour=None, size=4):
        super().__init__("images/Meteors/meteorGrey_big4.png", center_x=x, center_y=y)
        if colour:
            # If the Meteor is given a colour, use that one.
            self.colour = colour
        else:
            # Otherwise, choose a random colour.
            self.colour = choice(["grey", "brown"])

        self.size = size
        self.angle = randint(0, 360)

        self.velocity_x = randint(-4, 4)
        self.velocity_y = randint(-4, 4)

        # Depending on the colour, choose an appropriate image.
        if self.colour == "grey":
            if self.size == 4:
                images = [
                    "images/Meteors/meteorGrey_big4.png",
                    "images/Meteors/meteorGrey_big3.png",
                    "images/Meteors/meteorGrey_big2.png",
                ]
                self.texture = load_texture(choice(images))
            elif self.size == 3:
                images = [
                    "images/Meteors/meteorGrey_med1.png",
                    "images/Meteors/meteorGrey_med2.png",
                ]
                self.texture = load_texture(choice(images))
            elif self.size == 2:
                images = [
                    "images/Meteors/meteorGrey_small1.png",
                    "images/Meteors/meteorGrey_small2.png",
                ]
                self.texture = load_texture(choice(images))
            elif self.size == 1:
                images = [
                    "images/Meteors/meteorGrey_tiny1.png",
                    "images/Meteors/meteorGrey_tiny2.png",
                ]
                self.texture = load_texture(choice(images))

        else:
            if self.size == 4:
                images = [
                    "images/Meteors/meteorBrown_big4.png",
                    "images/Meteors/meteorBrown_big3.png",
                    "images/Meteors/meteorBrown_big2.png",
                ]
                self.texture = load_texture(choice(images))
            elif self.size == 3:
                images = [
                    "images/Meteors/meteorBrown_med1.png",
                    "images/Meteors/meteorBrown_med2.png",
                ]
                self.texture = load_texture(choice(images))
            elif self.size == 2:
                images = [
                    "images/Meteors/meteorBrown_small1.png",
                    "images/Meteors/meteorBrown_small2.png",
                ]
                self.texture = load_texture(choice(images))
            elif self.size == 1:
                images = [
                    "images/Meteors/meteorBrown_tiny1.png",
                    "images/Meteors/meteorBrown_tiny2.png",
                ]
                self.texture = load_texture(choice(images))

    def break_apart(self):
        self.kill()
        meteor_1 = None
        meteor_2 = None
        if self.size > 1:
            meteor_1 = Meteor(
                self.center_x, self.center_y, colour=self.colour, size=self.size - 1
            )
            if choice([0, 1]) == 1:
                meteor_2 = Meteor(
                    self.center_x, self.center_y, colour=self.colour, size=self.size - 1
                )
            else:
                meteor_2 = None
        return meteor_1, meteor_2

    def update(self, width, height):
        self.center_x = self.center_x + self.velocity_x
        self.center_y = self.center_y + self.velocity_y

        # Check the left side of the screen
        if self.right < 0:
            self.left = width
        # Check the right side of the screen
        elif self.left > width:
            self.right = 0

        # Check the bottom of the screen
        if self.top < 0:
            self.bottom = height
        # Check the top of the screen
        elif self.bottom > height:
            self.top = 0
