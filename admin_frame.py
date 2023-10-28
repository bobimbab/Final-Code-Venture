import tkinter as tk
from detail_frame import detailframe


class AdminFrame(tk.Frame):

    def __init__(self, master,login_frame,shutdown_frame, user_obj):
        super().__init__(master)
        self.master = master
        self.login_frame = login_frame
        self.shutdown_frame = shutdown_frame
        self.user_obj = user_obj

        for row_count in range(5):
            self.master.rowconfigure(row_count, weight=1, uniform="row")

        self.master.columnconfigure(0, weight=1, uniform="col")

        edit = tk.Button(self, text="Edit Module",command=self.edit)
        edit.grid(row=0, column=0, padx=10, pady=10)

        delete = tk.Button(self, text="Del Module", command=self.delete)
        delete.grid(row=1, column=0, padx=10, pady=10)

        view_profile_user = tk.Button(self, text="View Profile for user", command=self.get_det_user)
        view_profile_user.grid(row=2, column=0, padx=10, pady=10)

        view_profile_admins = tk.Button(self, text="View Profile for admin", command=self.get_det_admin)
        view_profile_admins.grid(row=3, column=0, padx=10, pady=10)

        logout = tk.Button(self, text="Logout", command=self.logout)
        logout.grid(row=4, column=0, padx=10, pady=10)

        shutdown = tk.Button(self, text="Shutdown", command=self.logout)
        shutdown.grid(row=5, column=0, padx=10, pady=10)


    @staticmethod

    def edit(self):
        pass

    def delete(self):
        pass

    def get_det_user(self):
        self.place_forget()
        dets_frame = detailframe(self.master, self)
        dets_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # return f"User: {self.first_name} {self.last_name}\n" \
        # f"Username: {self.username}\n" \
        # f"Date of Birth: {self.dob}\n" \
        # f"Email: {self.email}\n" \
        # f"Phone Number: {self.ph_num}\n" \
        # f"Grade: {self.grade}\n"

    def get_det_admin(self):
        self.place_forget()
        dets_frame = detailframe(self.master,self)
        dets_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def logout(self):
        self.place_forget()
        self.login_frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

    def shut_down(self):
        self.place_forget()
        self.shutdown_frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
