import tkinter as tk
from game import Game


class ProgressTrackerFrame(tk.Frame):
    def __init__(self, master, username, young_learner):
        super().__init__(master)
        self.master = master
        
        self.young_learner = young_learner
        self.game = Game(username)

        self.progress_label = tk.Label(self, text="")
        self.progress_label.pack()

        self.show_progress()

        # Back to learner page
        # back_button = tk.Button(self, text="Back", command=lambda: login_frame.place())
        back_button = tk.Button(master=self, text="Back", command=self.return_to_younglearner)
        back_button.pack()

    def return_to_younglearner(self):
        self.place_forget()

        # Show the YoungLearnerFrame (assuming you have an instance of YoungLearnerFrame available)
        self.young_learner.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def show_progress(self):
        progress = self.game.progress
        message = "Your progress:\n"
        if self.game.completion == True:
            for module in progress:
                message += f"{module}: Completed\n"
        else:
            for module, count in progress.items():
                message += f"{module}: {count} pages viewed\n"
        self.progress_label.config(text=message)
