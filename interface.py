import tkinter as tk
from login_frame import LoginFrame


class Interface(tk.Tk):
    """
    Class definition for the Interface class
    """
    def __init__(self, title, width=1000, height=800):
        """
        Constructor for the Interface class,
        the main window for the HCMS.
        :param title: str
        :param width: int - default 960 pixels
        :param height: int - default 540 pixels
        """
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")

if __name__ == "__main__":
    # DO NOT MODIFY THIS
    x = Interface("CodeVenture Application")
    login = LoginFrame(x)
    login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    x.mainloop()
    print("--- End of program execution ---")
