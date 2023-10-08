# The purpose of this program:
#
# a brute force attack involves systematically checking all possible values
# for a solution until the correct one is found.
# Think of it as trying every possible combination to unlock a padlock.
#
# This program is a test to decrypt caesar cipher texts without knowing the shift value
#
# Running the program, the decryption is not 100% if you input an encrypted phrase.
# Portions of the message are still encrypted.


import tkinter as tk
from tkinter import ttk


# Caesar Cipher decryption
def decrypt_caesar(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():  # Only modify alphabetic characters
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():  # Handle uppercase separately
                if shifted < ord('A'):
                    shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char  # Keep spaces, punctuation, etc. unchanged
    return decrypted


# Brute Force Caesar Cipher
# The strip() method will remove any unwanted whitespace characters
# (like the newline character) from the start and end of the string.
def brute_force_caesar():
    ciphertext = txt_ciphertext.get(1.0, tk.END).strip()  # Remove trailing/leading whitespaces
    result.delete(1.0, tk.END)
    for shift in range(1, 26):
        plaintext = decrypt_caesar(ciphertext, shift)
        result.insert(tk.END, f"Shift {shift}: {plaintext}\n")


# GUI setup
root = tk.Tk()
root.title("Caesar Cipher Brute Force Decryptor")

frame = ttk.LabelFrame(root, text="Input Caesar Cipher Text", padding=(10, 5))
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

txt_ciphertext = tk.Text(frame, height=5)
txt_ciphertext.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

btn_decrypt = ttk.Button(frame, text="Brute Force Decrypt", command=brute_force_caesar)
btn_decrypt.pack(pady=5)

result_frame = ttk.LabelFrame(root, text="Decryption Results", padding=(10, 5))
result_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

result = tk.Text(result_frame, height=15)
result.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

root.mainloop()