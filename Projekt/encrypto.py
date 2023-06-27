import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image

def find_json_files(main_folder):
    json_files = []
    for root, dirs, files in os.walk(main_folder):
        for file_name in files:
            if file_name.endswith('.csv'):
                json_files.append(os.path.join(root, file_name))
    return json_files

# ovde se uzme ključ i otključa 
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)         
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(tk.END, folder_path)

# generacija ključa za enkriptiranje i dekriptiranje
key = Fernet.generate_key()

def encrypt_files():
    main_folder = folder_entry.get()
    if not main_folder:
        messagebox.showwarning("Folder Not Selected", "Please select a folder.")
        return

    json_files = find_json_files(main_folder)

    if not json_files:
        messagebox.showinfo("No .CSV Files", "No .CSV files found in the selected folder.")
        return

    for file_path in json_files:
        encrypt_file(file_path, key)

    messagebox.showinfo("Encryption Complete", ".CSV files encrypted successfully.")

def decrypt_files():
    main_folder = folder_entry.get()
    if not main_folder:
        messagebox.showwarning("Folder Not Selected", "Please select a folder.")
        return

    # key = Fernet.generate_key()
    json_files = find_json_files(main_folder)

    if not json_files:
        messagebox.showinfo("No .CSV Files", "No .CSV files found in the selected folder.")
        return

    for file_path in json_files:
        decrypt_file(file_path, key)

    messagebox.showinfo("Decryption Complete", ".CSV files decrypted successfully.")

# Create the main window
window = tk.Tk()
window.title("CSV File Encryption")
window.geometry("400x400")

image_path = "/home/bruno/Documents/GitHub/seminar-sis/Projekt/wiz.png"  
if os.path.exists(image_path):
    image = Image.open(image_path)
    image = image.resize((200, 200), Image.ANTIALIAS)
    wizard_img = ImageTk.PhotoImage(image)
    img_label = tk.Label(window, image=wizard_img)
    img_label.pack(pady=10)
else:
    print("Image file not found.")

# Folder selection label and entry
folder_label = tk.Label(window, text="Select Folder:")
folder_label.pack()
folder_entry = tk.Entry(window, width=40)
folder_entry.pack()

# Folder selection button
select_button = tk.Button(window, text="Browse", command=select_folder)
select_button.pack(pady=10)

# Encryption button
encrypt_button = tk.Button(window, text="Encrypt Files", command=encrypt_files)
encrypt_button.pack()

# Decryption button
decrypt_button = tk.Button(window, text="Decrypt Files", command=decrypt_files)
decrypt_button.pack()

# Start the GUI main loop
window.mainloop()
