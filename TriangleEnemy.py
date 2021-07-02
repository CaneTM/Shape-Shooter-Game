import random


class TriangleEnemy:

    def __init__(self, window):
        self.window = window
        self.canvas = window.canvas
        self.y2 = 20
        self.x1 = random.randint(1, self.window.window_width - self.y2)
        self.y1 = 0
        self.x2 = self.x1 + 10
        self.x3 = self.x1 + self.y2
        self.y3 = 0
        self.avatar = self.canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, fill='blue')

    def move(self, speed):
        self.canvas.move(self.avatar, 0, speed)

    def passed_line(self):
        boundary_coords = self.canvas.coords(self.window.boundary)
        return self.get_coords()[3] > boundary_coords[3]

    def get_coords(self):
        return self.canvas.coords(self.avatar)
