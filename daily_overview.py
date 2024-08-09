import tkinter as tk
from tkinter import messagebox
import mysql.connector
from db import create_connection
from barcode_scanner import BarcodeScannerFrame
from choose_disease import ChooseDiseaseFrame

class DailyOverviewFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self)
        frame.pack(expand=True)

        welcome_label = tk.Label(frame, text="Welcome to Healthcare Management", font=("Arial", 14))
        welcome_label.pack(pady=10)

        nutrient_intake_button = tk.Button(frame, text="Nutrient Intake", width=25, font=("Arial", 12), command=self.show_nutrient_intake)
        nutrient_intake_button.pack(pady=5)

        reminders_button = tk.Button(frame, text="Reminders", width=25, font=("Arial", 12), command=self.show_reminders)
        reminders_button.pack(pady=5)

        add_activity_button = tk.Button(frame, text="Add a Daily Activity", width=25, font=("Arial", 12), command=self.add_daily_activity)
        add_activity_button.pack(pady=5)

        scan_barcode_button = tk.Button(frame, text="Scan a Barcode", width=25, font=("Arial", 12), command=self.open_barcode_scanner)
        scan_barcode_button.pack(pady=5)
        
        choose_disease_button = tk.Button(frame, text="Choose Your Disease", width=25, font=("Arial", 12), command=self.open_choose_disease)
        choose_disease_button.pack(pady=5)
        
        logout_button = tk.Button(frame, text="Log Out", width=25, font=("Arial", 12), command=self.logout)
        logout_button.pack(pady=5)

    def show_nutrient_intake(self):
        connection = create_connection()
        if connection is not None:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT NutrientIntake FROM DailyActivities WHERE UserID = %s ORDER BY Date DESC LIMIT 1", (self.master.user_id,))
                result = cursor.fetchone()
                if result:
                    messagebox.showinfo("Nutrient Intake", f"Nutrient Intake: {result[0]}")
                else:
                    messagebox.showinfo("Nutrient Intake", "No nutrient intake data found.")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
            finally:
                connection.close()
        else:
            messagebox.showerror("Connection Error", "Can't connect to the database")

    def show_reminders(self):
        connection = create_connection()
        if connection is not None:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT Reminder FROM Reminders WHERE UserID = %s ORDER BY Date DESC", (self.master.user_id,))
                results = cursor.fetchall()
                if results:
                    reminders = "\n".join([result[0] for result in results])
                    messagebox.showinfo("Reminders", f"Reminders:\n{reminders}")
                else:
                    messagebox.showinfo("Reminders", "No reminders found.")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
            finally:
                connection.close()
        else:
            messagebox.showerror("Connection Error", "Can't connect to the database")

    def add_daily_activity(self):
        def submit_activity():
            activity = activity_entry.get()
            connection = create_connection()
            if connection is not None:
                try:
                    cursor = connection.cursor()
                    cursor.execute("INSERT INTO DailyActivities (UserID, Date, NutrientIntake) VALUES (%s, CURDATE(), %s)", (self.master.user_id, activity))
                    connection.commit()
                    messagebox.showinfo("Success", "Daily activity added successfully!")
                    add_activity_window.destroy()
                except mysql.connector.Error as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")
                finally:
                    connection.close()
            else:
                messagebox.showerror("Connection Error", "Can't connect to the database")

        add_activity_window = tk.Toplevel(self)
        add_activity_window.title("Add Daily Activity")
        
        tk.Label(add_activity_window, text="Enter Nutrient Intake:", font=("Arial", 12)).pack(pady=5)
        activity_entry = tk.Entry(add_activity_window, width=50)
        activity_entry.pack(pady=5)
        
        submit_button = tk.Button(add_activity_window, text="Submit", font=("Arial", 12), command=submit_activity)
        submit_button.pack(pady=10)

    def open_barcode_scanner(self):
        self.master.switch_frame(BarcodeScannerFrame)

    def open_choose_disease(self):
        self.master.switch_frame(ChooseDiseaseFrame)
    
    def logout(self):
        from login_page import LoginFrame
        self.master.switch_frame(LoginFrame)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Healthcare Management Application")
    root.geometry("375x667")  # Set window size to mimic a mobile screen
    root.resizable(False, False)  # Disable window resizing
    app = DailyOverviewFrame(master=root)
    app.mainloop()
