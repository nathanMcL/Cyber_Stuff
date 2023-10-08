# The purpose of this program:
# Allow user to enter a password.
# The password is "Salted" before hashing.
# The Password is hashed using the SHA-256 algorithm.
# A prompt to Iteratively Hash the password.
# Displays the salted and hashed value in the read-only text field


#Salting: It's common practice to add a unique "salt" to each password.
# This ensures that even if two users have the same password,
# their hashes will be different.
# It also helps protect against rainbow table attacks.

# Iterative Hashing: Rather than hashing just once,
# you can hash the password multiple times (often thousands or more).
# This makes brute-force attacks and other methods of attack more time-consuming and less practical.

import tkinter as tk
from tkinter import ttk
import hashlib
import os


def generate_hash():
    password = password_entry.get()

    # Generate a unique salt
    salt = os.urandom(16)
    salted_password = salt + password.encode()

    # Hash the salted password
    hashed_password = hashlib.sha256(salted_password).hexdigest()

    # If iterative hashing is selected, rehash the result multiple times
    if iterative_var.get():
        for _ in range(10000):  # 10,000 iterations as an example
            hashed_password = hashlib.sha256(hashed_password.encode()).hexdigest()

    # Display salt and hash
    display_text = f"Salt: {salt.hex()}\nHash: {hashed_password}"

    hash_display.config(state=tk.NORMAL)  # Temporarily enable the Text widget
    hash_display.delete(1.0, tk.END)
    hash_display.insert(tk.END, display_text)
    hash_display.config(state=tk.DISABLED)  # Set text field back to read-only


root = tk.Tk()
root.title("Password Hash Generator with Salt and Iterative Hashing")

frame = ttk.LabelFrame(root, text="Password Input", padding=(10, 5))
frame.pack(padx=10, pady=10, fill=tk.X)

password_label = ttk.Label(frame, text="Enter Password:")
password_label.pack(padx=5, pady=5, anchor=tk.W)

password_entry = ttk.Entry(frame, show="*")
password_entry.pack(padx=5, pady=5, fill=tk.X)

# Checkbutton for iterative hashing
iterative_var = tk.BooleanVar()  # Holds the on/off state of the checkbutton
iterative_check = ttk.Checkbutton(frame, text="Use Iterative Hashing", variable=iterative_var)
iterative_check.pack(padx=5, pady=10)

generate_button = ttk.Button(frame, text="Generate Hash", command=generate_hash)
generate_button.pack(padx=5, pady=20)

hash_display = tk.Text(root, height=10, wrap=tk.WORD)  # Increased height for better display
hash_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
hash_display.config(state=tk.DISABLED)


def insert_text(text):
    hash_display.config(state=tk.NORMAL)
    hash_display.insert(tk.END, text)
    hash_display.config(state=tk.DISABLED)


insert_text("Your salt and password hash will be displayed here.")

root.mainloop()

