import tkinter as tk
from user import User, YoungLearner, Admin
from authenticator import Authenticator
from register_frame import RegisterFrame
from younglearner_frame import YoungLearnerFrame

class LoginFrame(tk.Frame):
    """
        The class definition for the LoginFrame class.
        """

    def __init__(self, master):
        """
        Constructor for the LoginFrame class.
        :param master: Tk object; the main window that the
                       login frame is to be contained.
        """
        super().__init__(master=master)
        self.master = master
        # self.master.geometry(f"{width}x{height}")

        # Logo image for the login page
        login_canvas = tk.Canvas(master=self, width=128, height=128)
        login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        image_path = "images/python_logo.png"
        self.login_logo = tk.PhotoImage(file=image_path)
        login_canvas.create_image(0, 0,
                                  anchor=tk.NW,
                                  image=self.login_logo)

        # Label containing the welcome heading
        login_title = tk.Label(master=self,
                               text="Welcome to CodeVenture!",
                               font=("Arial Bold", 30))
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)

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

        # Button to login
        # login_button = tk.Button(master=self, text="Login")
        login_button = tk.Button(master=self, text="Login",
                                 command=self.authenticate_login)
        login_button.grid(row=3, column=1, padx=100)
        # login_button.grid(row=4, columnspan=2, padx=10, pady=10)

        # Variable and label to inform user of login outcome
        self.login_text = tk.StringVar()
        login_message = tk.Label(master=self, textvariable=self.login_text)
        login_message.grid(row=5, columnspan=2, padx=10, pady=10)

        # Button to reset password
        pw_reset_button = tk.Button(master=self, text="Forgot Password")
        pw_reset_button.grid(row=6, columnspan=2, padx=10, pady=10)

        # Button to register new account
        register_button = tk.Button(master=self, text="Register New Account", command=self.switch_to_register)
        register_button.grid(row=7, columnspan=2, padx=10, pady=10)

    def switch_to_register(self):
        self.place_forget()
        register_frame = RegisterFrame(self.master, login_frame=self)
        # register_frame = RegisterFrame(master=self)
        register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Display the register frame
        # DEBUGGING USE
        print("Currently in register frame")

    def authenticate_login(self):
        """
        Frontend function for the authentication procedure.
        This is invoked when the login button is clicked.
        :return: None
        """
        authenticator = Authenticator()
        auth_res = authenticator.authenticate(self.username.get(),
                                              self.password.get())

        if isinstance(auth_res, User):

            # Removes login successful text when logging out
            # self.login_text.set("")

            if auth_res.get_role() == "PA":  # patient login

                # Clears password and username input from index 0 to the end of index upon successful login
                # Not visible until user logs out
                self.password_entry.delete(0, 'end')
                self.username_entry.delete(0, 'end')

                # Remove login page from display
                self.place_forget()

                # Create and display the Patient login frame
                login_frame = YoungLearner(self.master, self, auth_res)
                login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            elif auth_res.get_role() in ["YL", "AD"]:
                self.login_text.set("Login successfully!")
                self.place_forget()
                yl_frame = YoungLearnerFrame(self.master, self)
                yl_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                # TESTING USAGE
                print("auth_res:", auth_res)
                # print("Role:", auth_res.get_role())
        else:
            self.login_text.set("Failed to login")
            # TESTING USAGE
            print("auth_res:", auth_res)
            # print("Role:", auth_res.get_role())


def main():
    # Create the main application window
    root = tk.Tk()
    root.title("Login Example")  # Set the window title

    # Create an instance of the LoginFrame class within the main window
    login_frame = LoginFrame(root)
    login_frame.grid(row=2, padx=10, pady=10)

    # Start the tkinter main loop to display the window
    root.mainloop()

if __name__ == "__main__":
    main()