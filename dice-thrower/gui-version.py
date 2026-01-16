import tkinter as tk
import random

dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

def animate_dice(count=10):
    if count > 0:
        dice_label.config(text=random.choice(dice_faces))
        dice_label.place(x=random.randint(80, 160), y=random.randint(60, 120))
        window.after(100, animate_dice, count - 1)
    else:
        final_face = random.choice(dice_faces)
        dice_label.config(text=final_face)
        dice_label.place(x=120, y=90)

# Ventana
window = tk.Tk()
window.title("Dice Roller")
window.geometry("300x250")
window.resizable(False, False)

# Título
title_label = tk.Label(
    window,
    text="🎲 Dice Roller",
    font=("Arial", 16, "bold")
)
title_label.pack(pady=10)

# Dado (usamos place para moverlo)
dice_label = tk.Label(
    window,
    text="⚀",
    font=("Arial", 50)
)
dice_label.place(x=120, y=90)

# Botón
roll_button = tk.Button(
    window,
    text="Roll Dice",
    font=("Arial", 12),
    command=animate_dice
)
roll_button.pack(side="bottom", pady=20)

window.mainloop()
