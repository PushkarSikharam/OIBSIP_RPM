import random
import string
import tkinter as Tk
from tkinter import ttk
import pyperclip
from PIL import Image, ImageTk

class Passwordgen:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x350")
        self.master.config(bg="#FFE4E1")  # Light Pink background

        # Load and resize background image
        bg_image = Image.open("password-security.jpg")
        bg_image = bg_image.resize((400, 350), Image.LANCZOS)  # Resize using LANCZOS resampling
        self.background_image = ImageTk.PhotoImage(bg_image)

        # Create background label
        self.background_label = Tk.Label(self.master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.style = ttk.Style()
        self.style.configure('TButton', font=('calibri', 10, 'bold'), foreground='white', background='#FF6347')  # Coral button color
        self.style.configure('TCheckbutton', background="#FFE4E1", foreground='#4B0082')  # Light Pink background, Indigo text color
        self.style.map('TCheckbutton', background=[('active', '#FFE4E1')])  # Light Pink background for active state

        self.length_label = ttk.Label(self.master, text='Password Length:', background="#FFE4E1", foreground='#4B0082')  # Light Pink label background, Indigo text color
        self.length_label.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        self.length_var = Tk.IntVar()
        self.length_entry = ttk.Entry(self.master, textvariable=self.length_var, width=5)
        self.length_entry.grid(row=0, column=1, pady=10, padx=10)

        self.num_passwords_label = ttk.Label(self.master, text='Number of Passwords:', background="#FFE4E1", foreground='#4B0082')  # Light Pink label background, Indigo text color
        self.num_passwords_label.grid(row=1, column=0, pady=5, padx=10, sticky='w')

        self.num_passwords_var = Tk.IntVar(value=1)
        self.num_passwords_entry = ttk.Entry(self.master, textvariable=self.num_passwords_var, width=5)
        self.num_passwords_entry.grid(row=1, column=1, pady=5, padx=10)

        self.uppercase_var = Tk.IntVar()
        self.uppercase_check = ttk.Checkbutton(self.master, text='Include Uppercase', variable=self.uppercase_var, style='TCheckbutton')
        self.uppercase_check.grid(row=2, column=0, pady=5, padx=10, sticky='w')

        self.lowercase_var = Tk.IntVar()
        self.lowercase_check = ttk.Checkbutton(self.master, text='Include Lowercase', variable=self.lowercase_var, style='TCheckbutton')
        self.lowercase_check.grid(row=3, column=0, pady=5, padx=10, sticky='w')

        self.digits_var = Tk.IntVar()
        self.digits_check = ttk.Checkbutton(self.master, text='Include Digits', variable=self.digits_var, style='TCheckbutton')
        self.digits_check.grid(row=4, column=0, pady=5, padx=10, sticky='w')

        self.specialchar_var = Tk.IntVar()
        self.specialchar_check = ttk.Checkbutton(self.master, text='Include Special Character', variable=self.specialchar_var, style='TCheckbutton')
        self.specialchar_check.grid(row=5, column=0, pady=5, padx=10, sticky='w')

        self.generate_button = ttk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky='ew')

        self.copy_button = ttk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=7, column=0, columnspan=2, pady=5, padx=10, sticky='ew')

        self.result_var = Tk.StringVar()
        self.result_label = ttk.Label(self.master, textvariable=self.result_var, wraplength=350, justify='center', background="#FFE4E1", foreground='#4B0082')  # Light Pink background, Indigo text color
        self.result_label.grid(row=8, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        num_passwords = self.num_passwords_var.get()
        uppercase = string.ascii_uppercase if self.uppercase_var.get() else ""
        lowercase = string.ascii_lowercase if self.lowercase_var.get() else ""
        digits = string.digits if self.digits_var.get() else ""    
        special = string.punctuation if self.specialchar_var.get() else ""

        all_characters = uppercase + lowercase + digits + special

        if not all_characters:
            self.result_var.set("Please select at least one character")
            return

        passwords = []
        for _ in range(num_passwords):
            password = ''.join(random.choice(all_characters) for _ in range(length))
            passwords.append(password)
        self.result_var.set("Generated Password(s):\n" + "\n".join(passwords))

    def copy_to_clipboard(self):
        generated_passwords = self.result_var.get()
        if generated_passwords:
            pyperclip.copy(generated_passwords)
            self.result_var.set("Password(s) copied to clipboard!")

if __name__ == "__main__":
    root = Tk.Tk()
    app = Passwordgen(root)
    # Center the window
    window_width = root.winfo_reqwidth()
    window_height = root.winfo_reqheight()
    position_right = int(root.winfo_screenwidth()/2 - window_width/2)
    position_down = int(root.winfo_screenheight()/2 - window_height/2)
    root.geometry("+{}+{}".format(position_right, position_down))
    root.mainloop()
