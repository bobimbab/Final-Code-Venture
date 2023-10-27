import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from game import Game

class GameFrame:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.viewing_started = False  # Track if viewing has started

        self.root.title("Game")

        self.album_selection_frame = tk.Frame(root)
        self.album_selection_frame.pack(pady=10)

        self.label = tk.Label(self.album_selection_frame, text="Select a module:")
        self.label.pack(side=tk.LEFT)

        self.album_var = tk.StringVar()
        self.album_var.set(game.albums[0])

        self.album_menu = tk.OptionMenu(self.album_selection_frame, self.album_var, *game.albums)
        self.album_menu.pack(side=tk.LEFT)

        self.start_button = tk.Button(self.album_selection_frame, text="Start", command=self.start_viewing)
        self.start_button.pack(side=tk.LEFT)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(side=tk.BOTTOM)

        self.image_frame = tk.Frame(root)
        self.image_frame.pack()

        self.image_label = tk.Label(self.image_frame)
        self.image_label.grid(row=0, column=0, columnspan=2)  # Span two columns

        # Create a nested frame for previous and next buttons and use grid within it
        button_frame = tk.Frame(self.image_frame)
        button_frame.grid(row=1, column=0, columnspan=2)  # Span two columns

        self.prev_button = tk.Button(button_frame, text="Previous", command=self.show_previous_image)
        self.next_button = tk.Button(button_frame, text="Next", command=self.show_next_image)

        self.prev_button.grid(row=0, column=0, sticky="nsew")
        self.next_button.grid(row=0, column=1, sticky="nsew")

        self.prev_button.grid_remove()  # Initially hide the previous button
        self.next_button.grid_remove()  # Initially hide the next button

        self.answer_frame = tk.Frame(root)

        self.answer_label = tk.Label(self.answer_frame, text="Your Answer:")
        self.answer_label.pack(side=tk.LEFT)

        self.answer_entry = tk.Entry(self.answer_frame)
        self.answer_entry.pack(side=tk.LEFT)
        self.answer_entry.config(state=tk.DISABLED)

        self.submit_button = tk.Button(self.answer_frame, text="Submit", command=self.submit_answer)
        self.submit_button.pack(side=tk.LEFT)
        self.submit_button.config(state=tk.DISABLED)

        self.answer_frame.pack_forget()  # Initially hide the answer frame

    def start_viewing(self):
        album_name = self.album_var.get()
        self.game.set_current_album(album_name)
        self.show_image()
        self.viewing_started = True  # Set viewing flag to true

        # Remove the "Select a module" and "Start" buttons
        self.label.pack_forget()
        self.album_menu.pack_forget()
        self.start_button.pack_forget()

        # Show the previous and next buttons
        self.prev_button.grid()
        self.next_button.grid()

        # Show the answer frame
        self.answer_frame.pack()

    def show_image(self):
        current_image = self.game.get_current_image()
        current_challenge, _ = self.game.get_current_challenge()

        if current_image:
            # Resize the image to fit the window
            window_width = self.root.winfo_width()
            window_height = self.root.winfo_height()
            current_image = self.resize_image_to_fit_window(current_image, window_width, window_height)

            photo = ImageTk.PhotoImage(current_image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

            self.answer_label.config(text=f"Challenge: {current_challenge}")
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.config(state=tk.NORMAL)
            self.submit_button.config(state=tk.NORMAL)
        else:
            messagebox.showinfo("End of Module", "You've reached the end of the module!")

    def resize_image_to_fit_window(self, image, window_width, window_height):
        img_width, img_height = image.size
        if img_width > window_width or img_height > window_height:
            ratio = min(window_width / img_width, window_height / img_height)
            new_width = int(img_width * ratio)
            new_height = int(img_height * ratio)
            return image.resize((new_width, new_height), Image.BILINEAR)
        else:
            return image

    def show_previous_image(self):
        self.game.current_image_index -= 1
        self.show_image()

    def show_next_image(self):
        self.game.current_image_index += 1
        self.show_image()

    def submit_answer(self):
        user_answer = self.answer_entry.get()
        result = self.game.check_answer(user_answer)
        messagebox.showinfo("Result", result)
        self.answer_entry.delete(0, tk.END)

        if result == "Correct!":
            self.submit_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = Game()
    app = GameFrame(root, game)
    root.mainloop()