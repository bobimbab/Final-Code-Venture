import tkinter as tk
from PIL import Image, ImageTk
from game import Game

class GameFrame:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.viewing_started = False  # Initialize the viewing flag

        self.root.title("Game")
        self.root.geometry("1200x800")  # Set the window size

        self.center_frame = tk.Frame(root)
        self.center_frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.center_frame, text="Select a module:")
        self.label.pack()

        self.album_var = tk.StringVar()
        if game.albums:
            first_album = next(iter(game.albums))
            self.album_var.set(first_album)

        self.album_menu = tk.OptionMenu(self.center_frame, self.album_var, *game.albums)
        self.album_menu.pack()

        self.start_button = tk.Button(self.center_frame, text="Start", command=self.start_viewing, bg='#d3f2e0',
                                      foreground='#087513')
        self.start_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, bg='#f2dad3', foreground='red')
        self.exit_button.pack(side=tk.BOTTOM)

        self.image_frame = tk.Frame(root)
        self.image_frame.pack(fill=tk.BOTH, expand=True)

        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(self.image_frame)
        self.button_frame.pack(fill=tk.BOTH, expand=True)

        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.show_previous_image, bg='#d3e3c5')
        self.next_button = tk.Button(self.button_frame, text="Next", command=self.show_next_image, bg='#d3e3c5')

        self.prev_button.pack(side=tk.LEFT)
        self.next_button.pack(side=tk.RIGHT)

        self.prev_button.pack_forget()  # Initially hide the previous button
        self.next_button.pack_forget()  # Initially hide the next button

        self.answer_frame = tk.Frame(root)

        self.answer_label = tk.Label(self.answer_frame, text="Challenge:")
        self.answer_label.grid(row=0, column=0, pady=300)

        self.answer_entry = tk.Entry(self.answer_frame)
        self.answer_entry.grid(row=0, column=1)
        self.answer_entry.config(state=tk.DISABLED)

        self.submit_button = tk.Button(self.answer_frame, text="Submit", command=self.submit_answer, bg='#f5f3b3')
        self.submit_button.grid(row=0, column=2)
        self.submit_button.config(state=tk.DISABLED)

        self.answer_frame.pack(fill=tk.BOTH, expand=True)
        self.answer_frame.pack_forget()  # Initially hide the answer frame

        self.result_frame = tk.Frame(self.answer_frame)  # Create the result frame
        self.result_frame.grid(row=1, column=0, columnspan=3)

        self.result_label = tk.Label(self.answer_frame, text="", fg="blue")
        self.result_label.grid(row=1, column=1, pady=(10, 0))  # Use grid to position the result label
        self.result_label.grid_remove()  # Initially hide the result label

    def start_viewing(self):
        album_name = self.album_var.get()
        self.game.set_current_album(album_name)
        self.viewing_started = True  # Set viewing flag to true

        # Remove the "Select a module" and "Start" buttons
        self.label.pack_forget()
        self.album_menu.pack_forget()
        self.start_button.pack_forget()

        # Show the previous and next buttons
        self.prev_button.pack(side=tk.LEFT)
        self.next_button.pack(side=tk.RIGHT)

        self.show_image()  # Added to display the first image

    def show_image(self):
        current_image = self.game.get_current_image()
        current_challenge, _ = self.game.get_current_challenge()

        # Remove the old image_label
        if hasattr(self, "image_label"):
            self.image_label.destroy()

        if current_image:
            # Resize the image to fit the window
            window_width = self.root.winfo_width()
            window_height = self.root.winfo_height()
            current_image = self.resize_image_to_fit_window(current_image, window_width, window_height)

            photo = ImageTk.PhotoImage(current_image)

            # Create a new image_label in the image_frame
            self.image_label = tk.Label(self.image_frame, image=photo)
            self.image_label.image = photo
            self.image_label.pack(fill=tk.BOTH, expand=True)

            if not self.viewing_started:
                self.answer_frame.pack_forget()  # Hide answer frame when viewing starts

            self.prev_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.NORMAL)

        else:
            # No more images, so display the challenge
            self.prev_button.config(state=tk.NORMAL)
            self.next_button.config(state=tk.DISABLED)

            self.answer_frame.pack(side=tk.TOP)
            self.answer_label.config(text=f"Challenge: {current_challenge}")
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.config(state=tk.NORMAL)
            self.submit_button.config(state=tk.NORMAL)

    def resize_image_to_fit_window(self, image, new_w, new_h):
        original_width, original_height = image.size
        if new_w == 0:
            scale_width = 1
        else:
            scale_width = new_w / original_width
        if new_h == 0:
            scale_height = 1
        else:
            scale_height = new_h / original_height

        scale = min(scale_width, scale_height)
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)

        resized_image = image.resize((new_width, new_height), Image.BILINEAR)
        return resized_image

    def show_previous_image(self):
        self.game.current_image_index -= 1
        self.show_image()

    def show_next_image(self):
        self.game.current_image_index += 1
        self.show_image()

    def submit_answer(self):
        user_answer = self.answer_entry.get()
        result = self.game.check_answer(user_answer)
        self.result_label.config(text=result)

        if result == "Correct!":
            self.submit_button.config(state=tk.DISABLED)

        self.result_label.grid()  # Show the result label using grid

    def show_result(self, result):
        self.result_label.config(text=result)
        if hasattr(self, "result_frame"):
            self.result_frame.destroy()

        self.result_frame = tk.Frame(self.answer_frame)
        self.result_frame.grid(row=1, column=0, columnspan=3)

        self.result_label = tk.Label(self.result_frame, text=result)
        self.result_label.grid(row=0, column=0)


if __name__ == "__main__":
    root = tk.Tk()
    game = Game()
    app = GameFrame(root, game)
    root.mainloop()
