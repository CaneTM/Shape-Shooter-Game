import random
from tkinter import *

from SquareEnemy import SquareEnemy
from TriangleEnemy import TriangleEnemy


class Window:

    def __init__(self, title, width, height):
        self.tk = Tk()
        self.tk.title(title)
        self.canvas = Canvas(self.tk, width=width, height=height, bg='black')
        self.boundary = self.canvas.create_line(0, height - 40, width, height - 40, fill='orange')
        self.square_enemies = []
        self.triangle_enemies = []
        self.enemy_projectiles = []
        self.running = True

        self.window_width = width
        self.window_height = height

        self.create_square_enemies_func = 0
        self.move_square_enemies_func = 0
        self.move_boundary_func = 0
        self.make_enemy_shoot_func = 0
        self.create_triangle_enemies_func = 0

    def create_square_enemies(self):
        self.square_enemies.append(SquareEnemy(self))
        self.create_square_enemies_func = self.tk.after(750, self.create_square_enemies)

    def create_triangle_enemies(self):
        ms = random.randint(16000, 24000)
        self.triangle_enemies.append(TriangleEnemy(self))
        self.create_triangle_enemies_func = self.tk.after(ms, self.create_triangle_enemies)

    def move_square_enemies(self):
        for enemy in self.square_enemies:
            enemy.move(8)
            if enemy.passed_line():
                self.running = False

        self.move_square_enemies_func = self.tk.after(1000, self.move_square_enemies)

    def move_triangle_enemies(self):
        for enemy in self.triangle_enemies:
            enemy.move(4)
            if enemy.passed_line():
                self.running = False

    def make_enemy_shoot(self):
        ms = random.randint(500, 1500)
        selected_enemy = random.choice(self.square_enemies)
        self.enemy_projectiles.append(selected_enemy.shoot())
        self.make_enemy_shoot_func = self.tk.after(ms, self.make_enemy_shoot)

    def move_enemy_projectiles(self, player):
        for projectile in self.enemy_projectiles:
            projectile_pos = self.canvas.coords(projectile)
            player_coords = player.get_coords()
            self.canvas.move(projectile, 0, 3)

            if projectile_pos[1] >= self.window_height:
                self.enemy_projectiles.remove(projectile)
                self.canvas.itemconfig(projectile, state='hidden')

            if player_coords[0] <= projectile_pos[0] <= player_coords[4] and \
                    projectile_pos[3] >= self.window_height - 10:
                self.running = False

    def move_boundary(self):
        self.canvas.move(self.boundary, 0, -10)
        self.move_boundary_func = self.tk.after(19000, self.move_boundary)

    def cancel_methods(self):
        self.tk.after_cancel(self.create_square_enemies_func)
        self.tk.after_cancel(self.move_square_enemies_func)
        self.tk.after_cancel(self.move_boundary_func)
        self.tk.after_cancel(self.make_enemy_shoot_func)
        self.tk.after_cancel(self.create_triangle_enemies_func)

    def pre_cancel_methods(self):
        self.tk.after_cancel(self.create_square_enemies_func)
        self.tk.after_cancel(self.move_square_enemies_func)
        self.tk.after_cancel(self.move_boundary_func)
        self.tk.after_cancel(self.make_enemy_shoot_func)

    def start_methods(self):
        self.create_square_enemies()
        self.move_square_enemies()
        self.move_boundary()
        self.make_enemy_shoot()
        self.tk.after(10000, self.create_triangle_enemies)

    def reset(self, player, score):
        for square in self.square_enemies:
            self.canvas.itemconfig(square.avatar, state='hidden')
        for triangle in self.triangle_enemies:
            self.canvas.itemconfig(triangle.avatar, state='hidden')
        for enemy_shot in self.enemy_projectiles:
            self.canvas.itemconfig(enemy_shot, state='hidden')
        for player_shot in player.projectiles:
            self.canvas.itemconfig(player_shot, state='hidden')

        self.square_enemies.clear()
        self.triangle_enemies.clear()
        self.enemy_projectiles.clear()
        player.projectiles.clear()

        self.canvas.move(self.boundary, 0, 460 - self.canvas.coords(self.boundary)[3])
        player.reset()
        score.reset()
        self.running = True
