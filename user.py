from datetime import date


class User:

    def __init__(self, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str | None = None, ph_num: str | None = None) -> None:
        """
        Initialize a User object with the given attributes.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            username (str): The username of the user.
            password (str): The password of the user.
            dob (date): The date of birth of the user.
            email (str|None, optional): The email address of the user. Defaults to None.
            ph_num (str|None, optional): The phone number of the user. Defaults to None.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.dob = dob
        self.email = email
        self.ph_num = ph_num

    @staticmethod
    def register(users_dict: dict, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str | None = None, ph_num: str | None = None):
        """
        Registers the user according to the parameters provided.
        Returns true if the registration is successful, and false if otherwise

        Args:
            users_dict (dict): The dictionary of users where the new user will be registered.
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            username (str): The username of the user.
            password (str): The password the user.
            dob (date): The date of user.
            email (str|None, optional): The email address of the user. Defaults to None.
            ph_num (str|None, optional): The phone number of the user. Defaults to None.

        Returns:
            bool: A boolean that represents whether the registration was successful or not.
        """
        if username not in users_dict:  # if username not found in dictionary, add it in
            users_dict[username] = User(first_name, last_name, username, password, dob, email, ph_num)
            return True
        return False

    @staticmethod
    def authenticate(users_dict: dict, username: str, password: str) -> bool:
        """
        Authenticates the user based on their username and password

        Arguments:
            users_dict (dict): The dictionary of users to authenticate against.
            username (str): A string that represents the username of the user.
            password (str): A string that represents the password of the user.

        Returns:
            bool: A boolean that states whether the user has been authenticated successfully
        """
        if username not in users_dict or users_dict[username].password != password:
            return False
        return True

    def get_details(self) -> str:
        """
        Retrieves all user details in a formatted string.

        Returns:
            str: A formatted string containing user details.
        """
        return f"User: {self.first_name} {self.last_name}\n" \
               f"Username: {self.username}\n" \
               f"Date of Birth: {self.dob}\n" \
               f"Email: {self.email}\n" \
               f"Phone Number: {self.ph_num}\n"

    def set_password(self, new_password) -> None:
        self.password = new_password


class YoungLearner(User):
    """
    A child class that inherits its parents (User).
    """

    def __init__(self, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str, ph_num: str, grade: int):
        super().__init__(first_name, last_name, username, password, dob, email, ph_num)
        self.grade = grade

    @staticmethod
    def register(users_dict: dict, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str, ph_num: str, grade: int) -> dict:
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


class Admin(User):
    """
    A child class that inherits its parents (User).
    """
    def __init__(self, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str, ph_num: str):
        super().__init__(first_name, last_name, username, password, dob, email, ph_num)

    @staticmethod
    def register(users_dict: dict, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str, ph_num: str) -> dict:
        """
        Registers a new admin in the system and add them to the user dictionary.

        Args:
            users_dict (dict): The dictionary users where the new admin will be registered.
            first_name (str): The first name of the admin.
            last_name (str): The last name of the admin.
            username (str): The username of the admin.
            password (str): The password of the.
            dob (date): The date of birth of the admin.
            email (str): The email of the admin.
            ph_num (str): The phone number of the admin.

        Returns:
            user dictionary.
        """
        users_dict[username] = Admin(first_name, last_name, username, password, dob, email, ph_num)
        return users_dict

    def get_details(self) -> str:
        """
        Returns a formatted string containing the details of the admin.

        Returns:
            str: A string that contains the admin's details.
        """
        return f"User: {self.first_name} {self.last_name}\n" \
               f"Username: {self.username}\n" \
               f"Date of Birth: {self.dob}\n" \
               f"Email: {self.email}\n" \
               f"Phone Number: {self.ph_num}\n"
