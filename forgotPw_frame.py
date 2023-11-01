import tkinter as tk
from authenticator import Authenticator
from user import User, YoungLearner
from tkinter import messagebox


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
        forgot_pw_title.grid(row=1, columnspan=2, padx=10, pady=10)

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
        confirm_password_label = tk.Label(master=self, text="Confirm New Password:")
        confirm_password_label.grid(row=7, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to new password, new password entry will be hidden
        self.confirm_password = tk.StringVar()
        self.confirm_password_entry = tk.Entry(master=self, textvariable=self.confirm_password,
                                               show="●")
        self.confirm_password_entry.grid(row=7, column=1, sticky=tk.W, padx=10, pady=10)

        # Confirm button for changing password
        confirm_button = tk.Button(master=self, text="Confirm", command=self.authenticate_info)
        confirm_button.grid(row=7, column=1, padx=100)

        # Back to login page button
        back_button = tk.Button(master=self, text="Back", command=self.return_menu)
        back_button.grid(row=0, column=0, sticky=tk.NW)

        # Variable and label to inform user of password outcome
        self.pw_outcome_text = tk.StringVar()
        pw_outcome_message = tk.Label(master=self, textvariable=self.pw_outcome_text)
        pw_outcome_message.grid(row=8, columnspan=2, padx=10, pady=10)

    def return_menu(self):
        """
        Returns to previous menu
        """
        self.place_forget()  # forget a widget from the parent widget or screen
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Positions the frame and is anchored in the

    def authenticate_info(self):
        """
            This function is invoked when the "Confirm" button is clicked to change the password.
            It collects input values, validates them, checks if the "New Password" and "Confirm Password" match,
            and proceeds with the password change if all checks pass.

        """
        # Get the values from the input fields
        email = self.email_entry.get()
        ph_num = self.ph_num_entry.get()
        password = self.password_entry.get()

        # Add this line to get the value of the confirm password field
        confirm_password = self.confirm_password_entry.get()

        # Check if any of the fields is empty
        if not email or not ph_num or not password:
            messagebox.showerror("Error", "All fields are required")
            return  # Don't proceed further if any field is empty

        # Check if the "New Password" and "Confirm Password" fields match
        if password != confirm_password:
            messagebox.showerror("Error", "Password and Confirm Password do not match.")
            return

        # Continue with the authentication procedure
        authenticator = Authenticator()
        auth_res = authenticator.authenticate_forgot_pw(email, ph_num, password)

        # If authentication is successful
        if isinstance(auth_res, User):

            # If user is younglearner
            if isinstance(auth_res, YoungLearner):
                self.pw_outcome_text.set("Password changed successfully!")
        else:
            self.pw_outcome_text.set("Failed to change password. Invalid details.")


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
