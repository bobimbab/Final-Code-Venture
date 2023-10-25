import tkinter as tk


class LoginFrame(tk.Frame):
    """
        The class definition for the LoginFrame class.
        """

    def __init__(self, master, width=960, height=540):
        """
        Constructor for the LoginFrame class.
        :param master: Tk object; the main window that the
                       login frame is to be contained.
        """
        super().__init__(master=master)
        self.master = master
        self.geometry(f"{width}x{height}")

        # # Logo image for the login page
        # login_canvas = tk.Canvas(master=self, width=128, height=128)
        # login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        # DO LATER
        # Image obtained from:
        # https://www.veryicon.com/icons/healthcate-medical/medical-icon-two-color-icon/ico-health-clinic.html
        # image_path = "images/week11_image.png"
        # self.login_logo = tk.PhotoImage(file=image_path)
        # login_canvas.create_image(0, 0,
        #                           anchor=tk.NW,
        #                           image=self.login_logo)

        # Label containing the welcome heading
        login_title = tk.Label(master=self,
                               text="Welcome to CodeVenture!",
                               font=("Arial Bold", 30))
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)



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