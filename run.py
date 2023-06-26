import tkinter as tk
import os
import subprocess

url_adresses = 'url.txt'

def run_CMSeek():
    subprocess.call(['python3', 'CMSeek/cmseek.py -l url.txt --follow-redirect -v --batch'])

def run_json_reading_v2():
    subprocess.call(['python3', 'Projekt/json_reading_v2.py'])
    show_output_folder("Projekt/cms_csv")

def run_ip_dns():
    subprocess.call(['python3', 'Projekt/ip_dns.py'])
    show_output_folder("Projekt/IP-DNS")

def run_call_encrypto(): 
    subprocess.call(['python3', 'Projekt/encrypto.py'])

def show_output_folder(folder_name):
    output_folder = os.path.join(os.getcwd(), folder_name)
    result_label.config(text=f"Output folder: {output_folder}")

    # Open output folder based on operating system
    if os.name == "nt":  # Windows
        subprocess.Popen(['explorer', output_folder])
    elif os.name == "posix":  # Linux or macOS
        subprocess.Popen(['xdg-open', output_folder])

root = tk.Tk()
root.title("ScriptMe")
root.geometry("350x300")  # Set window size

# First Button
btn1 = tk.Button(root, text="Run CMSeek", command=run_CMSeek)
btn1.pack(pady=10)

# Second Button
btn2 = tk.Button(root, text="Run json_reading_v2.py", command=run_json_reading_v2)
btn2.pack(pady=10)

# Third Button
btn3 = tk.Button(root, text="Run ip_dns.py", command=run_ip_dns)
btn3.pack(pady=10)

# Fourth button
btn4 = tk.Button(root, text="Call Encrypto", command=run_call_encrypto)
btn4.pack(pady=10)

# Output Folder Label
result_label = tk.Label(root, text="Output folder: ")
result_label.pack(pady=10)

root.mainloop()
