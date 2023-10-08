# This Password Generator GUI:
# Uses random ascii, and numerical characters
# Chose length of password to generate.
# Can add more words to the list.


import random
import string
import tkinter as tk
from tkinter import ttk


def insert_word(password, word):
    index = random.randint(0, len(password))
    return password[:index] + word + password[index:]


def generate_password():
    try:
        length = int(entry_length.get())
    except ValueError:
        result_label.config(text="Invalid input for length!")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))

    add_words = ["RaBBit", "crAp", "eGGs", "SaucEd"]
    for word in add_words:
        if random.choice([True, False]):
            password = insert_word(password, word)

    result_label.config(text=f"Generated Password: {password}")


# Initialize Tkinter window
root = tk.Tk()
root.title("Password Generator")

# Add a label for password length
label_length = ttk.Label(root, text="Enter password length:")
label_length.grid(row=0, column=0, padx=10, pady=10)

# Add an entry box for password length
entry_length = ttk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

# Add a button to trigger password generation
button_generate = ttk.Button(root, text="Generate Password", command=generate_password)
button_generate.grid(row=1, columnspan=2, pady=10)

# Add a label to display the generated password
result_label = ttk.Label(root, text="")
result_label.grid(row=2, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
