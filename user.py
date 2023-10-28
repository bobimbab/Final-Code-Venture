from datetime import date


class User:

    def __init__(self, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str | None = None, ph_num: str | None = None, role=None) -> None:
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
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__password = password
        self.__dob = dob
        self.__email = email
        self.__ph_num = ph_num
        self.__role = role

    def get_full_name(self):
        """
        Getter for the user's full name.
        :return: str
        """
        return f"{self.__first_name} {self.__last_name}"

    def get_dob(self):
        """
        Getter for the date of birth attribute.
        :return: date
        """
        return self.__dob

    def get_email(self):
        """
        Getter for the email attribute.
        :return: str
        """
        return self.__email

    def get_ph_num(self):
        """
        Getter for the phone number attribute.
        :return: str
        """
        return self.__ph_num
    def get_username(self):
        """
        Getter for the username attribute.
        :return: str
        """
        return self.__username

    def get_password(self):
        """
        Getter for the password attribute.
        :return: str
        """
        return self.__password

    def get_role(self):
        """
        Getter for the role attribute.
        :return: str
        """
        return self.__role

    def set_password(self, new_password) -> None:
        self.__password = new_password


class YoungLearner(User):
    """
    A child class that inherits its parents (User).
    """

    def __init__(self, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str, ph_num: str, grade: int):
        super().__init__(first_name=first_name,
                         last_name=last_name,
                         username=username,
                         password=password,
                         dob=dob,
                         email=email,
                         ph_num=ph_num,
                         role="YL")
        self.__grade = grade



    def get_details(self) -> str:
        """
        Returns a formatted string containing the details of the young learner.

        Returns:
            str: A string that contains the young learner's details.
        """
        return f"User: {self.__first_name} {self.__last_name}\n" \
               f"Username: {self.__username}\n" \
               f"Date of Birth: {self.__dob}\n" \
               f"Email: {self.__email}\n" \
               f"Phone Number: {self.__ph_num}\n" \
               f"Grade: {self.__grade}\n"


class Admin(User):
    """
    A child class that inherits its parents (User).
    """
    def __init__(self, first_name: str, last_name: str, username: str, password: str, dob: date,
                 email: str, ph_num: str):
        super().__init__(first_name=first_name,
                         last_name=last_name,
                         username=username,
                         password=password,
                         dob=dob,
                         email=email,
                         ph_num=ph_num,
                         role="AD")

    def get_details(self) -> str:
        """
        Returns a formatted string containing the details of the admin.

        Returns:
            str: A string that contains the admin's details.
        """
        return f"User: {self.__first_name} {self.__last_name}\n" \
               f"Username: {self.__username}\n" \
               f"Date of Birth: {self.__dob}\n" \
               f"Email: {self.__email}\n" \
               f"Phone Number: {self.__ph_num}\n"
