import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from cryptography.fernet import Fernet
from main import PasswordManager  # Import the backend
#root main window
class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.configure(bg='#24292b')
        self.pm = PasswordManager()
        self.root.iconbitmap('favicon.ico')
        self.root.geometry('1200x800')

        self.create_widgets()
        
# anchor='w': Aligns the buttons to the left (west).
# padx=10: Adds horizontal padding to keep buttons away from the window edge.
# pady=5: Adds vertical padding between buttons.


    def create_widgets(self):
    # Create buttons with dark grey background and align them to the left
        self.create_key_button = tk.Button(self.root, text="Create New Key", command=self.create_key, bg='dark grey', fg='white')
        self.create_key_button.pack(anchor='w', padx=10, pady=(50, 5) )  # Align to the left (west)

        self.load_key_button = tk.Button(self.root, text="Load Existing Key", command=self.load_key, bg='dark grey', fg='white')
        self.load_key_button.pack(anchor='w', padx=10, pady=5)  # Align to the left (west)

        self.create_pass_file_button = tk.Button(self.root, text="Create New Password File", command=self.create_pass_file, bg='dark grey', fg='white')
        self.create_pass_file_button.pack(anchor='w', padx=10, pady=5)  # Align to the left (west)

        self.load_pass_file_button = tk.Button(self.root, text="Load Existing Password File", command=self.load_pass_file, bg='dark grey', fg='white')
        self.load_pass_file_button.pack(anchor='w', padx=10, pady=5)  # Align to the left (west)

        self.add_pass_button = tk.Button(self.root, text="Add New Password", command=self.add_pass, bg='dark grey', fg='white')
        self.add_pass_button.pack(anchor='w', padx=10, pady=5)  # Align to the left (west)

        self.get_pass_button = tk.Button(self.root, text="Get Password", command=self.get_pass, bg='dark grey', fg='white')
        self.get_pass_button.pack(anchor='w', padx=10, pady=5)  # Align to the left (west)


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
                "email": "123",
                "youtube": "465as",
                "Tiktok": "uiqwu123"
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

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerGUI(root)
    root.mainloop()
