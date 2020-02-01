from arcade import *
from sorting import data, bubble


class BubbleSort(Window):
    def __init__(self):
        super().__init__(800, 300, "Bubble Sort Visualisation")
        set_background_color(color.WHITE)

        self.bars = []
        for i, number in enumerate(data):
            self.bars.append(Bar(number))
            self.bars[i].set_x_position(i * 25)

    def on_draw(self):
        start_render()
        for bar in self.bars:
            bar.draw()

    def on_update(self, delta_time):
        bubble(self.bars)


class Bar(Sprite):
    def __init__(self, height):
        super().__init__()
        self.height = height
        self.width = 20
        self.left = 0
        self.bottom = 0

    def set_x_position(self, x):
        self.left = x
    
    def draw(self):
        draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, color.BLUE)


animation = BubbleSort()
run()
