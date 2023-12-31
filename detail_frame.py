import tkinter as tk
from user import User, YoungLearner, Admin

class DetailFrame(tk.Frame):
    """
    The DetailFrame class represents a frame that displays user details.
    """
    def __init__(self, master, younglearner_frame, user):
        """
        Initialize the DetailFrame with user details.

        Args:
            master (tk.Tk): The parent window.
            younglearner_frame: The young learner frame to return to.
            user (User): The user object to display details for.
        """
        super().__init__(master)
        self.master = master
        self.younglearner_frame = younglearner_frame
        self.user = user

        for row_count in range(5):
            self.master.rowconfigure(row_count, weight=1, uniform="row")

        self.master.columnconfigure(0, weight=1, uniform="col")

        detail_user = tk.Label(self, text=f"User: {self.user.get_full_name()} ")
        detail_user.grid(row=0, column=0, padx=10, pady=10)
        detail_username = tk.Label(self, text=f"Username: {self.user.get_username()}")
        detail_username.grid(row=1, column=0, padx=10, pady=10)
        detail_dob = tk.Label(self, text=f"Date of Birth: {self.user.get_dob()}")
        detail_dob.grid(row=2, column=0, padx=10, pady=10)
        detail_email = tk.Label(self, text=f"Email: {self.user.get_email()}")
        detail_email.grid(row=3, column=0, padx=10, pady=10)
        detail_ph = tk.Label(self, text=f"Phone Number: {self.user.get_ph_num()}")
        detail_ph.grid(row=4, column=0, padx=10, pady=10)

        if isinstance(self.user, YoungLearner):
            detail_grade = tk.Label(self, text=f"Grade: {self.user.get_grade()}")
            detail_grade.grid(row=5, column=0, padx=10, pady=10)

        back_button = tk.Button(self, text="Back", command=self.back)
        back_button.grid(row=6, column=0, padx=10, pady=10)

    def back(self):
        """
        Return to the young learner frame.
        """
        self.place_forget()
        self.younglearner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
