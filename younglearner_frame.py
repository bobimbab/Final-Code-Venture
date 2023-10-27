import tkinter as tk
from game_frame import GameFrame
# from quizzes_frame import QuizFrame
from detail_frame import detailframe
class YoungLearner(tk.Frame):
    """
    A child class that inherits its parents (User).
    """
    def __init__(self, master,login_frame, user_obj):
        super().__init__(master)
        self.master = master
        self.login_frame=login_frame
        self.user_obj = user_obj

        for row_count in range(5):
            self.master.rowconfigure(row_count, weight=1, uniform="row")

        self.master.columnconfigure(0, weight=1, uniform="col")

        play_game = tk.Button(self, text="Play Game 👾",command=self.play_game)
        play_game.grid(row=0, column=0, padx=10, pady=10)

        quiz = tk.Button(self, text="Do Quiz ✍️", command=self.do_quiz)
        quiz.grid(row=1, column=0, padx=10, pady=10)

        view_profile = tk.Button(self, text="View Profile 📃", command=self.get_det)
        view_profile.grid(row=2, column=0, padx=10, pady=10)

        logout = tk.Button(self, text="Logout", command=self.logout)
        logout.grid(row=3, column=0, padx=10, pady=10)


    @staticmethod

    def play_game(self):
        self.place_forget()
        game_frame = GameFrame(self.master,self)
        game_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def do_quiz(self):
        # self.place_forget()
        # quiz_frame = QuizFrame(self.master,self)
        # quiz_frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        pass

    def get_det(self):
        self.place_forget()
        dets_frame = detailframe(self.master, self)
        dets_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def logout(self):
        self.place_forget()
        self.login_frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

if __name__ == "__main__":
    # DO NOT MODIFY THIS
    login = YoungLearner(tk.Tk(),None,None)
    login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    login.mainloop()
