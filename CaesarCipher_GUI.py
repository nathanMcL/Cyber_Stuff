# The purpose of this program:
# Implement a Caesar cipher GUI.
# Enter a message to encrypt,
# Enter a shift value
# Encrypt message option
# Decrypt message option


import tkinter as tk


# This function encrypts a message using the Caesar cipher.
def encrypt_caesar(plaintext, shift):
    """
    Encrypt a message using the Caesar cipher.

    Args:
        plaintext (str): The message to encrypt.
        shift (int): The shift value.

    Returns:
        str: The encrypted message.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            ciphertext += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            ciphertext += char
    return ciphertext


# This function decrypts a message using the Caesar cipher.
def decrypt_caesar(ciphertext, shift):
    """
    Decrypt a message using the Caesar cipher.

    Args:
        ciphertext (str): The message to decrypt.
        shift (int): The shift value.

    Returns:
        str: The decrypted message.
    """
    return encrypt_caesar(ciphertext, -shift)


# This function encrypts the message entered by the user.
def encrypt_message():
    """
    Encrypt the message entered by the user.
    """
    user_message = user_input.get()
    shift_value = int(shift_input.get())
    encrypted_result = encrypt_caesar(user_message, shift_value)
    encrypted_message.set(encrypted_result)
    print(f"Encrypted Message: {encrypted_result}")


# This function decrypts the message entered by the user.
def decrypt_message():
    """
    Decrypt the message entered by the user.
    """
    encrypted_message_text = encrypted_message.get()
    shift_value = int(shift_input.get())
    decrypted_result = decrypt_caesar(encrypted_message_text, shift_value)
    decrypted_message.set(decrypted_result)
    print(f"Decrypted Message: {decrypted_result}")


# Initialize the Tkinter window.
root = tk.Tk()
root.title("Caesar Cipher GUI")

# Create Tkinter variables.
user_input = tk.StringVar()
shift_input = tk.StringVar()
encrypted_message = tk.StringVar()
decrypted_message = tk.StringVar()

# Create Labels and Entry widgets.
tk.Label(root, text="Enter message:").pack()
tk.Entry(root, textvariable=user_input).pack()

tk.Label(root, text="Enter shift value:").pack()
tk.Entry(root, textvariable=shift_input).pack()

# Create Encrypt button.
tk.Button(root, text="Encrypt", command=encrypt_message).pack()

# Create a Label to show the encrypted message.
tk.Label(root, text="Encrypted message:").pack()
tk.Label(root, textvariable=encrypted_message).pack()

# Create Decrypt button.
tk.Button(root, text="Decrypt", command=decrypt_message).pack()

# Create a Label to show the decrypted message.
tk.Label(root, text="Decrypted message:").pack()
tk.Label(root, textvariable=decrypted_message).pack()

# Run the Tkinter event loop.
root.mainloop()
