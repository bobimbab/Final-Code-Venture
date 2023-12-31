import tkinter as tk
from PIL import Image, ImageTk
from game import Game
from younglearner_frame import YoungLearnerFrame
from user import YoungLearner

class GameFrame(tk.Frame):
    """
    The GameFrame class represents the frame that displays the game to the user. 
    It inherits from the tkinter Frame class and contains various widgets and methods 
    for managing the game interface.
    """

    def __init__(self, root, young_learner_frame, user_obj):
        """
        Initialize a GameFrame instance.

        Args:
            root (tk.Tk): The root tkinter window.
            young_learner_frame (YoungLearnerFrame): Reference to the YoungLearnerFrame.
            user_obj (YoungLearner): The user object.
        """
        super().__init__(root)
        self.root = root
        self.young_learner_frame = young_learner_frame  # Store a reference to the YoungLearnerFrame
        self.user_obj = user_obj
        self.game = Game(user_obj._username)
        self.viewing_started = False  # Initialize the viewing flag

        self.root.title("Game")

        self.center_frame = tk.Frame(root)
        self.center_frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.center_frame, text="Select a module:")
        self.label.pack()

        self.module_var = tk.StringVar()
        if self.game.modules:
            first_module = next(iter(self.game.modules))
            self.module_var.set(first_module)

        self.module_menu = tk.OptionMenu(self.center_frame, self.module_var, *self.game.modules)
        self.module_menu.pack()

        self.start_button = tk.Button(self.center_frame, text="Start", command=self.start_viewing, bg='#d3f2e0',
                                      foreground='#087513', font=("Georgia"))
        self.start_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=self.return_to_younglearner, bg='#f2dad3',
                                     foreground='red', font=("Georgia"))
        self.exit_button.pack(side=tk.BOTTOM)

        self.progress_label = tk.Label(root, text="")
        self.progress_label.pack()

        self.image_frame = tk.Frame(root)
        self.image_frame.pack(fill=tk.BOTH, expand=True)

        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(self.image_frame)
        self.button_frame.pack(fill=tk.BOTH, expand=True)

        self.prev_button = tk.Button(self.button_frame, text="Previous", command=self.show_previous_image, bg='#d3e3c5', font=("Georgia"))
        self.next_button = tk.Button(self.button_frame, text="Next", command=self.show_next_image, bg='#d3e3c5', font=("Georgia"))

        self.prev_button.pack(side=tk.LEFT)
        self.next_button.pack(side=tk.RIGHT)

        self.prev_button.pack_forget()  # Initially hide the previous button
        self.next_button.pack_forget()  # Initially hide the next button

        self.answer_frame = tk.Frame(root)

        self.answer_label = tk.Label(self.answer_frame, text="Challenge:", font=("Georgia"))
        self.answer_label.grid(row=0, column=0, pady=150)

        self.answer_entry = tk.Entry(self.answer_frame)
        self.answer_entry.grid(row=0, column=1)
        self.answer_entry.config(state=tk.DISABLED)

        self.submit_button = tk.Button(self.answer_frame, text="Submit", command=self.submit_answer, bg='#f5f3b3', font=("Georgia"))
        self.submit_button.grid(row=0, column=2)
        self.submit_button.config(state=tk.DISABLED)

        self.answer_frame.pack(fill=tk.BOTH, expand=True)
        self.answer_frame.pack_forget()  # Initially hide the answer frame

        self.result_frame = tk.Frame(self.answer_frame)  # Create the result frame
        self.result_frame.grid(row=1, column=0, columnspan=3)

        self.result_label = tk.Label(self.answer_frame, text="", fg="blue", font=("Georgia"))
        self.result_label.grid(row=1, column=1, pady=(10, 0))  # Use grid to position the result label
        self.result_label.grid_remove()  # Initially hide the result label

    def start_viewing(self):
        """
        Start the game viewing when the "Start" button is clicked.
        """
        module_name = self.module_var.get()
        self.game.set_current_module(module_name)
        self.viewing_started = True  # Set viewing flag to true

        # Remove the "Select a module" and "Start" buttons
        self.label.pack_forget()
        self.module_menu.pack_forget()
        self.start_button.pack_forget()

        # Show the previous and next buttons
        self.prev_button.pack(side=tk.LEFT)
        self.next_button.pack(side=tk.RIGHT)

        self.show_image()  # display the first image

    def show_image(self):
        """
        Display the current image or challenge to the user.
        """
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

    @staticmethod
    def resize_image_to_fit_window(image, new_w, new_h):
        """
        Resize the image to fit the specified dimensions.

        Args:
            image (PIL.Image.Image): The image to resize.
            new_w (int): The new width.
            new_h (int): The new height.

        Returns:
            PIL.Image.Image: The resized image.
        """
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
        """
        Display the previous image when the "Previous" button is clicked.
        """
        self.game.current_image_index -= 1
        self.show_image()

    def show_next_image(self):
        """
        Display the next image when the "Next" button is clicked.
        """
        self.game.current_image_index += 1
        self.show_image()

    def submit_answer(self):
        """
        Submit the user's answer and display the result.
        """
        user_answer = self.answer_entry.get()
        result = self.game.check_answer(user_answer)
        self.result_label.config(text=result)

        if result == "Correct!":
            self.submit_button.config(state=tk.DISABLED)
            self.game.update_progress()  # Add this line to update the progress

        self.result_label.grid()  # Show the result label using grid

        if result == "Incorrect!":
            self.submit_button.config(command=self.submit_correct_answer)

    def submit_correct_answer(self):
        """
        Submit the user's answer again after an incorrect attempt.
        """
        user_answer = self.answer_entry.get()
        result = self.game.check_answer(user_answer)
        self.result_label.config(text=result)

        if result == "Correct!":
            self.submit_button.config(state=tk.DISABLED)
            self.game.update_progress()  # Add this line to update the progress

        self.result_label.grid()

    def show_result(self, result):
        """
        Display the result to the user.

        Args:
            result (str): The result message to display.
        """
        self.result_label.config(text=result)
        if hasattr(self, "result_frame"):
            self.result_frame.destroy()

        self.result_frame = tk.Frame(self.answer_frame)
        self.result_frame.grid(row=1, column=0, columnspan=3)

        self.result_label = tk.Label(self.result_frame, text=result)
        self.result_label.grid(row=0, column=0)

    def show_progress(self):
        """
        Display the user's progress.
        """
        progress = self.game.progress
        message = "Your progress:\n"
        if self.game.completion:
            for module in progress:
                message += f"{module}: Completed"
        else:
            for module, count in progress.items():
                message += f"{module}: {count} pages viewed\n"
        self.progress_label.config(text=message)

    def return_to_younglearner(self):
        """
        Return to the YoungLearnerFrame and hide the GameFrame.
        """
        self.place_forget()

        # Hide the "Exit" button
        self.exit_button.pack_forget()

        # Hide the current frame (GameFrame)
        self.center_frame.pack_forget()
        self.image_frame.pack_forget()
        self.answer_frame.pack_forget()
        self.result_frame.pack_forget()

        # Show the YoungLearnerFrame (assuming you have an instance of YoungLearnerFrame available)
        self.young_learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
