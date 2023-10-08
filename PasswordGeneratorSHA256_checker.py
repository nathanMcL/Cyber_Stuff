# The purpose of this program:
# (the result from PasswordgeneratorSHA256.py).
# A salt (as a hexadecimal string).
# A hashed password
# A user-entered password.

# The program will then hash the user-entered password with the provided salt and
# compare the result to the hashed password.
# If they match, it indicates the user-entered password is the original password
# (assuming the same salt and hashing procedure was applied).
# If not, the entered password is incorrect.

import tkinter as tk
from tkinter import ttk
import hashlib


def verify_password():
    # Retrieve the salt, hashed password, and user-entered password
    entered_salt = salt_entry.get()
    entered_hash = hash_entry.get()
    entered_password = password_entry.get()

    # Convert the hexadecimal salt back to bytes
    salt_bytes = bytes.fromhex(entered_salt)

    # Hash the user-entered password with the provided salt
    salted_password = salt_bytes + entered_password.encode()
    hashed_password = hashlib.sha256(salted_password).hexdigest()

    # If iterative hashing is selected, rehash the result multiple times
    if iterative_var.get():
        for _ in range(10000):  # 10,000 iterations as an example
            hashed_password = hashlib.sha256(hashed_password.encode()).hexdigest()

        # Check if the hashed result matches the provided hash
        if hashed_password == entered_hash:
            verification_result = "Password is Correct!"
        else:
            verification_result = "Password is Incorrect!"

        # Update the result_display with the verification result and the entered password
        result_display.config(state=tk.NORMAL)
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, f"{verification_result}\nEntered Password: {entered_password}")
        result_display.config(state=tk.DISABLED)

    # Check if the hashed result matches the provided hash
    if hashed_password == entered_hash:
        result_display.config(state=tk.NORMAL)
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, "Password is Correct!")
        result_display.config(state=tk.DISABLED)
    else:
        result_display.config(state=tk.NORMAL)
        result_display.delete(1.0, tk.END)
        result_display.insert(tk.END, "Password is Incorrect!")
        result_display.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Password Verifier with Salt and Iterative Hashing")

frame = ttk.LabelFrame(root, text="Input Fields", padding=(10, 5))
frame.pack(padx=10, pady=10, fill=tk.X)

# Entry fields for salt, hash, and password
salt_label = ttk.Label(frame, text="Enter Salt (hexadecimal):")
salt_label.pack(padx=5, pady=5, anchor=tk.W)

salt_entry = ttk.Entry(frame)
salt_entry.pack(padx=5, pady=5, fill=tk.X)

hash_label = ttk.Label(frame, text="Enter Hashed Password:")
hash_label.pack(padx=5, pady=5, anchor=tk.W)

hash_entry = ttk.Entry(frame)
hash_entry.pack(padx=5, pady=5, fill=tk.X)

password_label = ttk.Label(frame, text="Enter Password to Verify:")
password_label.pack(padx=5, pady=5, anchor=tk.W)

password_entry = ttk.Entry(frame, show="*")
password_entry.pack(padx=5, pady=5, fill=tk.X)

# Checkbutton for iterative hashing
iterative_var = tk.BooleanVar()
iterative_check = ttk.Checkbutton(frame, text="Use Iterative Hashing", variable=iterative_var)
iterative_check.pack(padx=5, pady=10)

verify_button = ttk.Button(frame, text="Verify Password", command=verify_password)
verify_button.pack(padx=5, pady=20)

result_display = tk.Text(root, height=3, wrap=tk.WORD)
result_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
result_display.config(state=tk.DISABLED)

root.mainloop()
