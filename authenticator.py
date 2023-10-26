from user import User, YoungLearner, Admin


class Authenticator:

    def __init__(self, file_path="./user_data.txt"):
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


if __name__ == "__main__":
    # Feel free to amend this block while working or testing,
    # but any amendments here should be reverted upon submission.
    # You will not be assessed for any work here, but if any code
    # written here causes an error when running week11_interface.py,
    # then marks will be deducted.
    pass
