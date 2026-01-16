import tkinter as tk
import random


class DiceRollerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dice Roller")
        self.window.geometry("400x300")
        self.window.resizable(False, False)

        self.dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

        self.create_widgets()

    def create_widgets(self):
        # Título
        self.title_label = tk.Label(
            self.window,
            text="🎲🎲 Dice Roller",
            font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=10)

        # Frame para los dados
        self.dice_frame = tk.Frame(self.window)
        self.dice_frame.pack(pady=10)

        # Dado 1
        self.dice_label_1 = tk.Label(
            self.dice_frame,
            text="⚀",
            font=("Arial", 50)
        )
        self.dice_label_1.grid(row=0, column=0, padx=20)

        # Dado 2
        self.dice_label_2 = tk.Label(
            self.dice_frame,
            text="⚀",
            font=("Arial", 50)
        )
        self.dice_label_2.grid(row=0, column=1, padx=20)

        # Suma
        self.sum_label = tk.Label(
            self.window,
            text="Sum: 2",
            font=("Arial", 14, "bold")
        )
        self.sum_label.pack(pady=10)

        # Botón
        self.roll_button = tk.Button(
            self.window,
            text="Roll Dice",
            font=("Arial", 12),
            command=self.start_animation
        )
        self.roll_button.pack(pady=10)

    def start_animation(self):
        self.animate_dice(count=10)

    def animate_dice(self, count):
        if count > 0:
            face1 = random.choice(self.dice_faces)
            face2 = random.choice(self.dice_faces)

            self.dice_label_1.config(text=face1)
            self.dice_label_2.config(text=face2)

            self.window.after(100, self.animate_dice, count - 1)
        else:
            final_1 = random.randint(1, 6)
            final_2 = random.randint(1, 6)

            self.dice_label_1.config(text=self.dice_faces[final_1 - 1])
            self.dice_label_2.config(text=self.dice_faces[final_2 - 1])

            self.sum_label.config(text=f"Sum: {final_1 + final_2}")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = DiceRollerApp()
    app.run()
