import tkinter as tk
from PIL import Image, ImageTk
from game import GameLogic

class GameFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.game_logic = None
        self.navigation_frame = None
        self.current_image = None  # Store the current image as an attribute

        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("easy")  # Default difficulty

        self.create_widgets()

    def create_widgets(self):
        # Create and place the navigation frame
        self.navigation_frame = tk.Frame(self.parent)
        self.navigation_frame.grid(row=0, column=0, columnspan=2)

        self.difficulty_label = tk.Label(self, text="Choose Difficulty:")
        self.difficulty_label.grid(row=1, column=0)

        difficulty_options = ["easy", "medium", "hard"]
        self.difficulty_menu = tk.OptionMenu(self, self.difficulty_var, *difficulty_options)
        self.difficulty_menu.grid(row=1, column=1)

        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, columnspan=2)

        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=3, column=0, columnspan=2)

        self.question_label = tk.Label(self, text="")
        self.question_label.grid(row=4, column=0, columnspan=2)

        self.previous_button = tk.Button(self, text="Previous", command=self.previous_image)
        self.next_button = tk.Button(self, text="Next", command=self.next_image)

        self.create_exit_button()  # Create the exit button

    def create_exit_button(self):
        self.exit_button = tk.Button(self, text="Exit", command=self.exit_game)
        self.exit_button.grid(row=5, column=0, columnspan=2)
        # Show the exit button by default
        self.exit_button.grid()

    def start_game(self):
        difficulty = self.difficulty_var.get()
        self.game_logic = GameLogic(difficulty)
        self.game_logic.load_images()
        self.game_logic.load_questions()
        self.display_current_image()

        # Clear the "Choose Difficulty" label and the "Start Game" button
        self.difficulty_label.destroy()
        self.difficulty_menu.destroy()
        self.start_button.destroy()

        self.previous_button.grid(row=5, column=0)  # Show the previous button
        self.next_button.grid(row=5, column=1)  # Show the next button

        self.create_exit_button()  # Create the exit button after the game starts

    def display_current_image(self):
        current_image_path = self.game_logic.get_current_image()
        image = Image.open(current_image_path)
        resized_image = self.resize_image(image)

        self.canvas.delete("all")  # Clear canvas before drawing new image
        self.current_image = resized_image  # Store the PhotoImage object
        self.canvas.create_image(0, 0, anchor="nw", image=self.current_image)
    def resize_image(self, image):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        image_width, image_height = image.size

        # Calculate the aspect ratio to maintain the image's original proportions
        aspect_ratio = min(canvas_width / image_width, canvas_height / image_height)
        new_width = int(image_width * aspect_ratio)
        new_height = int(image_height * aspect_ratio)

        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        return ImageTk.PhotoImage(resized_image)

    def display_current_question(self):
        current_question = self.game_logic.get_current_question()
        self.canvas.grid_forget()
        self.question_label.config(text=current_question)

        # Update the grid layout to properly position the buttons
        self.previous_button.grid(row=6, column=0)
        self.next_button.grid(row=6, column=1)
        self.exit_button.grid_remove()  # Remove the duplicate exit button

    def next_image(self):
        self.game_logic.next_image()
        self.display_current_image()
        if self.game_logic.current_image_index == len(self.game_logic.images) - 1:
            self.display_current_question()

    def previous_image(self):
        self.game_logic.previous_image()
        self.display_current_image()

    def exit_game(self):
        self.parent.destroy()  # Destroy the current frame and exit the application

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x800")

    game_frame = GameFrame(root)
    game_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place the frame in the center

    root.mainloop()