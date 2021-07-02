class Score:

    def __init__(self, window):
        self.canvas = window.canvas
        self.points = 0
        self.screen_text = self.canvas.create_text(350, 490, text='Pts: %s' % self.points, fill='white', font='Verdana')

    def update(self, amt):
        self.points += amt
        self.canvas.itemconfig(self.screen_text, text='Pts: %s' % self.points)

    def reset(self):
        self.update(-self.points)
