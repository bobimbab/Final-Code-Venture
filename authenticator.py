from user import User, YoungLearner, Admin
from datetime import datetime

class Authenticator:
    """
    The Authenticator class manages user authentication and user data handling.
    """

    def __init__(self, file_path="./data/user_data.txt"):
        """
        Initialize the Authenticator with a user data file.

        Args:
            file_path (str, optional): The path to the user data file. Defaults to "./data/user_data.txt".
        """
        self.file_path = file_path
        self.users = []
        self.load_users()

    def load_users(self):
        """
        Load the list of users from the user data file.

        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            with open(self.file_path, "r", encoding="utf8") as users_f:
                users_lines = users_f.readlines()
                for line in users_lines:
                    user_data = line.strip().split(",")

                    if len(user_data) == 9:
                        (first_name, last_name, username, password, dob_str, email, ph_num, role, grade) = user_data
                        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
                        user_obj = YoungLearner(first_name, last_name, username, password, dob, email, ph_num, grade)
                    else:
                        (first_name, last_name, username, password, dob_str, email, ph_num, role) = user_data
                        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
                        user_obj = Admin(first_name, last_name, username, password, dob, email, ph_num)
                    self.users.append(user_obj)
            return True
        except FileNotFoundError:
            print(f"The file \"{self.file_path}\" does not exist!")
            return False

    def save_users(self):
        """
        Save the list of users to the user data file.
        """
        try:
            with open(self.file_path, "w", encoding="utf8") as users_f:
                for user_obj in self.users:
                    dob_str = user_obj._dob.strftime("%Y-%m-%d")
                    if user_obj.get_role() == "YL":
                        role = "YL"
                        user_data = ",".join([
                            user_obj._first_name,
                            user_obj._last_name,
                            user_obj._username,
                            user_obj._password,
                            dob_str,
                            user_obj._email or "",  # Handle None
                            user_obj._ph_num or "",  # Handle None
                            role,
                            str(user_obj._grade)
                        ])
                    else:
                        role = "AD"
                        user_data = ",".join([
                            user_obj._first_name,
                            user_obj._last_name,
                            user_obj._username,
                            user_obj._password,
                            dob_str,
                            user_obj._email or "",  # Handle None
                            user_obj._ph_num or "",  # Handle None
                            role
                        ])
                    users_f.write(user_data + "\n")
        except FileNotFoundError:
            print(f"The file \"{self.file_path}\" does not exist.")

    def authenticate(self, input_username, input_password):
        """
        Authenticate a user's login procedure.

        Args:
            input_username (str): Username entered by the user.
            input_password (str): Password entered by the user.

        Returns:
            bool: User object if authentication is successful, False otherwise.
        """
        for user_obj in self.users:
            if user_obj.get_username() == input_username:
                if user_obj.get_password() == input_password:
                    return user_obj
                else:
                    return False
        return False

    def authenticate_forgot_pw(self, input_email, input_ph_num, new_password):
        """
        Authenticate a user's password reset procedure.

        Args:
            input_email (str): Email entered by the user.
            input_ph_num (str): Phone number entered by the user.
            new_password (str): New password to set.

        Returns:
            bool: User object if authentication is successful, False otherwise.
        """
        for user_obj in self.users:
            if user_obj.get_email() == input_email:
                if user_obj.get_ph_num() == input_ph_num:
                    user_obj.set_password(new_password)
                    self.save_users()
                    return user_obj
                else:
                    return False
        return False

    def username_exists(self, input_username):
        """
        Check if the provided username exists in the system.

        Args:
            input_username (str): Username entered by the user.

        Returns:
            bool: True if the username exists, False otherwise.
        """
        for user_obj in self.users:
            if user_obj.get_username() == input_username:
                return True
        return False

    def register(self, username, password, first_name, last_name, dob, phone, email, grade):
        """
        Register a new user.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.
            first_name (str): The first name of the new user.
            last_name (str): The last name of the new user.
            dob (date): The date of birth of the new user.
            phone (str): The phone number of the new user.
            email (str): The email address of the new user.
            grade (int): The grade of the new user.

        Returns:
            User|None: The newly registered user or None if the username already exists.
        """
        if self.username_exists(username):
            return None

        new_user = YoungLearner(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            dob=dob,
            email=email,
            ph_num=phone,
            grade=grade
        )

        self.users.append(new_user)
        self.save_users()
        return new_user