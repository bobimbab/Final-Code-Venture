import tkinter as tk

# from quizzes_frame import QuizFrame
from detail_frame import detailframe
from user import User, YoungLearner
from datetime import date
from progress_tracker_frame import ProgressTrackerFrame
class YoungLearnerFrame(tk.Frame):

    """
    A child class that inherits its parents (User).
    """
    def __init__(self, master,login_frame, user_obj, game_frame):
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame
        self.user_obj = user_obj
        self.game_frame = game_frame


        for row_count in range(5):
            self.master.rowconfigure(row_count, weight=1, uniform="row")

        self.master.columnconfigure(0, weight=1, uniform="col")

        play_game = tk.Button(self, text="Play Game 👾",command=self.play_game)
        play_game.grid(row=0, column=0, padx=10, pady=10)

        quiz = tk.Button(self, text="Do Quiz ✍️", command=self.do_quiz)
        quiz.grid(row=1, column=0, padx=10, pady=10)

        view_profile = tk.Button(self, text="View Profile 📃", command=lambda: self.get_det(self.user_obj))
        view_profile.grid(row=2, column=0, padx=10, pady=10)

        view_progress = tk.Button(self, text="View Progress", command=self.progress_tracker)
        view_progress.grid(row=3, column=0, padx=10, pady=10)

        logout = tk.Button(self, text="Logout", command=self.logout)
        logout.grid(row=4, column=0, padx=10, pady=10)


    def play_game(self):
        from game_frame import GameFrame
        self.place_forget()
        game_frame = GameFrame(self.master,self, self.user_obj)
        game_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def do_quiz(self):
        # self.place_forget()
        # quiz_frame = QuizFrame(self.master,self)
        # quiz_frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        pass

    def get_det(self, user):
        self.place_forget()
        dets_frame = detailframe(self.master, self, user)
        dets_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def progress_tracker(self):
        self.place_forget()
        progress_tracker = ProgressTrackerFrame(self.master, self.user_obj, self)
        progress_tracker.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Display the register frame


    def logout(self):
        self.place_forget()
        self.login_frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)


if __name__ == "__main__":
    sample_user = YoungLearner(
        first_name="John",
        last_name="Doe",
        username="johndoe",
        password="password123",
        dob=date(2005, 5, 15),
        email="johndoe@example.com",
        ph_num="123-456-7890",
        grade=7
    )

    # Create the main application window
    root = tk.Tk()

    # Create a YoungLearnerFrame with the sample user
    young_learner_frame = YoungLearnerFrame(root, None, sample_user, None)

    # Place the YoungLearnerFrame in the window
    young_learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Start the application's main loop
    root.mainloop()
    # login = YoungLearnerFrame(tk.Tk(),None,None)
    # login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    # login.mainloop()