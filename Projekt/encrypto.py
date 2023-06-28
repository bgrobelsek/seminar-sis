# encyrpto.py je jednostavna mala python aplikacija koja ima osnovno GUI sučelje i koja koristi
# fernet enkripcijski ključ za enkripciju i dekripciju isključivo CSV datoteka unutar foldera

################################################################################################

# Modul za rad s putanjama i direktorijima
import os 
# Modul za generaciju enkripcijskog ključa
from cryptography.fernet import Fernet 
# Modul za GUI
import tkinter as tk
# Dodatni moduli iz GUI modula
from tkinter import filedialog, messagebox
# Modul PIL
from PIL import ImageTk, Image

# Definira se root folder kroz kojeg će proći petlja koja nalazi .csv datoteke i 
# stavlja ih u csv_files 
def find_json_files(main_folder):
    csv_files = []
    for root, dirs, files in os.walk(main_folder):
        for file_name in files:
            if file_name.endswith('.csv'):
                csv_files.append(os.path.join(root, file_name))
    return csv_files

# Generiranje ključa za enkriptiranje i dekriptiranje
key = Fernet.generate_key()

# Funkcija za enkripciju jedne json datoteke koristeći Fernet ključ
def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Funkcija za dekripciju jedne json datoteke koristeći Fernet ključ
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)         
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# funkcija koja bilježi odabir foldera iz TKinter sučelja
def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(tk.END, folder_path)


# Funkcija koja pokreće enkripciju svake json datoteke unutar odabranog foldera
def encrypt_files():
    main_folder = folder_entry.get()
    if not main_folder:
        messagebox.showwarning("Folder Not Selected", "Please select a folder.")
        return

    # Pozivanje funkcije find_jason_files koju smo gore definirali 
    csv_files = find_json_files(main_folder)

    # ako funkcija ne nađe niti jednu .csv datoteku obavjestiti će korisnika porukom
    if not csv_files:
        messagebox.showinfo("No .CSV Files", "No .CSV files found in the selected folder.")
        return

    # for petlja koja proalzi kroz json datoteke    
    for file_path in csv_files:
        encrypt_file(file_path, key)

    # poruka koja iskače ako je enkripcija izvršena 
    messagebox.showinfo("Encryption Complete", ".CSV files encrypted successfully.")

# Funkcija koja pokreće dekripciju svake json datoteke unutar odabranog foldera
def decrypt_files():
    main_folder = folder_entry.get()
    if not main_folder:
        messagebox.showwarning("Folder Not Selected", "Please select a folder.")
        return
    
    # Pozivanje funkcije find_jason_files koju smo gore definirali 
    csv_files = find_json_files(main_folder)

    # ako funkcija ne nađe niti jednu .csv datoteku obavjestiti će korisnika porukom
    if not csv_files:
        messagebox.showinfo("No .CSV Files", "No .CSV files found in the selected folder.")
        return
    
    # for petlja koja proalzi kroz json datoteke  
    for file_path in csv_files:
        decrypt_file(file_path, key)

    # poruka koja iskače ako je dekripcija izvršena
    messagebox.showinfo("Decryption Complete", ".CSV files decrypted successfully.")


# Kreacija glavnog prozora 
window = tk.Tk()
window.title("CSV File Encryption")
window.geometry("400x400")

# Slika čarobnjaka zajedno sa relativnim path-om, u slučaju da se ne nađe slika izlazi error "Image not found."
image_path = "Projekt/wiz.png"  
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
