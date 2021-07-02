from SquareEnemy import SquareEnemy
from TriangleEnemy import TriangleEnemy


class Player:

    def __init__(self, window):
        self.window = window
        self.canvas = window.canvas
        self.avatar = self.canvas.create_polygon(190, 500, 200, 480, 210, 500, fill='red')
        self.x = 0
        self.speed = 2
        self.player_pos = 0
        self.projectiles = []
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<space>', self.shoot)

    def move_left(self, evt):
        self.x = -self.speed

    def move_right(self, evt):
        self.x = self.speed

    def draw(self, score):
        self.canvas.move(self.avatar, self.x, 0)
        player_pos = self.canvas.coords(self.avatar)

        if player_pos[0] <= 0 or player_pos[4] >= self.window.window_width:
            self.x = 0

        self.handle_projectiles(score)

    def shoot(self, evt):
        player_pos = self.canvas.coords(self.avatar)
        player_shot = self.canvas.create_line(player_pos[2], 480, player_pos[2], 460, fill='yellow')
        self.projectiles.append(player_shot)

    def handle_projectiles(self, score):
        self.move_projectiles()
        self.check_projectiles(self.window.square_enemies, 2, 3, 0, 2, 1, 3, score)
        self.check_projectiles(self.window.triangle_enemies, 2, 3, 0, 4, 1, 3, score)

    def move_projectiles(self):
        for player_shot in self.projectiles:
            projectile_pos = self.canvas.coords(player_shot)
            self.canvas.move(player_shot, 0, -5)
            if projectile_pos[3] <= 0:
                self.projectiles.remove(player_shot)
                self.canvas.itemconfig(player_shot, state='hidden')

    def check_projectiles(self, enemies_list, shot_coord1, shot_coord2,
                          e_coord1, e_coord2, e_coord3, e_coord4, score):
        for enemy in enemies_list:
            for player_shot in self.projectiles:
                enemy_pos = enemy.get_coords()
                player_shot_pos = self.window.canvas.coords(player_shot)
                if enemy_pos[e_coord1] <= player_shot_pos[shot_coord1] <= enemy_pos[e_coord2] and \
                        enemy_pos[e_coord3] <= player_shot_pos[shot_coord2] <= enemy_pos[e_coord4]:
                    enemies_list.remove(enemy)
                    self.projectiles.remove(player_shot)
                    self.window.canvas.itemconfig(enemy.avatar, state='hidden')
                    self.window.canvas.itemconfig(player_shot, state='hidden')

                    if isinstance(enemy, SquareEnemy):
                        score.update(1)
                    elif isinstance(enemy, TriangleEnemy):
                        score.update(10)

    def get_coords(self):
        return self.canvas.coords(self.avatar)

    def reset(self):
        self.canvas.move(self.avatar, 190 - self.get_coords()[0], 0)
