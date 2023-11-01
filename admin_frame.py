import os
import shutil
import tkinter as tk
from tkinter import simpledialog
from detail_frame import detailframe
from user import User, YoungLearner, Admin


class AdminFrame(tk.Frame):

    def __init__(self, master, login_frame, shutdown_frame, user_obj):
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame
        self.shutdown_frame = shutdown_frame
        self.user_obj = user_obj

        for row_count in range(5):
            self.master.rowconfigure(row_count, weight=1, uniform="row")

        self.master.columnconfigure(0, weight=1, uniform="col")

        add = tk.Button(self, text="Add Module", command=self.add_module)
        add.grid(row=0, column=0, padx=10, pady=10)

        delete = tk.Button(self, text="Del Module", command=self.delete_module)
        delete.grid(row=1, column=0, padx=10, pady=10)

        view_profile_user = tk.Button(self, text="View Profile for user",
                                      command=lambda: self.get_det_user(self.user_obj))
        view_profile_user.grid(row=2, column=0, padx=10, pady=10)

        view_profile_admins = tk.Button(self, text="View Profile for admin",
                                        command=lambda: self.get_det_admin(self.user_obj))
        view_profile_admins.grid(row=3, column=0, padx=10, pady=10)

        logout = tk.Button(self, text="Logout", command=self.logout)
        logout.grid(row=4, column=0, padx=10, pady=10)

        shutdown = tk.Button(self, text="Shutdown", command=self.shut_down)
        shutdown.grid(row=5, column=0, padx=10, pady=10)

    def add_module(self):
        module_path = os.path.join("data", "modules.txt")
        module_name = self.get_module_name_input()
        image_names = self.get_image_names_input()

        if module_name and image_names:  # Check if input is not empty
            with open(module_path, "a") as file:
                file.write(f"\n{module_name}: {image_names}\n")
            tk.messagebox.showinfo("Success", "Module added successfully!")
        else:
            tk.messagebox.showerror("Error", "Module name or image names cannot be empty!")

    def delete_module(self):
        module_path = os.path.join("data", "modules.txt")
        with open(module_path, "r") as file:
            module_lines = file.readlines()

        selected_module = self.get_selected_module_input()
        module_found = False

        with open(module_path, "w") as file:
            for line in module_lines:
                if not line.startswith(selected_module):
                    file.write(line)
                else:
                    module_found = True

        if module_found:
            module_content_directory = os.path.join("data", "module_content", selected_module)
            if os.path.exists(module_content_directory):
                shutil.rmtree(module_content_directory)
                tk.messagebox.showinfo("Success", f"Module '{selected_module}' and its images deleted successfully!")
            else:
                tk.messagebox.showinfo("Success", f"Module '{selected_module}' deleted successfully!")
        else:
            tk.messagebox.showerror("Error", f"Module '{selected_module}' does not exist.")

    def get_module_name_input(self):
        module_name = simpledialog.askstring("Enter the module name", "Module Name")
        return module_name

    def get_image_names_input(self):
        image_names = simpledialog.askstring("Enter the image names", "Image Names (comma-separated)")
        return image_names

    def get_selected_module_input(self):
        selected_module = simpledialog.askstring("Enter the module name to delete", "Module Name")
        return selected_module

    def get_det_user(self, user):

        username = simpledialog.askstring("Enter the username", "Username of the user:")

        if username:
            # Look up the user with the entered username

            user = self.lookup_user_by_username(username)

            if user:
                # user=
                self.place_forget()
                dets_frame = detailframe(self.master, self, user)
                dets_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
                self.show_user_details(user)
            else:
                tk.messagebox.showerror("Error", "User with the entered username does not exist.")
        else:
            tk.messagebox.showerror("Error", "Username cannot be empty.")

        # self.place_forget()
        # dets_frame = detailframe(self.master, self, user)
        # dets_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # return f"User: {self.first_name} {self.last_name}\n" \
        # f"Username: {self.username}\n" \
        # f"Date of Birth: {self.dob}\n" \
        # f"Email: {self.email}\n" \
        # f"Phone Number: {self.ph_num}\n" \
        # f"Grade: {self.grade}\n"

    def lookup_user_by_username(self, username):
        user_data_file = os.path.join("data", "user_data.txt")
        user = None
        # Read user data from the file
        with open(user_data_file, "r", encoding="utf8") as file:
            files = file.readlines()
            for line in files:
                user_info = line.strip().split(",")
                if len(user_info) == 9:
                    first_name, last_name, user_name, password, dob, email, ph_num, user_type, grade = user_info
                    if user_name == username:
                        if user_type == "YL":
                            user = YoungLearner(
                                first_name=first_name,
                                last_name=last_name,
                                username=username,
                                password=password,
                                dob=dob,
                                email=email,
                                ph_num=ph_num,
                                grade=grade
                            )
                        elif user_type == "AD":
                            user = Admin(
                                first_name=first_name,
                                last_name=last_name,
                                username=username,
                                password=password,
                                dob=dob,
                                email=email,
                                ph_num=ph_num
                            )
                        break
        return user

    def show_user_details(self, user):
        # Display the user details using a detailframe or any other method
        self.place_forget()
        dets_frame = detailframe(self.master, self, user)
        dets_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def get_det_admin(self, user):
        self.place_forget()
        dets_frame = detailframe(self.master, self, user)
        dets_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def logout(self):
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def shut_down(self):
        # Display "Shutting Down" message
        for widget in self.winfo_children():
            widget.destroy()
        shutdown_label = tk.Label(self, text="Shutting Down...", font=("Helvetica", 18))
        shutdown_label.grid(row=0, column=0, padx=10, pady=10)

        # Schedule the actual shutdown after 3 seconds
        self.after(3000, self.shutdown_application)

    def shutdown_application(self):
        # Perform any shutdown actions here
        self.master.destroy()


if __name__ == "__main__":
    from user import Admin
    from datetime import date

    sample_user = Admin(
        first_name="John",
        last_name="Doe",
        username="johndoe",
        password="password123",
        dob=date(2005, 5, 15),
        email="johndoe@example.com",
        ph_num="123-456-7890",

    )

    # Create the main application window
    root = tk.Tk()

    # Create a YoungLearnerFrame with the sample user
    young_learner_frame = AdminFrame(root, None, None, sample_user)

    # Place the YoungLearnerFrame in the window
    young_learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Start the application's main loop
    root.mainloop()
