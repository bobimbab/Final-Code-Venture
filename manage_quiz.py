from tkinter import ttk
from quizzes_frame import load_quizzes
import tkinter as tk


class ManageQuiz(tk.Frame):

    difficulty = ["Easy", "Medium", "Hard"]

    def __init__(self, parent):
        super().__init__(parent)
        self.quizzes = load_quizzes()
        self.parent = parent
        self.title = ttk.Label(self, text="Manage Quiz", font=("Arial", 30, "bold"))
        self.title.pack(padx=10, pady=10)

        new_lst = []
        for i in self.quizzes:
            new_lst.append(i)

        self.quizzes_box = ttk.Combobox(self,values = new_lst,width=30)
        self.quizzes_box.set("Please select a quiz")
        self.quizzes_box.pack(padx=10, pady=10)

        self.difficulty_box = ttk.Combobox(self, values=self.difficulty,width=30)
        self.difficulty_box.set("Please select a difficulty")
        self.difficulty_box.pack(padx=10, pady=10)

        self.view_question_button = ttk.Button(self, text="View Question", command=self.view_question)
        self.view_question_button.pack(padx=10, pady=10)

        self.add_question_button = ttk.Button(self, text="Add Question", command=self.add_quizzes)
        self.add_question_button.pack(padx=10, pady=20)



    def view_question(self):
        if self.quizzes_box.get() == "Please select a quiz" or self.difficulty_box.get() == "Please select a difficulty":
            return

        selected_quiz = self.quizzes[self.quizzes_box.get()]
        selected_difficulty = self.difficulty_box.get()

    def add_quizzes(self):
        self.place_forget()
        add_question_frame = AddQuizzesFrame(self.master,self)
        add_question_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class AddQuizzesFrame(tk.Frame):
    def __init__(self, parent,manage_quiz_frame):
        super().__init__(parent)
        self.manage_quiz_frame = manage_quiz_frame
        self.title = ttk.Label(self, text="Please enter a quiz title ", font=("Arial", 30, "bold"))
        self.title.pack(padx=10, pady=10)

        self.quiz_name = ttk.Label(self, text="Quiz Name:")
        self.quiz_name.pack(padx=10, pady=10)

        self.quiz_name_entry = ttk.Entry(self)
        self.quiz_name_entry.pack(padx=10, pady=10)

        self.add_question_button = ttk.Button(self, text="Add Question", command=self.add_question)
        self.add_question_button.pack(padx=10, pady=10)

    def add_question(self):
        # catch error if title is empty
        # need to validate if the name already exist in the dictionary or not
        # but for now assume that the name is unique
        self.place_forget()
        add_question_frame = AddQuestionFrame(self.master, self.quiz_name_entry.get(), self.manage_quiz_frame)
        add_question_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class AddQuestionFrame(tk.Frame):
    def __init__(self, parent, quiz_title,manage_quiz_frame):
        super().__init__(parent)
        self.manage_quiz_frame = manage_quiz_frame
        self.parent = parent
        self.question_lst = []

        self.quiz_title = quiz_title
        self.display_quiz_title = ttk.Label(self, text="Quiz Title: " + self.quiz_title, font=("Arial", 10, "bold"))
        self.display_quiz_title.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.title = ttk.Label(self, text="Please enter difficulty and question ", font=("Arial", 10, "bold"))
        self.title.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

        # Combo box for difficulty
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.difficulty_box = ttk.Combobox(self, values=self.difficulty,width=30)
        self.difficulty_box.set("Please select a difficulty")
        self.difficulty_box.grid(row=2, column=0, columnspan=5, padx=10, pady=10)

        # Question
        self.question = ttk.Label(self, text="Question:")
        self.question.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        self.question_entry = ttk.Entry(self,width=50)
        self.question_entry.grid(row=4, column=0, columnspan=5, padx=10, pady=(0, 20))

        # Options
        option_labels = ['a', 'b', 'c', 'd'] # can be changed to more options
        self.option_entries = {}
        self.correct_answer = tk.StringVar()
        for label in option_labels:
            option_label = ttk.Label(self, text=f"{label})")
            option_label.grid(row=option_labels.index(label) + 5, column=0, padx=0, pady=5, sticky='w')
            option_entry = ttk.Entry(self, width=50)
            option_entry.grid(row=option_labels.index(label) + 5, column=1, padx=0, pady=5, sticky='w')
            option_radio = ttk.Radiobutton(self, value=label, variable=self.correct_answer)
            option_radio.grid(row=option_labels.index(label) + 5, column=2, padx=0, pady=5)
            self.option_entries[label] = option_entry

        self.add_question_button = ttk.Button(self, text="Save Question", command=self.add_question)
        self.add_question_button.grid(row=10, column=1, padx=10, pady=10)
        self.done_button = ttk.Button(self, text="Done", command=self.done_button)
        self.done_button.grid(row=10, column=2, padx=10, pady=10)
        self.cancel_button = ttk.Button(self, text="Cancel", command=self.cancel_button)
        self.cancel_button.grid(row=10, column=0, padx=10, pady=10)

    def add_question(self):
        """
        Current bugs:
        1. If the user only selects one option, the program should crash
        2. A bug where if 2 options are selected, there will be no comma after the first option
        3. There will be more to come

        :return:
        """
        options = []
        if self.difficulty_box.get() == "Please select a difficulty":
            print("Please enter the difficulty and question")
            return

        if self.correct_answer.get() == "":
            print("Please select a correct answer")
            return

        if self.question_entry.get() == "":
            print("Please enter the question")
            return

        if self.option_entries[self.correct_answer.get()].get() == "":
            print("You can't select an empty option as the correct answer")
            return
        # add lines into the quizzes.txt
        ascii_num = 97
        line = ""
        line += self.quiz_title + ";" + self.difficulty_box.get() + ";" + self.question_entry.get() + ";["

        for i in self.option_entries.values():
            if i.get() == "":
                continue
            options.append(i.get().strip())

        for i in options:
            line += f'"{chr(ascii_num)}) {i}"'
            ascii_num += 1
            if i != options[-1]:
                line += ","

        line += "];"
        line += f"{self.correct_answer.get()}) {self.option_entries[self.correct_answer.get()].get()}"
        self.question_lst.append(line)
        self.question_entry.delete(0, tk.END)
        for i in self.option_entries.values():
            i.delete(0, tk.END)

    def done_button(self):
        for line in self.question_lst:
            with open("data\quizzes.txt", "a") as f:
                f.write("\n" + line)
        self.question_lst = []
        self.place_forget()
        self.manage_quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def cancel_button(self):
        self.question_lst = []
        self.place_forget()
        self.manage_quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

















if __name__ == "__main__":
    # DO NOT MODIFY THIS
    root = tk.Tk()
    root.geometry("1000x800")
    root.title("Manage Quiz")
    quiz_frame = ManageQuiz(root)
    quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place the frame in the center
    root.mainloop()









