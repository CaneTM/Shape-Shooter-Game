import time

from Score import Score
from Window import Window
from Player import Player
from tkinter import messagebox

window = Window("Shape Shooter", 400, 500)
window.canvas.pack()

player = Player(window)
score = Score(window)

window.start_methods()

while True:
    if window.running:
        player.draw(score)
        window.move_enemy_projectiles(player)
        window.move_triangle_enemies()

        window.tk.update_idletasks()
        window.tk.update()
        time.sleep(0.01)

    else:
        window.cancel_methods()
        if messagebox.askyesno("Game Over", "GAME OVER\nDo you wish to play again?"):
            window.reset(player, score)
            window.start_methods()
        else:
            messagebox.askokcancel("End Game", "Your final score was %s points" % score.points)
            break
