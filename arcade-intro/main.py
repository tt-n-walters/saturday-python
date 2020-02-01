from arcade import *
from random import choice, randint
from meteor import Meteor
from player import Player


class Window(Window):
    def __init__(self):
        # Tell the class incharge, to run the __init__ function
        super().__init__(800, 600, "My Arcade Window")
        self.set_update_rate(1)
        # Create a copy of the Meteor class, using x=200 and y=200
        # self.meteor = Meteor(200, 200)
        # Create an empty list
        self.meteors = SpriteList()
        # Loop 20 times
        for i in range(20):
            # Create a copy of the Meteor class, using random integers for x and y
            new_meteor = Meteor(randint(0, self.width), randint(0, self.height))
            # Add the new copy to the list of meteors
            self.meteors.append(new_meteor)

        self.player = Player(self.width / 2, self.height / 2, "Best Player", "blue")

        self.a_pressed = False
        self.d_pressed = False
        self.w_pressed = False
        self.s_pressed = False

    def on_draw(self):
        print("Drawing")
        start_render()
        # Draw the player
        self.player.draw()

        # self.meteor.draw()
        # Loop from 0 to the number of meteors in the list
        for i in range(len(self.meteors)):
            # Draw each meteor one at a time
            self.meteors[i].draw()

    def on_update(self, delta_time):
        print("Updating!")
        # Update each meteor one at a time
        for meteor in self.meteors:
            meteor.update(self.width, self.height)
        
        if self.a_pressed == True:
            self.player.turn_left()
        if self.d_pressed == True:
            self.player.turn_right()

    def on_mouse_motion(self, x, y, dx, dy):
        pass
        # self.meteor.center_x = x
        # self.meteor.center_y = y

    def on_key_press(self, symbol, modifiers):
        print("Key pressed")
        print(symbol)
        if symbol == key.A or symbol == key.LEFT:
            print("Change a_pressed to True")
            self.a_pressed = True
        elif symbol == key.D or symbol == key.RIGHT:
            print("Change d_pressed to True")
            self.d_pressed = True
        else:
            random_meteor = choice(self.meteors)
            new_meteor_1, new_meteor_2 = random_meteor.break_apart()
            if new_meteor_1:
                # If the __break_apart__ function creates a new Meteor, add it to the list.
                # Otherwise, don't add it to the list.
                self.meteors.append(new_meteor_1)
            if new_meteor_2:
                self.meteors.append(new_meteor_2)

    def on_key_release(self, symbol, modifiers):
        print("Key released")
        if symbol == key.A or symbol == key.LEFT:
            print("Change a_pressed to False")
            self.a_pressed = False
        elif symbol == key.D or symbol == key.RIGHT:
            print("Change d_pressed to False")
            self.d_pressed = False

Window()
run()
