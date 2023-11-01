"""
FIT1056 Problem Solving Tasks for Week 11
"""

# Third party imports
import tkinter as tk

# Local application imports
from login_frame import LoginFrame

# CREATED FOR TESTING PURPOSES
class Interface(tk.Tk):
    """
    Class definition for the Interface class
    """
    def __init__(self, title, width=1000, height=700):
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


# root = Interface("CodeVenture")
# login = LoginFrame(root)
# login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# root.mainloop()

# TESTING USE
if __name__ == "__main__":
    # DO NOT MODIFY THIS
    x = Interface("CodeVenture Application")
    login = LoginFrame(x)
    login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    x.mainloop()
    print("--- End of program execution ---")
