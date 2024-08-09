import tkinter as tk
from tkinter import messagebox
import mysql.connector
from db import create_connection
class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        # Create a frame for centering the widgets
        frame = tk.Frame(self)
        frame.pack(expand=True)

        tk.Label(frame, text="Healthcare Management Application", font=("Arial", 16, "bold")).pack(pady=20)

        tk.Label(frame, text="User Name", font=("Arial", 12)).pack(pady=5)
        self.entry_username = tk.Entry(frame, width=30)
        self.entry_username.pack(pady=5)

        tk.Label(frame, text="Password", font=("Arial", 12)).pack(pady=5)
        self.entry_password = tk.Entry(frame, show='*', width=30)
        self.entry_password.pack(pady=5)

        login_button = tk.Button(frame, text="Log In", font=("Arial", 12), command=self.login)
        login_button.pack(pady=15)

        sign_up_frame = tk.Frame(frame)
        sign_up_frame.pack(pady=10)

        tk.Label(sign_up_frame, text="Don't have an account?", font=("Arial", 10)).pack(side="left")
        sign_up_button = tk.Button(sign_up_frame, text="Sign Up", font=("Arial", 10), command=self.open_sign_up)
        sign_up_button.pack(side="left")

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        connection = create_connection()

        if connection is not None:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT UserID FROM Users WHERE UserName = %s AND Password = %s", (username, password))
                account = cursor.fetchone()
                if account:
                    self.master.user_id = account[0]  # Set the user_id attribute in the master
                    messagebox.showinfo("Login Success", "You have successfully logged in!")
                    from daily_overview import DailyOverviewFrame
                    self.master.switch_frame(DailyOverviewFrame)
                else:
                    messagebox.showerror("Login Failed", "Invalid username or password")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
            finally:
                connection.close()  # Ensure connection is closed after operation
        else:
            messagebox.showerror("Connection Error", "Can't connect to the database")

    def open_sign_up(self):
        from signup_page import SignUpFrame
        self.master.switch_frame(SignUpFrame)

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Healthcare Management Application")
        self.geometry("375x667")  # Set window size to mimic a mobile screen
        self.resizable(False, False)  # Disable window resizing
        self._frame = None
        self.user_id = None  # Initialize user_id as None
        self.switch_frame(LoginFrame)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()