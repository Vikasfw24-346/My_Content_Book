from tkinter import *
from tkinter.ttk import *
from sqlite3 import *
from tkinter import messagebox
import home

class LoginWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Login")
        self.geometry("300x200")
        self.resizable(FALSE, FALSE)

        s = Style()
        
        s.configure('Header.TFrame', background = 'blue')

        header_frame = Frame(self, style = 'Header.TFrame')
        header_frame.pack(fill = X)

        s.configure('Header.TLabel', background = 'blue', foreground = 'white', font = ('Arial', 20))

        header_label = Label(header_frame, text = "My Contact Book", style = 'Header.TLabel')
        header_label.pack(pady = 10)

        s.configure('Content.TFrame', background = 'white')

        content_frame = Frame(self, style = 'Content.TFrame')
        content_frame.pack(fill = BOTH, expand = TRUE)

        login_frame = Frame(content_frame, style = 'Content.TFrame')
        login_frame.place(relx = .5, rely = .5, anchor = CENTER)

        s.configure('Login.TLabel', background = 'white')

        username_label = Label(login_frame, text = "Username: ", style = 'Login.TLabel')
        username_label.grid(row = 0, column = 0)

        self.username_entry = Entry(login_frame, width = 20)
        self.username_entry.grid(row = 0, column = 1, pady = 5)

        password_label = Label(login_frame, text = "Password: ", style = 'Login.TLabel')
        password_label.grid(row = 1, column = 0)

        self.password_entry = Entry(login_frame, width = 20, show = '*')
        self.password_entry.grid(row = 1, column = 1, pady = 5)

        s.configure('Login.TButton', width = 20)

        login_button = Button(login_frame, text = 'Login', style = 'Login.TButton', command = self.login_button_click)
        login_button.grid(row = 2, column = 1, pady = 5)
        login_button.bind('<Return>', self.login_button_click)

    def login_button_click(self, event = None):
        con = connect('mycontacts.db')
        cur = con.cursor()
        cur.execute("select * from Login where Username = ? and Password = ?",
        (self.username_entry.get(), self.password_entry.get()))
        if cur.fetchone() is not None:
            self.destroy()
            home.HomeWindow()
        else:
            messagebox.showerror('Error Message', 'Incorrect username or password')

if __name__ == '__main__':
    lw = LoginWindow()
    lw.mainloop()
