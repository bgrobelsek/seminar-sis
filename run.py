# run.py
# Ova datoteka je za pokretanje grafičkog sučelja koje sadrži 4 tipke - svaka poziva funkciju koja je 
# vezana .py datoteku da se izvrši odnosno da bude okidač za istu

# Importiranje modula za grafičko sučelje
import tkinter as tk
# Modul pomocu kojega čitamo i komuniciramo sa OS komponentama
import os
# Importiranje modula za subprocese
import subprocess
# Importiranje modula za poruke
from tkinter import messagebox


# Definiranje poziva funkcije run_CMSeek iz CMSeek foldera
# 'python3' - python komanda za izvršavanje skripte
# 'CMSeek/cmseek.py' - skripta ulazi u CMSeek folder i pokreće cmseek.py datoteku 
# 'url.txt' - govorimo skripti da uzme url.txt datoteku i koristi je kao listu
# '--folllow-redirect' - pošto se radi o url adresama, tražimo CMSeek da uvijek koristi sekundarnu http adresu
# '-v' - verbose
# '-' - batch
def run_CMSeek():
    subprocess.call(['python3', 'CMSeek/cmseek.py', '-l', 'url.txt', '--follow-redirect', '-v', '--batch'])

# Definiranje poziva funkcije koja poziva ********** i nakon poziva otvara folder sa .csv datotekama
def run_json_csv_sorting():
    subprocess.call(['python3', 'Projekt/json_csv_sorting.py'])
    show_output_folder("Projekt/cms_csv")

def run_ip_dns():
    subprocess.call(['python3', 'Projekt/ip_dns.py'])
    show_output_folder("Projekt/IP-DNS")

# Definiranje fukcije koja poziva encrypto
def run_call_encrypto(): 
    subprocess.call(['python3', 'Projekt/encrypto.py'])

# Definiranje funkcije koja kada se pozove otvara folder u kojem se nalaze obrađene datoteke
def show_output_folder(folder_name):
    output_folder = os.path.join(os.getcwd(), folder_name)
    result_label.config(text=f"Output folder: {output_folder}")

    # Open output folder based on operating system
    if os.name == "nt":  # Windows
        subprocess.Popen(['explorer', output_folder])
    elif os.name == "posix":  # Linux or macOS
        subprocess.Popen(['xdg-open', output_folder])

# Definiramo koji su nam folderi bitni za brisanje
directory_paths = ['Projekt/cms_csv', 'Projekt/IP-DNS']

# Brisanje svih datoteka unutar gorenavedenih foldera 
def delete_evidence():
    for directory_path in directory_paths:
            print(f"Deleting files in: {directory_path}")
            for filename in os.listdir(directory_path):
                file_path = os.path.join(directory_path, filename)
                if os.path.isfile(file_path):
                    subprocess.run(['rm', file_path])
                    print(f"Deleted file: {file_path}")
    messagebox.showinfo("Deletion Complete", "Nothing ever happened ;)")

# Ovo je TKinter sučelje
root = tk.Tk()
root.title("ScriptMe")

# Podešavanje veličine glavnog prozora
root.geometry("600x300")  

# Definiranje prve tipke
btn1 = tk.Button(root, text="Run CMSeek", fg='white', bg='green', command=run_CMSeek)
btn1.pack(pady=10)

# Definiranje druge tipke
btn2 = tk.Button(root, text="Run JSON > CSV", command=run_json_csv_sorting)
btn2.pack(pady=10)

# Definiranje treće tipke
btn3 = tk.Button(root, text="Run IP/DNS", command=run_ip_dns)
btn3.pack(pady=10)

# Definiranje četvrte tipke
btn4 = tk.Button(root, text="Call Encrypto", fg='white', bg='blue', command=run_call_encrypto)
btn4.pack(pady=10)

# Definiranje labele koja će nam pokazati koji je izlazni folder
result_label = tk.Label(root, text="Output folder: ")
result_label.pack(pady=15)

# Brisanje svih stavki unutar cms_csv i IP-DNS foldera
btn4 = tk.Button(root, text="DELETE EVIDENCE", fg='white', bg='red', command=delete_evidence)
btn4.pack(pady=10)

root.mainloop()
