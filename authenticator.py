from user import User, YoungLearner, Admin


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
                    (first_name,
                     last_name,
                     username,
                     password,
                     dob,
                     email,
                     ph_num,
                     role,
                     grade) = line.strip().split(",")
                    if role == "YL":
                        user_obj = YoungLearner(first_name=first_name,
                                                last_name=last_name,
                                                username=username,
                                                password=password,
                                                dob=dob,
                                                email=email,
                                                ph_num=ph_num,
                                                grade=grade)
                    else:
                        user_obj = Admin(first_name=first_name,
                                         last_name=last_name,
                                         username=username,
                                         password=password,
                                         dob=dob,
                                         email=email,
                                         ph_num=ph_num)
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
                    # Create a comma-separated line with user data
                    user_data = ",".join([user_obj.__first_name,
                                          user_obj.__last_name,
                                          user_obj.__username,
                                          user_obj.__password,
                                          user_obj.__dob,
                                          user_obj.__email,
                                          user_obj.__ph_num,
                                          user_obj.__role,
                                          user_obj.__grade])
                    users_f.write(user_data + "\n")
        except FileNotFoundError:
            print(f"The file \"{self.file_path}\" does not exist!")

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

    def register(self, username, password, firstname, lastname, dob, phone, email, grade):
        # Check if the username is unique
        if self.username_exists(username):
            return None  # Username already exists

        # Assuming User class has an appropriate constructor
        new_user = User(username, password, firstname, lastname, dob, phone, email, grade)
        self.users.append(new_user)  # Add the new user to the list (replace with database storage)
        return new_user  # Return the newly registered user


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
