import tkinter as tk


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
        login_canvas = tk.Canvas(master=self, width=360, height=360)
        login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        # DO LATER
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

        # Variable and entry to password
        self.password = tk.StringVar()
        self.password_entry = tk.Entry(master=self, textvariable=self.password,
                                       show="●")
        self.password_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)


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