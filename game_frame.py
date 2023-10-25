import tkinter as tk
from tkinter import Label, Button, Entry
from PIL import Image, ImageTk
from game import Game

class Game_frame:
    def __init__(self, root):
        self.root = root
        self.root.title("Game")
        self.root.geometry("400x400")

        self.label = Label(self.root)
        self.label.pack()

        self.question_label = Label(self.root, text="", font=("Arial", 12))
        self.question_label.pack()

        self.answer_entry = Entry(self.root)
        self.answer_entry.pack()

        self.next_button = Button(self.root, text="Next", command=self.next_image)
        self.prev_button = Button(self.root, text="Previous", command=self.prev_image)

        self.next_button.pack()
        self.prev_button.pack()

        self.show_content()
        self.show_challenge()

    def show_content(self):
        image_path = Game.get_current_image_path()
        img = Image.open(image_path)
        img = img.resize((300, 300))
        photo = ImageTk.PhotoImage(img)

        self.label.config(image=photo)
        self.label.image = photo

    def show_challenge(self):
        challenge = Game.get_current_challenge()
        self.question_label.config(text=challenge["question"])
        self.answer_entry.delete(0, "end")  # Clear the answer entry field

    def next_content(self):
        Game.next_content()
        self.show_content()
        self.show_challenge()

    def prev_content(self):
        Game.prev_content()
        self.show_content()
        self.show_challenge()

    def check_answer(self):
        answer = self.answer_entry.get()
        if Game.is_answer_correct(answer):
            # Handle correct answer, e.g., show a message or move to the next image.
            print("Correct answer!")
            self.next_image()
        else:
            # Handle incorrect answer, e.g., show an error message.
            print("Incorrect answer!")

if __name__ == "__main__":
    root = tk.Tk()
    app = Game_frame(root)
    root.mainloop()
