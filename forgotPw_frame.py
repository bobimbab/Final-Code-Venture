import tkinter as tk
from authenticator import Authenticator
from user import User, YoungLearner

class ForgotPwFrame(tk.Frame):
    """
            The class definition for the ForgotPwFrame class.
            """

    def __init__(self, master, login_frame):
        """
        Constructor for the ForgotPwFrame class.
        :param master: Tk object; the main window that the
                       forgot password frame is to be contained.
        """
        super().__init__(master=master)
        self.master = master
        self.login_frame = login_frame

        # Label containing heading indicating the current frame is a password resetting page
        forgot_pw_title = tk.Label(master=self,
                               text="Trouble Logging in?",
                               font=("Arial", 30))
        # regis_title.grid()
        forgot_pw_title.grid(row=1,columnspan=2, padx=10, pady=10)

        # Label containing description
        forgot_pw_desc = tk.Label(master=self,
                                  text="Enter your details for verification to reset password successfully.",
                                  font=("Times New Romans", 12))
        # regis_title.grid()
        forgot_pw_desc.grid(row=2, columnspan=2, padx=10, pady=10)

        # Label to ask user for Email
        email_label = tk.Label(master=self, text="Email:")
        email_label.grid(row=4, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to email
        self.email = tk.StringVar()
        self.email_entry = tk.Entry(master=self, textvariable=self.email)
        self.email_entry.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for their phone number
        ph_num_label = tk.Label(master=self, text="Phone number:")
        ph_num_label.grid(row=5, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to phone number
        self.ph_num = tk.StringVar()
        self.ph_num_entry = tk.Entry(master=self, textvariable=self.ph_num)
        self.ph_num_entry.grid(row=5, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for Password
        password_label = tk.Label(master=self, text="New Password:")
        password_label.grid(row=6, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to password, password entry will be hidden
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(master=self, textvariable=self.password,
                                       show="●")
        self.password_entry.grid(row=6, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user to confirm their new Password
        password_label = tk.Label(master=self, text="Confirm New Password:")
        password_label.grid(row=7, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to new password, new password entry will be hidden
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(master=self, textvariable=self.password,
                                       show="●")
        self.password_entry.grid(row=7, column=1, sticky=tk.W, padx=10, pady=10)

        # Confirm button for changing password
        confirm_button = tk.Button(master=self, text="Confirm", command=self.authenticate_info)
        confirm_button.grid(row=7, column=1, padx=100)

        # Back to login page button
        # back_button = tk.Button(self, text="Back", command=lambda: login_frame.place())
        back_button = tk.Button(master=self, text="Back", command=self.return_menu)
        # back_button = tk.Button(master=self, text="Back")
        back_button.grid(row=0, column=0, sticky=tk.NW)

        # Variable and label to inform user of password outcome
        self.pw_outcome_text = tk.StringVar()
        pw_outcome_message = tk.Label(master=self, textvariable=self.pw_outcome_text)
        pw_outcome_message.grid(row=8, columnspan=2, padx=10, pady=10)


    def return_menu(self):
        """
        Returns to previous menu
        """
        self.place_forget() # forget a widget from the parent widget or screen
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Positions the frame and is anchored in the
                                                                       # \middle
        # DEBUGGING USE
        print("Currently in login frame")

    def authenticate_info(self):
        """
        Frontend function for the authentication procedure.
        This is invoked when the login button is clicked.
        :return: None
        """
        authenticator = Authenticator()
        auth_res = authenticator.authenticate_forgot_pw(self.email_entry.get(), self.ph_num.get())

        if isinstance(auth_res, User):

            if isinstance(auth_res, YoungLearner):  # Check if the user is a YoungLearner
                self.pw_outcome_text.set("Password changed successfully!")

        else:
            self.pw_outcome_text.set("Fail to change password")

def main():
    root = tk.Tk()
    root.title("Forgot password Example")

    x_frame = tk.Frame(root)  # Create a login frame
    x_frame.grid(row=0, padx=10, pady=10)

    y_frame = ForgotPwFrame(root, x_frame)
    y_frame.grid(row=0, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()