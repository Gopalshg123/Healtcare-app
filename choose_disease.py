import tkinter as tk
from tkinter import messagebox

class ChooseDiseaseFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Choose Your Disease", font=("Arial", 14)).pack(pady=10)

        self.disease_var = tk.StringVar(value="Select Disease")

        disease_menu = tk.OptionMenu(self, self.disease_var, "Diabetes", "Jaundice", "Hypertension")
        disease_menu.config(width=20)
        disease_menu.pack(pady=10)

        select_button = tk.Button(self, text="Select Disease", command=self.select_disease)
        select_button.pack(pady=10)

        back_button = tk.Button(self, text="Back to Daily Overview", command=self.go_back)
        back_button.pack(pady=10)

    def select_disease(self):
        selected_disease = self.disease_var.get()
        if selected_disease == "Select Disease":
            messagebox.showwarning("Selection Error", "Please select a disease.")
        else:
            messagebox.showinfo("Disease Selected", f"You have selected {selected_disease}.")

    def go_back(self):
        from daily_overview import DailyOverviewFrame
        self.master.switch_frame(DailyOverviewFrame)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChooseDiseaseFrame(master=root)
    app.mainloop()
