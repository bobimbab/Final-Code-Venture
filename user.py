from datetime import date


class User:
    def __init__(self, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str | None = None, ph_num: str | None = None, role: str | None = None) -> None:
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
            role (str|None, optional): The role of the user. Defaults to None.
        """
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._password = password
        self._dob = dob
        self._email = email
        self._ph_num = ph_num
        self._role = role

    def get_full_name(self) -> str:
        """
        Getter for the user's full name.

        Returns:
            str: The user's full name.
        """
        return f"{self._first_name} {self._last_name}"

    def get_dob(self) -> date:
        """
        Getter for the date of birth attribute.

        Returns:
            date: The user's date of birth.
        """
        return self._dob

    def get_email(self) -> str | None:
        """
        Getter for the email attribute.

        Returns:
            str|None: The user's email address.
        """
        return self._email

    def get_ph_num(self) -> str | None:
        """
        Getter for the phone number attribute.

        Returns:
            str|None: The user's phone number.
        """
        return self._ph_num

    def get_username(self) -> str:
        """
        Getter for the username attribute.

        Returns:
            str: The user's username.
        """
        return self._username

    def get_password(self) -> str:
        """
        Getter for the password attribute.

        Returns:
            str: The user's password.
        """
        return self._password

    def get_role(self) -> str | None:
        """
        Getter for the role attribute.

        Returns:
            str|None: The user's role.
        """
        return self._role

    def set_password(self, new_password: str) -> None:
        """
        Set a new password for the user.

        Args:
            new_password (str): The new password to set.
        """
        self._password = new_password


class YoungLearner(User):
    def __init__(self, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str, ph_num: str, grade: int) -> None:
        super().__init__(first_name=first_name,
                         last_name=last_name,
                         username=username,
                         password=password,
                         dob=dob,
                         email=email,
                         ph_num=ph_num,
                         role="YL")
        self._grade = grade

    def get_grade(self) -> int:
        """
        Getter for the grade attribute.

        Returns:
            int: The young learner's grade.
        """
        return self._grade

    def get_details(self) -> str:
        """
        Returns a formatted string containing the details of the young learner.

        Returns:
            str: A string that contains the young learner's details.
        """
        return f"User: {self.get_full_name()}\n" \
               f"Username: {self.get_username()}\n" \
               f"Date of Birth: {self.get_dob()}\n" \
               f"Email: {self.get_email()}\n" \
               f"Phone Number: {self.get_ph_num()}\n" \
               f"Grade: {self.get_grade()}\n"


class Admin(User):
    def __init__(self, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str, ph_num: str) -> None:
        super().__init__(first_name, last_name, username, password, dob, email, ph_num, role="AD")


    def get_details(self) -> str:
        """
        Returns a formatted string containing the details of the admin.

        Returns:
            str: A string that contains the admin's details.
        """
        return f"User: {self.get_full_name()}\n" \
               f"Username: {self.get_username()}\n" \
               f"Date of Birth: {self.get_dob()}\n" \
               f"Email: {self.get_email()}\n" \
               f"Phone Number: {self.get_ph_num()}\n"
