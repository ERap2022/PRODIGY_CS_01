import tkinter as tk
from tkinter import ttk, messagebox, filedialog


def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


def process_cipher():
    text = entry_text.get()
    shift = shift_value.get()

    if not text:
        messagebox.showwarning("Input Error", "Please enter text to process.")
        return

    if not shift.isdigit():
        messagebox.showwarning("Input Error", "Please enter a valid shift value.")
        return

    shift = int(shift)

    if operation.get() == "Encrypt":
        result = encrypt(text, shift)
    else:
        result = decrypt(text, shift)

    result_var.set(result)


def save_to_file():
    text = result_var.get()
    if not text:
        messagebox.showwarning("Save Error", "No text available to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text)
        messagebox.showinfo("File Saved", "The text has been saved successfully.")


def load_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
        entry_text.delete(0, tk.END)
        entry_text.insert(0, text)
        messagebox.showinfo("File Loaded", "The text has been loaded successfully.")


# Setting up the main window
window = tk.Tk()
window.title("Caesar Cipher Tool")
window.geometry("400x350")
window.configure(bg="#2C3E50")

# Style configuration
style = ttk.Style()
style.configure("TLabel", background="#2C3E50", foreground="#ECF0F1", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TRadiobutton", background="#2C3E50", foreground="#ECF0F1", font=("Helvetica", 12))

# Input text
ttk.Label(window, text="Plain text:").grid(row=0, column=0, padx=10, pady=10, sticky="E")
entry_text = ttk.Entry(window, width=30)
entry_text.grid(row=0, column=1, padx=10, pady=10, sticky="W")

# Shift value
ttk.Label(window, text="Shift value:").grid(row=1, column=0, padx=10, pady=10, sticky="E")
shift_value = ttk.Entry(window, width=10)
shift_value.grid(row=1, column=1, padx=10, pady=10, sticky="W")

# Operation selection
operation = tk.StringVar(value="Encrypt")
ttk.Radiobutton(window, text="Encrypt", variable=operation, value="Encrypt").grid(row=2, column=0, padx=10, pady=10,
                                                                                  sticky="E")
ttk.Radiobutton(window, text="Decrypt", variable=operation, value="Decrypt").grid(row=2, column=1, padx=10, pady=10,
                                                                                  sticky="W")

# Process button (using tk.Button for custom color)
process_button = tk.Button(window, text="Process", command=process_cipher, font=("Helvetica", 12), bg="#2C3E50",
                           fg="#ECF0F1")
process_button.grid(row=3, column=0, columnspan=2, pady=20)

# Output result
ttk.Label(window, text="Cipher Text:").grid(row=4, column=0, padx=10, pady=10, sticky="E")
result_var = tk.StringVar()
result_label = ttk.Entry(window, textvariable=result_var, width=30, state='readonly')
result_label.grid(row=4, column=1, padx=10, pady=10, sticky="W")

# Save and Load buttons
save_button = tk.Button(window, text="Save to File", command=save_to_file, font=("Helvetica", 12), bg="#2C3E50",
                        fg="#ECF0F1")
save_button.grid(row=5, column=0, padx=10, pady=10)

load_button = tk.Button(window, text="Load from File", command=load_from_file, font=("Helvetica", 12), bg="#2C3E50",
                        fg="#ECF0F1")
load_button.grid(row=5, column=1, padx=10, pady=10)

# Run the main loop
window.mainloop()
