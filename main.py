from cryptography.fernet import Fernet
import secrets
import string


class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_pass_file(self, path, initial_values=None):      
        self.password_file = path

        if initial_values is not None:
            for key,value in initial_values.items():
                self.add_pass(key, value)

    
    def load_pass_file(self, path):
        self.password_file = path
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
    
    def add_pass(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ':' + encrypted.decode() + '\n')

    def get_pass(self, site):
        return self.password_dict[site]
    

    #using string for all the symbols in a password
    def generate_random_password(self,length):
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Password length must be a positive integer")
    
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    
def main():
    password = {"email" : "123",
                "youtube" : "465as",
                "Tiktok" : " uiqwu123"}
    
    pm = PasswordManager()
    print(""" Menu
(1) Create new key
(2) Load existing key
(3) Create new password file
(4) Load existing password file
(5) Add a new password
(6) Get a password
(q) Quit
""")

    while True:
        choise = input("Enter an option: ")

        if choise == "1":
            path= input("Enter path: ")
            pm.create_key(path)

        elif choise == "2":
            path= input("Enter path: ")
            pm.load_key(path)
        
        elif choise == "3":
            path= input("Enter path: ")
            pm.create_pass_file(path, password)

        elif choise == "4":
            path= input("Enter path: ")
            pm.load_pass_file(path)  

        elif choise == "5":
            site = input("Enter the site: ")
            password = input("Enter your password: ")
            pm.add_pass(site, password)
        
        elif choise == "6":
            site = input("Which site: ")
            print(f"Password for {site} is {pm.get_pass(site)}")

        elif choise == "q":
            print("Bye :) ")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

