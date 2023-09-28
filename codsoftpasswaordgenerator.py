import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 1:
        password_label.config(text="Password length must be at least 1")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=f"Generated Password: {password}")

root = tk.Tk()
root.title("Password Generator")

root.geometry("400x200")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 18), bg="#f0f0f0")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

length_label = tk.Label(frame, text="Password Length:", font=("Helvetica", 12), bg="#f0f0f0")
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

length_entry = tk.Entry(frame, font=("Helvetica", 12), width=5)
length_entry.grid(row=0, column=1, padx=5, pady=5)

generate_button = tk.Button(frame, text="Generate Password", font=("Helvetica", 12), command=generate_password)
generate_button.grid(row=0, column=2, padx=5, pady=5)

password_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0")
password_label.pack(pady=10)


root.mainloop()
