import tkinter as tk


class YoungLearner(tk.Frame):
    """
    A child class that inherits its parents (User).
    """
    def __init__(self, first_name: str, last_name: str, username: str, password: str, dob: str, date, email: str, ph_num: str, grade: int):
        super().__init__(first_name, last_name, username, password, dob, email, ph_num)
        self.grade = grade

    @staticmethod
    def register(self,users_dict: dict, first_name: str, last_name: str, username: str, password: str, dob: date,email: str, ph_num: str, grade: int) -> dict:
        """
        Registers a new young learner account in the system and add them to the user dictionary.
        """
        # Adds the newly registered user's information into the dictionary
        users_dict[username] = YoungLearner(first_name, last_name, username, password, dob, email, ph_num, grade)
        return users_dict
    def get_details(self) -> str:
        """
        Returns a formatted string containing the details of the young learner.
        Returns:
        str: A string that contains the young learner's details.
        """
        return f"User: {self.first_name} {self.last_name}\n" \
        f"Username: {self.username}\n" \
        f"Date of Birth: {self.dob}\n" \
        f"Email: {self.email}\n" \
        f"Phone Number: {self.ph_num}\n" \
        f"Grade: {self.grade}\n"