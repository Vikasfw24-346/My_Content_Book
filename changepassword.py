from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from sqlite3 import *

class ChangePasswordFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.place(relx = .5, rely = .5, anchor = CENTER)

        s = Style()

        s.configure('TFrame', background = 'white')
        s.configure('TLabel', background = 'white')
        s.configure('TButton', width = 15)
        

        old_password_label = Label(self, text = "Old Password: ")
        old_password_label.grid(row = 0, column = 0, sticky = E)

        self.old_password_entry = Entry(self, width = 15, show = '*')
        self.old_password_entry.grid(row = 0, column = 1, pady = 5)

        new_password_label = Label(self, text = "New Password: ")
        new_password_label.grid(row = 1, column = 0, sticky = E)

        self.new_password_entry = Entry(self, width = 15)
        self.new_password_entry.grid(row = 1, column = 1, pady = 5)

        confirm_password_label = Label(self, text = "Confirm Password: ")
        confirm_password_label.grid(row = 2, column = 0, sticky = E)

        self.confirm_password_entry = Entry(self, width = 15, show = '*')
        self.confirm_password_entry.grid(row = 2, column = 1, pady = 5)

        change_button = Button(self, text = "Change", command = self.change_button_click)
        change_button.grid(row = 3, column = 1, pady = 5)

    def change_button_click(self):
        con = connect('mycontacts.db')
        cur = con.cursor()
        cur.execute("select * from Login where Password = ?", (self.old_password_entry.get(),))
        if cur.fetchone() is not None:
            if self.new_password_entry.get() == self.confirm_password_entry.get():
                cur.execute("update Login set Password = ? where Password = ?", (
                self.new_password_entry.get(), self.old_password_entry.get()))
                con.commit()
                messagebox.showinfo('Success Message', 'Password is changed successfully')
            else:
                messagebox.showerror('Error Message', 'New and confirm passwords mismatched')
        else:
            messagebox.showerror('Error Message', 'Incorrect old password')