import tkinter as tk
import random


class AnimatedButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.normal_font_size = 13
        self.max_font_size = 15
        self.min_font_size = 14
        self.increasing = True
        self.animate()

    def animate(self):
        current_font_size = self.cget("font").split()[1]
        current_font_size = int(current_font_size)

        if self.increasing:
            current_font_size += 1
            if current_font_size >= self.max_font_size:
                self.increasing = False
        else:
            current_font_size -= 1
            if current_font_size <= self.min_font_size:
                self.increasing = True

        new_font = ("Arial", current_font_size)
        self.config(font=new_font)
        self.after(500, self.animate)


class FadingLabel(tk.Label):
    def __init__(self, master=None, text="", font=("Arial", 14), duration=2000):
        super().__init__(master, text=text, font=font)
        self.text = text
        self.duration = duration
        self.alpha = 255  # Fully opaque
        self.fade_out_interval = 2  # Time interval for fading (in milliseconds)
        self.fade_out()

    def fade_out(self):
        if self.alpha > 0:
            if self.text == "Correct":
                #change color to green
                self.configure(fg=f'#00{self.alpha:02x}00')  # Set text color with alpha channel
            elif self.text == "Incorrect":
                #change color to red
                self.configure(fg=f'#{self.alpha:02x}0000')
            self.alpha -= 1
            self.after(self.fade_out_interval, self.fade_out)
        else:
            self.destroy()  # Remove the label when it's fully faded out

class ConfettiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Confetti Animation")

        self.canvas = tk.Canvas(self, width=400, height=300, bg="white")
        self.canvas.pack()

        self.confetti_colors = ["red", "green", "blue", "yellow", "orange", "purple"]
        self.confetti_shapes = ["circle", "rectangle", "triangle"]

        self.confetti = []

        self.animate_confetti()

    def create_confetti(self):
        x = random.randint(10, 390)
        y = random.randint(10, 290)
        size = random.randint(10, 30)
        color = random.choice(self.confetti_colors)
        shape = random.choice(self.confetti_shapes)

        if shape == "circle":
            confetto = self.canvas.create_oval(x, y, x + size, y + size, fill=color, outline="")
        elif shape == "rectangle":
            confetto = self.canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline="")
        else:
            confetto = self.canvas.create_polygon(x, y, x + size, y, x + size / 2, y + size, fill=color, outline="")

        self.confetti.append((confetto, size))

    def animate_confetti(self):
        self.create_confetti()
        if len(self.confetti) > 20:
            self.canvas.delete(self.confetti[0][0])
            self.confetti.pop(0)
        self.move_confetti()
        self.after(100, self.animate_confetti)

    def move_confetti(self):
        for i, (confetto, size) in enumerate(self.confetti):
            x_velocity = random.randint(-5, 5)
            y_velocity = random.randint(2, 5)
            self.canvas.move(confetto, x_velocity, y_velocity)