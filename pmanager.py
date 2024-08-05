import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from cryptography.fernet import Fernet
from main import PasswordManager  # Import the backend

class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.configure(bg='#2f3138')
        self.pm = PasswordManager()
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('1500x800')

        self.create_widgets()

    def create_widgets(self):
        self.menu_frame = tk.Frame(self.root, bg='#23272a', width=300)
        self.menu_frame.pack(side='left', fill='y')

        self.title_label = tk.Label(self.menu_frame, text="🏠 Menu", fg='#dcddde', bg='#23272a', font=('Helvetica', 16, 'bold'), anchor='w')
        self.title_label.pack(padx=15, pady=(20, 15), anchor='w')

        # Create buttons and add them to the menu frame
        self.add_separator()
        self.create_key_button = self.create_button("🔑 Create New Key", self.create_key)
        self.load_key_button = self.create_button("📂 Load Existing Key", self.load_key)
        self.create_pass_file_button = self.create_button("📁 Create New Password File", self.create_pass_file)
        self.load_pass_file_button = self.create_button("📂 Load Existing Password File", self.load_pass_file)
        self.add_pass_button = self.create_button("➕ Add New Password", self.add_pass)
        self.get_pass_button = self.create_button("🔍 Get Password", self.get_pass)
        self.generate_password_button = self.create_button("☆NEW☆ Generate Password", self.generate_password)

    #Method that creates the buttons
    def create_button(self, text, command):
        button = tk.Button(self.menu_frame, text=text, command=command, fg='#5c5e66', font=('Helvetica', 12, 'bold'),
                           bg='#23272a', activebackground='#2f3136', bd=0, highlightthickness=0, anchor='w', justify='left')
        button.pack(padx=15, pady=5, fill='x')

        # Bind hover events
        button.bind("<Enter>", lambda e: self.on_enter(button))
        button.bind("<Leave>", lambda e: self.on_leave(button))

        return button
    
    def add_separator(self):
        separator = tk.Frame(self.menu_frame, bg='#5c5e66', height=2)
        separator.pack(fill='x', padx=13, pady=5)


    def on_enter(self, button):
        button.config(bg='#2f3136')  # Change background color on hover

    def on_leave(self, button):
        button.config(bg='#23272a')  # Revert background color when hover ends

    def create_key(self):
        path = simpledialog.askstring("Input", "Enter path to save the key:")
        if path:
            self.pm.create_key(path)
            messagebox.showinfo("Success", f"Key created and saved at {path}")

    def load_key(self):
        path = simpledialog.askstring("Input", "Enter path to load the key from:")
        if path:
            self.pm.load_key(path)
            messagebox.showinfo("Success", f"Key loaded from {path}")

    def create_pass_file(self):
        path = simpledialog.askstring("Input", "Enter path to create the password file:")
        if path:
            initial_values = {
                "email": "83",
                "youtube": "485as",
                "Tiktok": "uiqwu83"
            }
            self.pm.create_pass_file(path, initial_values)
            messagebox.showinfo("Success", f"Password file created at {path}")

    def load_pass_file(self):
        path = simpledialog.askstring("Input", "Enter path to load the password file from:")
        if path:
            self.pm.load_pass_file(path)
            messagebox.showinfo("Success", f"Password file loaded from {path}")

    def add_pass(self):
        site = simpledialog.askstring("Input", "Enter the site:")
        password = simpledialog.askstring("Input", "Enter your password:")
        if site and password:
            self.pm.add_pass(site, password)
            messagebox.showinfo("Success", f"Password for {site} added")

    def get_pass(self):
        site = simpledialog.askstring("Input", "Enter the site to get the password for:")
        if site:
            try:
                password = self.pm.get_pass(site)
                messagebox.showinfo("Password", f"Password for {site}: {password}")
            except KeyError:
                messagebox.showerror("Error", f"No password found for {site}")
#generator method not done yet
    def generate_password(self):
        digits = simpledialog.askstring("Input", "Enter how many digits would you like:")
        if digits >= str("8") :
            try:
                psswd=self.pm.generate_password(digits)
                messagebox.showinfo("Success!", f"Password has been generated: {psswd}")
                self.copy_button.config(state='normal')
            except KeyError:
                messagebox.showerror("Error", "Invalid Input")


        
        


    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password)
        messagebox.showinfo("Success", "Password copied to clipboard")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerGUI(root)
    root.mainloop()
