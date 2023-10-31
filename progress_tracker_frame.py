import tkinter as tk


class ProgressTrackerFrame(tk.Frame):
    def __init__(self, master, user_obj, young_learner):
        super().__init__(master)
        self.master = master
        self.user_obj = user_obj
        self.young_learner = young_learner

        self.progress_label = tk.Label(self, text="")
        self.progress_label.pack()

        progress_label = tk.Label(self, text="Progress: ")
        progress_label.pack(side=tk.TOP)

        # Back to login page button
        # back_button = tk.Button(self, text="Back", command=lambda: login_frame.place())
        back_button = tk.Button(master=self, text="Back", command=self.return_to_younglearner)
        back_button.pack(side=tk.BOTTOM)

    def return_to_younglearner(self):
        # self.show_progress()
        self.place_forget()

        # Show the YoungLearnerFrame (assuming you have an instance of YoungLearnerFrame available)
        self.young_learner.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # def show_progress(self):
        progress = self.user_obj.get_progress()  # Replace with your method to retrieve progress
        message = "Your progress:\n"
        if self.user_obj.completed:
            for module in progress:
                message += f"{module}: Completed\n"
        else:
            for module, count in progress.items():
                message += f"{module}: {count} images viewed\n"
        self.progress_label.config(text=message)

