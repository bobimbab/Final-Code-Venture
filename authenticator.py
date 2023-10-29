from user import User, YoungLearner, Admin
from datetime import datetime


class Authenticator:

    def __init__(self, file_path="./data/user_data.txt"):
        self.file_path = file_path
        self.users = []
        self.load_users()

    def load_users(self):
        """
        Load list of users from the ./data/users.txt file
        :return: bool (True if successful, False otherwise)
        """
        try:
            with open(self.file_path, "r", encoding="utf8") as users_f:
                users_lines = users_f.readlines()
                for line in users_lines:
                    user_data = line.strip().split(",")
                    # DEBUGGING USE
                    print(user_data)
                    # (first_name, last_name, username, password, dob_str, email, ph_num, role, grade) = user_data
                    if len(user_data) == 9:
                    # if role == "YL":
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
        Logic for authenticating a login procedure
        :param input_username: str - username entered by the user
        :param input_password: str - password entered by the user
        :return: bool
        """
        for user_obj in self.users:
            if user_obj.get_username() == input_username:
                # If username is found
                if user_obj.get_password() == input_password:
                    # Passwords match and account is active
                    return user_obj
                else:
                    # Authentication fails
                    return False
        # Account does not exist
        return False

    def username_exists(self, input_username):
        """
        Check if the provided username exists in the system.
        :param input_username: str - username entered by the user
        :return: bool
        """
        for user_obj in self.users:
            if user_obj.get_username() == input_username:
                return True
        return False

    def register(self, username, password, first_name, last_name, dob, phone, email, grade):
        # Check if the username is unique
        if self.username_exists(username):
            return None  # Username already exists

        # Assuming User class has an appropriate constructor
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
        # Append the new user to the list of users
        self.users.append(new_user)

        # Save the updated user data to the file
        self.save_users()
        return new_user  # Return the newly registered user


if __name__ == "__main__":
    pass