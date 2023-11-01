import tkinter as tk
from tkcalendar import Calendar
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime
from user import User, YoungLearner, Admin
from authenticator import Authenticator

class RegisterFrame(tk.Frame):

    def __init__(self, master, login_frame):
        """
        Constructor for the RegisterFrame class.
        :param master: Tk object; the main window that the
                       register frame is to be contained.
        """
        super().__init__(master=master)
        self.master = master
        self.login_frame = login_frame

        # Label containing heading indicating the current frame is a account registration page
        regis_title = tk.Label(master=self,
                               text="Welcome to CodeVenture!",
                               font=("Arial Bold", 30))
        # regis_title.grid()
        regis_title.grid(row=1, columnspan=2, padx=10, pady=10)

        # Label to ask user for Username
        username_label = tk.Label(master=self, text="Username:")
        username_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry for username
        self.username = tk.StringVar()
        self.username_entry = tk.Entry(master=self, textvariable=self.username)
        self.username_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for Password
        password_label = tk.Label(master=self, text="Password:")
        password_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to password, password entry will be hidden
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(master=self, textvariable=self.password,
                                       show="●")
        self.password_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for First Name
        first_name_label = tk.Label(master=self, text="First Name:")
        first_name_label.grid(row=4, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry for First Name
        self.first_name = tk.StringVar()
        self.first_name_entry = tk.Entry(master=self, textvariable=self.first_name)
        self.first_name_entry.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for Last Name
        last_name_label = tk.Label(master=self, text="Last Name:")
        last_name_label.grid(row=5, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry for Last Name
        self.last_name = tk.StringVar()
        self.last_name_entry = tk.Entry(master=self, textvariable=self.last_name)
        self.last_name_entry.grid(row=5, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for their date of birth
        dob_label = tk.Label(master=self, text="Date of birth:")
        dob_label.grid(row=6, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to date of birth
        self.dob_entry = DateEntry(self, selectmode="day", locale="en_UK", date_pattern="yyyy-mm-dd")
        self.dob_entry.grid(row=6, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for their phone number
        ph_num_label = tk.Label(master=self, text="Phone number:")
        ph_num_label.grid(row=7, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to phone number
        self.ph_num_entry = tk.StringVar()
        self.ph_num_entry = tk.Entry(master=self, textvariable= self.ph_num_entry)
        self.ph_num_entry.grid(row=7, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for their email
        email_label = tk.Label(master=self, text="Email:")
        email_label.grid(row=8, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to email
        self.email_entry = tk.StringVar()
        self.email_entry = tk.Entry(master=self, textvariable=self.email_entry)
        self.email_entry.grid(row=8, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for their grade
        grade_label = tk.Label(master=self, text="Grade:")
        grade_label.grid(row=9, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to grade
        self.grade_entry = tk.StringVar()
        self.grade_entry = tk.Entry(master=self, textvariable=self.grade_entry)
        self.grade_entry.grid(row=9, column=1, sticky=tk.W, padx=10, pady=10)

        # Button to register
        register_button = tk.Button(master=self, text="Register", command=self.authenticate_register)
        register_button.grid(row=10,column=0, columnspan=2, padx=10, pady=10)

        # Back to login page button
        back_button = tk.Button(master=self, text="Back", command=self.return_menu)
        back_button.grid(row=0, column=0, sticky=tk.NW)

        # Variable and label to inform user of registration outcome
        self.registration_text = tk.StringVar()
        registration_message = tk.Label(master=self, textvariable=self.registration_text)
        registration_message.grid(row=11, columnspan=2, padx=10, pady=10)

    def return_menu(self):
        """
        Returns to previous menu
        """
        self.place_forget() # forget a widget from the parent widget or screen
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Positions the frame and is anchored in the
                                                                       # \middle

    def authenticate_register(self):
        """
        Frontend function for the authentication procedure.
        This is invoked when the register button is clicked.
        :return: None
        """

        # Extract user registration information from the input fields
        username = self.username_entry.get()
        password = self.password_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()

        # Convert the dob to a date object
        dob_str = self.dob_entry.get()
        try:
            dob_date = datetime.strptime(dob_str, "%Y-%m-%d").date()
        except ValueError:
            # Display an error message if the date format is invalid
            messagebox.showerror("Registration Error", "Invalid date of birth format. Use YYYY-MM-DD")
            return

        phone = self.ph_num_entry.get()
        email = self.email_entry.get()
        grade = self.grade_entry.get()

        # Check if any of the fields are empty
        if not username or not password or not first_name or not last_name or not dob_date \
                or not phone or not email or not grade:
            # Display an error message if any fields are left blank
            messagebox.showerror("Registration Error", "Please fill in all registration fields.")
        else:
            authenticator = Authenticator()
            auth_res = authenticator.username_exists(username)  # Check if the username already exists

            if auth_res:
                messagebox.showerror("Error:", "Username already exists. Please pick another username")

            else:
                # Attempt to register the user with the provided information
                user = authenticator.register(username, password, first_name, last_name, dob_date, phone, email, grade)

                if user:
                    # Display a success message if registration is successful
                    self.registration_text.set("Registration successful! You may now log in from the login page.")

                    # Clear input fields upon successful registration
                    self.username_entry.delete(0, 'end')
                    self.password_entry.delete(0, 'end')
                    self.first_name_entry.delete(0, 'end')
                    self.last_name_entry.delete(0, 'end')
                    self.dob_entry.set_date(None)  # Clear the DateEntry widget
                    self.ph_num_entry.delete(0, 'end')
                    self.email_entry.delete(0, 'end')
                    self.grade_entry.delete(0, 'end')

                else:
                    # Display an error message if registration fails
                    self.registration_text.set("Failed to register. Please try again.")
                    messagebox.showerror("Registration Error", "Failed to register. Please try again.")

def main():
    root = tk.Tk()
    root.title("Register Example")

    login_frame = tk.Frame(root)  # Create a login frame
    login_frame.grid(row=0, padx=10, pady=10)

    register_frame = RegisterFrame(root, login_frame)
    register_frame.grid(row=0, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()