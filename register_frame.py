import tkinter as tk
from tkcalendar import Calendar
from tkcalendar import DateEntry

from user import User, YoungLearner, Admin
from authenticator import Authenticator

class RegisterFrame(tk.Frame):

    def __init__(self, master, login_frame):
        """
        Constructor for the LoginFrame class.
        :param master: Tk object; the main window that the
                       login frame is to be contained.
        """
        super().__init__(master=master)
        self.master = master
        self.login_frame = login_frame
        # self.master.geometry(f"{width}x{height}")

        # Logo image for the login page
        canvas = tk.Canvas(master=self, width=128, height=128)
        canvas.grid(row=0, columnspan=2, padx=10, pady=10)

        image_path = "images/python_logo.png"
        self.logo = tk.PhotoImage(file=image_path)
        canvas.create_image(0, 0, anchor=tk.NW, image=self.logo)

        # Label containing heading indicating the current frame is a account registration page
        regis_title = tk.Label(master=self,
                               text="Welcome to CodeVenture!",
                               font=("Arial Bold", 30))
        # regis_title.grid()
        regis_title.grid(row=1,columnspan=2, padx=10, pady=10)

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

        # Label to ask user for their date of birth
        dob_label = tk.Label(master=self, text="Date of birth:")
        dob_label.grid(row=4, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to date of birth
        # self.dob_entry = tk.StringVar()
        self.dob_entry = DateEntry(self, selectmode="day", locale="en_UK")
        # self.dob_entry = DateEntry(master=self, width=12, borderwidth=2)
        # self.dob_entry = tk.Entry(master=self, textvariable=self.dob_entry)
        self.dob_entry.grid(row=4, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for their phone number
        ph_num_label = tk.Label(master=self, text="Phone number:")
        ph_num_label.grid(row=5, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to phone number
        self.ph_num_entry = tk.StringVar()
        self.ph_num_entry = tk.Entry(master=self, textvariable= self.ph_num_entry)
        self.ph_num_entry.grid(row=5, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for their email
        email_label = tk.Label(master=self, text="Email:")
        email_label.grid(row=6, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to email
        self.email_entry = tk.StringVar()
        self.email_entry = tk.Entry(master=self, textvariable=self.email_entry)
        self.email_entry.grid(row=6, column=1, sticky=tk.W, padx=10, pady=10)

        # Label to ask user for their grade
        grade_label = tk.Label(master=self, text="Grade:")
        grade_label.grid(row=7, column=0, sticky=tk.E, padx=10, pady=10)

        # Variable and entry to grade
        self.grade_entry = tk.StringVar()
        self.grade_entry = tk.Entry(master=self, textvariable=self.grade_entry)
        self.grade_entry.grid(row=7, column=1, sticky=tk.W, padx=10, pady=10)

        # Button to register
        register_button = tk.Button(master=self, text="Register")
        # login_button = tk.Button(master=self, text="Login",
        #                          command=self.authenticate_login)
        register_button.grid(row=8,column=0, columnspan=2, padx=10, pady=10)

        # Back to login page button
        # back_button = tk.Button(self, text="Back", command=lambda: login_frame.place())
        back_button = tk.Button(master=self, text="Back", command=self.return_menu)
        back_button.grid(row=0, column=0, sticky=tk.NW)

    def return_menu(self):
        """
        Returns to previous menu which is patient's main menu
        """
        self.place_forget() # forget a widget from the parent widget or screen
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Positions the frame and is anchored in the
                                                                       # \middle
        # DEBUGGING USE
        print("Currently in login frame")

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