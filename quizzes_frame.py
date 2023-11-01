import tkinter as tk
import random
from animations import AnimatedButton, FadingLabel
from tkinter import ttk
from quizzes import Quizzes


class QuizzesMenuFrame(tk.Frame):
    """
    The frame that contains the quiz menu.
    """
    def __init__(self,parent,young_learner_frame):
        super().__init__(parent)
        self.all_quizzes = Quizzes.load_quizzes()
        self.parent = parent
        self.young_learner_frame = young_learner_frame

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
        self.back_button = tk.Button(self, text="Return to Menu", font=("Arial", 15), command=self.back_to_menu)
        self.back_button.pack(pady=10)  # Add vertical padding

    def play_quiz(self):
        try:
            selected_quiz = self.all_quizzes[self.selected_quiz.get()]
        except KeyError:
            self.warning_text.set("Please select a quiz!")
            return

        self.place_forget()
        choose_difficulty_frame = ChooseDifficultyFrame(self.parent, selected_quiz,self)
        choose_difficulty_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def back_to_menu(self):
        self.place_forget()
        self.young_learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class ChooseDifficultyFrame(tk.Frame):
    """
    Frame to choose difficulty level
    """
    def __init__(self,parent,selected_quiz,quiz_menu):
        super().__init__(parent)
        self.selected_quiz = selected_quiz
        self.quiz_menu = quiz_menu
        self.parent = parent

        style = ttk.Style()
        style.configure("Easy.TButton", background="green", font=("Arial", 15, "bold"))
        style.configure("Medium.TButton", background="yellow", font=("Arial", 15, "bold"))
        style.configure("Hard.TButton", background="red", font=("Arial", 15, "bold"))

        # Main Title
        self.title = ttk.Label(self, text="PLEASE SELECT YOUR DIFFICULTY", font=("Arial", 30, "bold"))
        self.title.grid(row=0, column=0, columnspan=8, pady=10)  # Add vertical padding

        if self.selected_quiz.get_number_of_easy_questions() > 0:
            self.easy_button = ttk.Button(self, text="Easy", style="Easy.TButton", command=lambda: self.set_difficulty(1))
            self.easy_button.grid(row=1, column=1, padx=(10, 5), pady=15, sticky="w")

        if self.selected_quiz.get_number_of_medium_questions() > 0:
            self.medium_button = ttk.Button(self, text="Medium", style="Medium.TButton", command=lambda: self.set_difficulty(2))
            self.medium_button.grid(row=1, column=3, padx=5, pady=15)

        if self.selected_quiz.get_number_of_hard_questions() > 0:
            self.hard_button = ttk.Button(self, text="Hard", style="Hard.TButton", command=lambda: self.set_difficulty(3))
            self.hard_button.grid(row=1, column=5, padx=(5, 10), pady=15, sticky="e")

    def set_difficulty(self,choice):
        self.selected_quiz.reset_quiz()
        self.selected_quiz.set_difficulty(choice)
        self.place_forget()
        play_quiz_frame = PlayQuizFrame(self.parent, self.selected_quiz,self.quiz_menu)
        play_quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class PlayQuizFrame (tk.Frame):
    """
    The class definition for the PlayQuizFrame class.
    """
    def __init__(self, parent, selected_quiz,quiz_menu):
        super().__init__(parent)
        self.quiz_menu = quiz_menu
        self.parent = parent
        self.selected_quiz = selected_quiz
        self.score = 0 # Initialise score to 0

        # Set up the frame title
        quiz_title = tk.Label(self, text=self.selected_quiz.get_quiz_title(), font=("Arial", 20, "bold"))
        quiz_title.pack(pady=10)

        # Display quiz instructions and information
        self.quiz_question = tk.StringVar()
        try:
            self.quiz_question.set(self.selected_quiz.current_question)
            self.question = tk.Label(self, textvariable=self.quiz_question, font=("Arial", 14))
            self.question.pack(pady=10)

            # Display options
            self.options = self.selected_quiz.current_options
            self.option_buttons = []

            for options in self.options:
                option = AnimatedButton(self, text=options, font=("Arial", 14), command=lambda o=options: self.submit_quiz(o))
                option.pack(pady=5)
                self.option_buttons.append(option)
        except IndexError:
            self.error = tk.Label(self, text="No questions in this quiz/difficulty!", font=("Arial", 14))
            self.error.pack(pady=10)

        # Back button to return to the quiz selection menu
        back_button = tk.Button(self, text="Return to Menu", font=("Arial", 14), command=self.return_to_menu)
        back_button.pack(pady=10)

    def update_options(self, new_options):
        self.options = new_options
        for button, option_text in zip(self.option_buttons, new_options):
            # change the text on the button
            button.config(text=option_text)
            # ensure that the button updates its value before calling the sumbit_quiz()
            button.config(command=lambda o=option_text: self.submit_quiz(o))

        # ensure that buttons from the excess buttons are removed
        for button in self.option_buttons[len(new_options):]:
            button.pack_forget()

    def submit_quiz(self,answer):
        # Implement quiz submission logic
        self.validate_answer(answer)
        try:
            self.selected_quiz.next_question()
        except IndexError:
            self.place_forget()
            play_quiz_frame = QuizResultsFrame(self.parent, self.selected_quiz, self.quiz_menu,self.score)
            play_quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.quiz_question.set(f"{self.selected_quiz.current_question}")
        self.update_options(self.selected_quiz.current_options)

    def validate_answer(self, answer):
        # Implement the logic to validate the answer
        print("your answer",answer)
        print("current answer",self.selected_quiz.current_answer)
        if answer == self.selected_quiz.current_answer:
            self.score += 1
            fading_label = FadingLabel(self.parent, text="Correct", font=("Arial", 20,"bold"))
            fading_label.pack(pady=10)
        else:
            fading_label = FadingLabel(self.parent, text="Incorrect", font=("Arial", 20,"bold"))
            fading_label.pack(pady=10)

    def return_to_menu(self):
        # Implement the logic to return to the quiz selection menu
        self.score = 0
        self.selected_quiz.reset_quiz()
        self.place_forget()
        self.quiz_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class QuizResultsFrame(tk.Frame):
    """
    The class definition for the QuizResultsFrame class.
    """
    message = ["GREAT JOB!", "GOOD JOB!", "NICE!", "WELL DONE!"]

    def __init__(self, parent, selected_quiz,quiz_menu,player_score):
        super().__init__(parent)
        self.quiz_menu = quiz_menu
        self.score = player_score
        self.selected_quiz = selected_quiz
        self.parent = parent

        # Set up the frame title
        quiz_title = tk.Label(self, text=random.choice(self.message), font=("Arial", 20, "bold"))
        quiz_title.pack(pady=10)

        score_label = tk.Label(self, text="Your Score", font=("Arial", 14))
        score_label.pack(pady=10)

        # Display quiz results
        self.quiz_results = tk.StringVar()
        self.quiz_results.set(f"{self.score} out of {self.selected_quiz.get_number_of_questions}" )
        self.results = tk.Label(self, textvariable=self.quiz_results, font=("Arial", 14))
        self.results.pack(pady=10)

        # Back button to return to the quiz selection menu
        self.back_button = tk.Button(self, text="Return to Menu", font=("Arial", 14), command=self.return_to_menu)
        self.back_button.pack(pady=10)

    def return_to_menu(self):
        # Implement the logic to return to the quiz selection menu
        self.score = 0
        self.selected_quiz.reset_quiz()
        self.place_forget()
        self.quiz_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


if __name__ == "__main__":
    # DO NOT MODIFY THIS
    root = tk.Tk()
    root.geometry("1000x800")
    root.title("CodeVenture Quizzes")
    quiz_frame = QuizzesMenuFrame(root)
    quiz_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Place the frame in the center
    root.mainloop()
