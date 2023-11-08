import tkinter as tk
from game import Game


class ProgressTrackerFrame(tk.Frame):
    """
    This class frame is used to display the user's progress in the game.
    """
    def __init__(self, master, username, young_learner):
        """
               Initialize a ProgressTrackerFrame.
               Parameters:
                   - master (tk.Tk): The parent window.
                   - username (obj): The username of the user.
                   - young_learner (YoungLearnerFrame): The YoungLearnerFrame instance.
        """
        super().__init__(master)
        self.master = master

        self.young_learner = young_learner  # Store a reference to the YoungLearnerFrame instance.
        print(username.get_username(),"so what")
        self.game = Game(username.get_username())  # Create a Game instance with the provided username.

        # A label to display progress.
        self.progress_label = tk.Label(self, text="")
        self.progress_label.pack()

        # Call the method to display the progress.
        print("show progress")
        self.show_progress()

        # Back to learner page
        back_button = tk.Button(master=self, text="Back", command=self.return_to_younglearner)
        back_button.pack()

    def return_to_younglearner(self):
        """
        Returns to younglearner page.
        """
        self.place_forget()

        # Show the YoungLearnerFrame
        self.young_learner.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_progress(self):
        """
        Shows the player's game progress.
        """
        # Get the progress data from the Game instance
        all_progress = self.game.get_all_progress()
        message = "Your progress:\n"

        print(all_progress)
        for module in all_progress:
            load_completion = all_progress[module]["completed"]
            load_page = all_progress[module]["page"] + 1
            if load_completion is True:
                message += f"{module}: Completed\n"
            else:
                message += f"{module}: {load_page} pages viewed\n"

        # # Check if the game is completed (all modules are completed).
        # if self.game.completion == True:
        #     for module in progress:
        #         message += f"{module}: Completed\n"
        # else:
        #     # If the game is not completed, iterate through each module's count.
        #
        #     for module, count in progress.items():
        #         message += f"{module}: {count} pages viewed\n"
        self.progress_label.config(text=message) # Update the progress label text accordingly.
