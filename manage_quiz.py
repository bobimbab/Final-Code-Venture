from tkinter import ttk
from quizzes_frame import load_quizzes
import tkinter as tk


class ManageQuiz(tk.Frame):

    difficulty = ["Easy", "Medium", "Hard"]

    def __init__(self, master, admin_frame = None):
        super().__init__(master=master)
        self.quizzes = load_quizzes()
        self.admin_frame = admin_frame
        self.title = ttk.Label(self, text="Manage Quiz", font=("Arial", 30, "bold"))
        self.title.pack()

        new_lst = []
        for i in self.quizzes:
            new_lst.append(i)

        self.quizzes_box = ttk.Combobox(self,values = new_lst)
        self.quizzes_box.set("Please select a quiz")
        self.quizzes_box.pack()

        self.difficulty_box = ttk.Combobox(self, values=self.difficulty)
        self.difficulty_box.set("Please select a difficulty")
        self.difficulty_box.pack()






if __name__ == "__main__":
    # DO NOT MODIFY THIS
    root = tk.Tk()
    root.geometry("1000x800")
    root.title("Manage Quiz")
    quiz_frame = ManageQuiz(root)
    quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place the frame in the center
    root.mainloop()









