from tkinter import ttk
from quizzes import Quizzes
import tkinter as tk


# ---------------------------- Manage Quiz Frame ---------------------------- #
class ManageQuiz(tk.Frame):

    difficulty = ["Easy", "Medium", "Hard"]

    def __init__(self, parent):
        super().__init__(parent)
        self.quizzes = Quizzes.load_quizzes()
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

        self.view_question_button = ttk.Button(self, text="View Quiz", command=self.view_question)
        self.view_question_button.pack(padx=10, pady=10)

        self.add_question_button = ttk.Button(self, text="Add new Questions", command=self.add_question)
        self.add_question_button.pack(padx=10, pady=10)

        self.add_quiz_button = ttk.Button(self, text="Add a new Quiz", command=self.add_quizzes)
        self.add_quiz_button.pack(padx=10, pady=30)

        self.message = tk.StringVar()
        self.message_label = ttk.Label(self, textvariable=self.message, font=("Arial", 10, "bold"))
        self.message_label.pack(padx=10, pady=10)

    def view_question(self):
        if self.quizzes_box.get() == "Please select a quiz" or self.difficulty_box.get() == "Please select a difficulty":
            self.message.set("Please select a quiz and difficulty")
            return

        selected_quiz = self.quizzes[self.quizzes_box.get()]
        selected_difficulty = self.difficulty_box.get()

        self.place_forget()
        view_quiz = ViewQuiz(self.parent, selected_quiz, selected_difficulty, self)
        view_quiz.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def add_question(self):
        if self.quizzes_box.get() == "Please select a quiz":
            self.message.set("Please select a quiz")
            return

        self.place_forget()
        add_question_frame = AddQuestionFrame(self.master, self.quizzes_box.get(), self)
        add_question_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def add_quizzes(self):
        self.place_forget()
        add_question_frame = AddQuizzesFrame(self.master,self)
        add_question_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# ---------------------------- Add Quiz Frame ---------------------------- #


class AddQuizzesFrame(tk.Frame):
    """

    """
    def __init__(self, parent,manage_quiz_frame):
        super().__init__(parent)
        self.manage_quiz_frame = manage_quiz_frame
        self.title = ttk.Label(self, text="Please enter a quiz title ", font=("Arial", 30, "bold"))
        self.title.pack(padx=10, pady=10)

        self.quiz_name = ttk.Label(self, text="Quiz Name:")
        self.quiz_name.pack(padx=10, pady=10)

        self.quiz_name_entry = ttk.Entry(self, width=50)
        self.quiz_name_entry.pack(padx=10, pady=10)

        self.add_question_button = ttk.Button(self, text="Add Question", command=self.add_question)
        self.add_question_button.pack(padx=10, pady=10)

        self.message = tk.StringVar()
        self.message_label = ttk.Label(self, textvariable=self.message, font=("Arial", 10, "bold"))
        self.message_label.pack(padx=10, pady=10)

        self.go_back_button = ttk.Button(self, text="Go Back", command=self.go_back)
        self.go_back_button.pack(padx=10, pady=10)

    def add_question(self):
        # catch error if title is empty
        if self.quiz_name_entry.get() == "":
            self.message.set("Please enter a quiz title")
            return

        if self.quiz_name_entry.get() in self.manage_quiz_frame.quizzes:
            self.message.set("Quiz name already exist")
            return

        self.place_forget()
        add_question_frame = AddQuestionFrame(self.master, self.quiz_name_entry.get().strip(), self.manage_quiz_frame)
        add_question_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def go_back(self):
        self.place_forget()
        self.manage_quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class AddQuestionFrame(tk.Frame):
    """

    """
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

        self.message = tk.StringVar()
        self.message_label = ttk.Label(self, textvariable=self.message, font=("Arial", 10, "bold"))
        self.message_label.grid(row=11, column=0, columnspan=5, padx=10, pady=10)

    def add_question(self):
        """



        """
        options = []
        if self.difficulty_box.get() == "Please select a difficulty":
            self.message.set("Please select a difficulty")
            print("Please enter the difficulty")
            return

        if self.correct_answer.get() == "":
            self.message.set("Please select a correct answer")
            print("Please select a correct answer")
            return

        if self.question_entry.get() == "":
            self.message.set("Please enter the question")
            print("Please enter the question")
            return

        if self.option_entries[self.correct_answer.get()].get() == "":
            self.message.set("You can't select an empty option as the correct answer")
            print("You can't select an empty option as the correct answer")
            return

        # add lines into the quizzes.txt
        ascii_num = 97
        line = ""
        line += self.quiz_title.strip() + ";" + self.difficulty_box.get() + ";" + self.question_entry.get().strip() + ";["

        for i in self.option_entries.values():
            if i.get() == "":
                continue
            options.append(i.get().strip())

        if len(options) < 2:
            self.message.set("Please enter at least 2 options")
            print("Please enter at least 2 options")
            return

        for i in options:
            line += f'"{chr(ascii_num)}) {i}"'
            ascii_num += 1
            if i != options[-1]:
                line += ","

        line += "];"
        line += f"{self.correct_answer.get()}) {self.option_entries[self.correct_answer.get()].get().strip()}"
        print(line)
        self.question_lst.append(line)
        self.question_entry.delete(0, tk.END)
        for i in self.option_entries.values():
            i.delete(0, tk.END)
        self.message.set("Question added successfully")

    def done_button(self):
        if len(self.question_lst) == 0:
            self.message.set("Please enter at least one question")
            print("Please enter at least one question")
            return

        for line in self.question_lst:
            with open("data\quizzes.txt", "a") as f:
                f.write("\n" + line)
                f.flush()
        self.question_lst = []
        self.place_forget()
        self.manage_quiz_frame.message.set("Please restart the program to see the changes")
        self.manage_quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def cancel_button(self):
        self.question_lst = []
        self.place_forget()
        self.manage_quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# ---------------------------- View Quiz Frame ---------------------------- #

class ViewQuiz(tk.Frame):
    def __init__(self, parent, selected_quiz, selected_difficulty, manage_quiz_frame):
        super().__init__(parent)
        self.parent = parent
        self.selected_quiz = selected_quiz
        self.selected_difficulty = selected_difficulty
        self.manage_quiz_frame = manage_quiz_frame

        self.label = ttk.Label(self, text=f"Quiz: {self.selected_quiz.get_quiz_title()} | Difficulty: {self.selected_difficulty}", font=("Arial", 20, "bold"))
        self.label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # display the questions and radio buttons for each question
        self.questions = [x for x in self.selected_quiz.get_questions(self.selected_difficulty)]
        print(self.questions)

        self.selected_question = tk.StringVar()
        for index, question in enumerate(self.questions, start=1):
            question_label = ttk.Label(self, text=f"{index}) {question[0]}")
            question_label.grid(row=index, column=0, padx=10, pady=10, sticky='w')
            option_radio = ttk.Radiobutton(self,value=question, variable=self.selected_question)
            option_radio.grid(row=index, column=1, padx=10, pady=10, sticky='w')

        self.view_question_button = ttk.Button(self, text="View Question", command=self.view_question)
        self.view_question_button.grid(row=11, column=0, padx=10, pady=10)
        self.back_button = ttk.Button(self, text="Back", command=self.back_button)
        self.back_button.grid(row=11, column=1, padx=10, pady=10)

        self.message = tk.StringVar()
        self.message_label = ttk.Label(self, textvariable=self.message, font=("Arial", 10, "bold"))
        self.message_label.grid(row=12, column=0, columnspan=5, padx=10, pady=10)

    def view_question(self):
        if self.selected_question.get() == "":
            self.message.set("Please select a question")
            print("Please select a question")
            return
        selected_question = eval(self.selected_question.get())
        self.place_forget()
        view_question_frame = ViewQuestion(self.parent, selected_question, self)
        view_question_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def back_button(self):
        self.place_forget()
        self.manage_quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class ViewQuestion(tk.Frame):
    def __init__(self, parent, question, view_quiz_frame):
        super().__init__(parent)
        self.parent = parent
        self.question = question
        self.view_quiz_frame = view_quiz_frame

        self.label = ttk.Label(self, text="Question: " + self.question[0], font=("Arial", 15, "bold"), wraplength=1000)
        self.label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.options = self.question[1]
        for i in self.options:
            self.options_label = ttk.Label(self, text=i, font=("Arial", 15),
                                   wraplength=1000)
            print(self.options.index(i) + 3)
            self.options_label.grid(row=self.options.index(i) + 3, column=0, columnspan=2, padx=10, pady=10)

        self.correct_answer = self.question[2]
        self.correct_answer_label = ttk.Label(self, text="Correct Answer: " + self.correct_answer, font=("Arial", 13, "bold"))
        self.correct_answer_label.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

        self.back_button = ttk.Button(self, text="Back", command=self.back_button)
        self.back_button.grid(row=11, column=1, padx=10, pady=10)

    def back_button(self):
        self.place_forget()
        self.view_quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


if __name__ == "__main__":
    # DO NOT MODIFY THIS
    root = tk.Tk()
    root.geometry("1000x800")
    root.title("Manage Quiz")
    quiz_frame = ManageQuiz(root)
    quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place the frame in the center
    root.mainloop()









