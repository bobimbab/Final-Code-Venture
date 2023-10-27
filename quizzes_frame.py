import tkinter as tk
from tkinter import ttk
from quizzes import Quizzes


def load_quizzes() -> dict[str, Quizzes]:
    """
    This function creates a Quizzes object and adds questions to it.

    """
    all_quizzes = {}
    quiz = Quizzes("Python Data Types")
    quiz2 = Quizzes("Python Programming")
    # Adding multiple-choice questions and answers for the "Easy" difficulty

    # Adding multiple-choice questions and answers for the "Easy" difficulty
    quiz.add_question("Easy", "What data type is used to represent whole numbers in Python?",
                      ["a) int", "b) float", "c) str"], "a) int")
    quiz.add_question("Easy", "How do you create a string variable in Python?",
                      ["a) str = 'Hello, World!'", "b) string = 'Hello, World!'", "c) s = 'Hello, World!'"],
                      "a) str = 'Hello, World!'")

    # Adding multiple-choice questions and answers for the "Medium" difficulty
    quiz.add_question("Medium", "What is the result of the expression '5 / 2' in Python?", ["a) 2.5", "b) 2", "c) 2.0"],
                      "a) 2.5")
    quiz.add_question("Medium", "How do you check the data type of a variable in Python?",
                      ["a) using the 'datatype()' function", "b) using the 'type()' function",
                       "c) using the 'check_type()' function"], "b) using the 'type()' function")

    # Adding multiple-choice questions and answers for the "Hard" difficulty
    quiz.add_question("Hard", "What is the primary difference between a list and a tuple in Python?",
                      ["a) Lists are mutable, while tuples are immutable.",
                       "b) Lists can only store integers, while tuples can store any data type.",
                       "c) Lists are used for mathematical calculations, while tuples are used for text processing."],
                      "a) Lists are mutable, while tuples are immutable.")
    quiz.add_question("Hard", "What is the purpose of the 'None' data type in Python?",
                      ["a) It represents an empty string.", "b) It represents a missing or undefined value.",
                       "c) It is used for type conversion."], "b) It represents a missing or undefined value")
    quiz.add_question("Hard", "How do you define a dictionary in Python?",
                      ["a) {key1: value1, key2: value2}", "b) [key1: value1, key2: value2]",
                       "c) (key1: value1, key2: value2}"], "a) {key1: value1, key2: value2}")

    # Adding multiple-choice questions and answers for the "Easy" difficulty
    quiz2.add_question("Easy", "What is the result of 5 + 3 in Python?", "a) 8\nb) 15\nc) 53", "a) 8")
    quiz2.add_question("Easy", "Which data type is used to represent decimal numbers in Python?",
                       "a) int\nb) float\nc) str", "b) float")
    quiz2.add_question("Easy", "What is the primary purpose of the 'if' statement in Python?",
                       "a) To create a loop\nb) To define a function\nc) To make decisions in the code",
                       "c) To make decisions in the code")

    # Adding multiple-choice questions and answers for the "Medium" difficulty
    quiz2.add_question("Medium", "Which operator is used for exponentiation in Python?", "a) +\nb) *\nc) ^\nd) **",
                       "d) **")
    quiz2.add_question("Medium", "What is the primary purpose of a Python function?",
                       "a) To store data\nb) To perform a specific task or operation\nc) To create a class",
                       "b) To perform a specific task or operation")
    quiz2.add_question("Medium", "What is the correct way to comment multiple lines in Python?",
                       "a) /* This is a comment */\nb) // This is a comment\nc) ''' This is a comment '''",
                       "c) ''' This is a comment '''")

    # Adding multiple-choice questions and answers for the "Hard" difficulty
    quiz2.add_question("Hard", "What is the primary use of the 'global' keyword in Python?",
                       "a) To define a global variable\nb) To indicate a variable is local to a function\nc) To define a class attribute",
                       "a) To define a global variable")
    quiz2.add_question("Hard", "What is the purpose of the 'lambda' function in Python?",
                       "a) To create a list\nb) To define a class\nc) To create anonymous functions",
                       "c) To create anonymous functions")
    quiz2.add_question("Hard", "What is the result of the expression '10 / 3' in Python?", "a) 3\nb) 3.33\nc) 3.0",
                       "b) 3.33")

    all_quizzes[quiz.title] = quiz
    all_quizzes[quiz2.title] = quiz2
    return all_quizzes



class QuizzesMenuFrame(tk.Frame):
    """
    The class definition for the QuizzesFrame class.
    """

    def __init__(self,parent):
        """
        Constructor for the Interface class,
        the main window for the HCMS.
        :param title: str
        :param

        """
        super().__init__(parent)
        self.all_quizzes = load_quizzes()
        self.parent = parent

        style = ttk.Style()
        style.configure('W.TButton', font=
        ('calibri', 10, 'bold', 'underline'),
                        foreground='red')

        # Main Title
        self.title = tk.Label(self, text="CODE VENTURE", font=("Arial", 30, "bold"))
        self.title.pack(pady=10)  # Add vertical padding

        # image
        image_path = "images/quiz_logo.png"
        self.image = tk.PhotoImage(file=image_path)
        self.image = self.image.subsample(5)  # Change the factor as needed
        self.image_label = tk.Label(self, image=self.image)
        self.image_label.pack(pady=10)
        # resize

        # Choose quiz
        self.choose_quiz = tk.Label(self, text="Choose a quiz:", font=("Arial", 20))
        self.choose_quiz.pack(pady=10)  # Add vertical padding

        # show all quiz titles as buttons to choose
        self.selected_quiz = tk.StringVar()
        self.selected_quiz.set("")
        self.radio_buttons = []

        for quiz in self.all_quizzes:
            radio_button = tk.Radiobutton(self, text=quiz, font=("Arial", 15), variable=self.selected_quiz, value=quiz)
            radio_button.pack(pady=5)
            self.radio_buttons.append(radio_button)

        # Play button
        self.play_button = tk.Button(self, text="Play!", font=("Arial", 15), command=self.play_quiz)
        self.play_button.pack(pady=20)  # Add vertical padding

        # no quiz selected label
        self.warning_text = tk.StringVar()
        self.warning_text.set("")
        self.warning_label = tk.Label(self, textvariable=self.warning_text, font=("Arial", 15), fg="red").pack(pady=10)

        # Back button
        self.back_button = tk.Button(self, text="Return to Menu", font=("Arial", 15), command="")
        self.back_button.pack(pady=10)  # Add vertical padding

    def play_quiz(self):
        try:
            selected_quiz = self.all_quizzes[self.selected_quiz.get()]
        except KeyError:
            self.warning_text.set("Please select a quiz!")
            return

        print(selected_quiz)
        self.place_forget()
        choose_difficulty_frame = ChooseDifficultyFrame(self.parent, selected_quiz)
        choose_difficulty_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class ChooseDifficultyFrame(tk.Frame):
    """
    Frame to choose difficulty level
    """
    def __init__(self,parent,selected_quiz):
        super().__init__(parent)
        self.selected_quiz = selected_quiz
        self.parent = parent

        style = ttk.Style()
        style.configure("Easy.TButton", background="green", font=("Arial", 15, "bold"))
        style.configure("Medium.TButton", background="yellow", font=("Arial", 15, "bold"))
        style.configure("Hard.TButton", background="red", font=("Arial", 15, "bold"))

        # Main Title
        self.title = ttk.Label(self, text="PLEASE SELECT YOUR DIFFICULTY", font=("Arial", 30, "bold"))
        self.title.grid(row=0, column=0, columnspan=8, pady=10)  # Add vertical padding

        self.easy_button = ttk.Button(self, text="Easy", style="Easy.TButton", command="")
        self.easy_button.grid(row=1, column=1, padx=(10, 5), pady=15, sticky="w")

        self.medium_button = ttk.Button(self, text="Medium", style="Medium.TButton", command="")
        self.medium_button.grid(row=1, column=3, padx=5, pady=15)

        self.hard_button = ttk.Button(self, text="Hard", style="Hard.TButton", command="")
        self.hard_button.grid(row=1, column=5, padx=(5, 10), pady=15, sticky="e")


class PlayQuizFrame (tk.Frame):
    """
    The class definition for the PlayQuizFrame class.
    """
    def __init__(self, parent, selected_quiz):
        super().__init__(parent)

        self.selected_quiz = selected_quiz

        # Set up the frame title
        quiz_title = tk.Label(self, text=f"Quiz: {selected_quiz.title}", font=("Arial", 20, "bold"))
        quiz_title.pack(pady=10)

        # Display quiz instructions or information
        quiz_instructions = tk.Label(self, text="Quiz instructions go here", font=("Arial", 14))
        quiz_instructions.pack(pady=10)

        # Create question widgets
        for question in selected_quiz.questions:
            question_label = tk.Label(self, text=question, font=("Arial", 16))
            question_label.pack(pady=10)

            # Create answer options as radio buttons
            # For example, use a loop to create radio buttons for answer options
            # Option 1: tk.Radiobutton(...)
            # Option 2: tk.Radiobutton(...)
            # ...

        # Create a "Submit" button
        submit_button = tk.Button(self, text="Submit", font=("Arial", 14), command=self.submit_quiz)
        submit_button.pack(pady=20)

        # Back button to return to the quiz selection menu
        back_button = tk.Button(self, text="Return to Menu", font=("Arial", 14), command=self.return_to_menu)
        back_button.pack(pady=10)


        def submit_quiz(self):
            # Implement quiz submission logic
            pass


        def return_to_menu(self):
            # Implement the logic to return to the quiz selection menu
            pass


if __name__ == "__main__":
    # DO NOT MODIFY THIS
    root = tk.Tk()
    root.geometry("1000x800")
    root.title("CodeVenture Quizzes")
    quiz_frame = QuizzesMenuFrame(root)
    quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place the frame in the center
    root.mainloop()






