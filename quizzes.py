import random
class Quizzes:
    difficulties = ["Easy", "Medium", "Hard"]

    def __init__(self, title: str):
        self.quiz_id = random.randint(1000, 9999)
        self.title = title
        self.easy_questions = []  # Initialize with empty dictionaries for questions
        self.medium_questions = []
        self.hard_questions = []
        self.player_difficulty = None
        self.questions = None

        # State variable to keep track of the current question index
        self.current_question_index = 0

    @classmethod
    def create_quiz(cls, title: str):
        """
        Create a quiz object with the given title
        :param title:
        :return:
        """
        pass

    def get_quiz_title(self):
        return self.title

    @property
    def available_difficulties(self):
        return self.difficulties

    @property
    def selected_difficulty(self):
        return self.player_difficulty

    @property
    def question_list(self):
        return f"{self.player_difficulty} Questions:\n{self.format_questions(self.questions)}\n"

    def add_question(self, difficulty: str, question: str, options: list[str], answer: str) -> None:
        """Add question into the quiz"""
        if difficulty == "Easy":
            self.easy_questions.append((question, options, answer))
        elif difficulty == "Medium":
            self.medium_questions.append((question, options, answer))
        elif difficulty == "Hard":
            self.hard_questions.append((question, options, answer))

    def set_difficulty(self, choice: int) -> None:
        if choice in [1, 2, 3]:
            self.player_difficulty = self.difficulties[choice - 1]

        if choice == 1:
            self.questions = self.easy_questions
        elif choice == 2:
            self.questions = self.medium_questions
        elif choice == 3:
            self.questions = self.hard_questions

    @property
    def current_question(self) -> str:
        return self.questions[self.current_question_index][0]

    @property
    def current_options(self) -> list:
        return self.questions[self.current_question_index][1]

    @property
    def current_answer(self) -> str:
        return self.questions[self.current_question_index][2]

    @property
    def get_number_of_questions(self) -> int:
        return len(self.questions)

    def get_number_of_easy_questions(self) -> int:
        return len(self.easy_questions)

    def get_number_of_medium_questions(self) -> int:
        return len(self.medium_questions)

    def get_number_of_hard_questions(self) -> int:
        return len(self.hard_questions)

    def next_question(self) -> None:
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
        else:
            raise IndexError("No more questions!")

    def reset_quiz(self):
        self.player_difficulty = None
        self.current_question_index = 0
        self.questions = None

    def __str__(self):
        return f"Quiz Title: {self.title}\n" \
               f"Easy Questions:\n{self.format_questions(self.easy_questions)}\n" \
               f"Medium Questions:\n{self.format_questions(self.medium_questions)}\n" \
               f"Hard Questions:\n{self.format_questions(self.hard_questions)}\n"

    def format_questions(self,questions):
        formatted_questions = "\n".join([f"  - {question[0]}" for question in questions])
        return formatted_questions


if __name__ == "__main__":
    # sample data
    quiz = Quizzes("Python Data Types")

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

    # print(quiz)
    quiz.set_difficulty(1)
    print(quiz.current_options)








