import random


class SquareEnemy:

    def __init__(self, window):
        self.window = window
        self.canvas = window.canvas
        self.width = 20
        self.x1 = random.randint(1, self.window.window_width - self.width)
        self.y1 = 0
        self.x2 = self.x1 + self.width
        self.avatar = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.width, fill='green')

    def move(self, speed):
        self.canvas.move(self.avatar, 0, speed)

    def shoot(self):
        starting_pos = self.get_coords()
        enemy_projectile = self.canvas.create_line(starting_pos[0] + 10, starting_pos[3],
                                                   starting_pos[0] + 10, starting_pos[3] + 20,
                                                   fill='magenta')
        return enemy_projectile

    def get_coords(self):
        return self.canvas.coords(self.avatar)

    def passed_line(self):
        boundary_coords = self.canvas.coords(self.window.boundary)
        return self.get_coords()[3] > boundary_coords[3]
