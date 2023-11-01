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
        self.alpha = 255
        self.fade_out_interval = 2
        self.fade_out()

    def fade_out(self):
        if self.alpha > 0:
            if self.text == "Correct":
                #change color to green
                self.configure(fg=f'#00{self.alpha:02x}00')
            elif self.text == "Incorrect":
                #change color to red
                self.configure(fg=f'#{self.alpha:02x}0000')
            self.alpha -= 1
            self.after(self.fade_out_interval, self.fade_out)
        else:
            self.destroy()
