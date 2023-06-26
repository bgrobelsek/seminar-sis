import csv
import os
import socket
import dns.resolver

# Dohvača putanju do root foldera 
root_folder_path = os.getcwd()

# Specificira ime input foldera
input_folder_name = 'Projekt/cms_csv'

# Stvara putanju do input foldera
input_folder_path = os.path.join(root_folder_path, input_folder_name)

# Specificira ime output foldera
output_folder_name = 'Projekt/IP-DNS'

# Stvara putanju do output foldera
output_folder_path = os.path.join(root_folder_path, output_folder_name)

# Dohvaća listu svih csv datoteka u input folderu
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Dohvaća listu svih csv datoteka u input folderu
csv_files = [file for file in os.listdir(input_folder_path) if file.endswith('.csv')]

# Petlja prolazi kroz svaku CSV datoteku
for file in csv_files:
    # Konstruira putanju za input datoteku
    input_file_path = os.path.join(input_folder_path, file)

    # Izvlači ime datoteke bez ekstenzija
    file_name = os.path.splitext(file)[0]

    # Konstruira output datoteku sa sufiksom "IPdns"
    output_file_name = file_name + "_IP-dns.csv"

    # Konstruira putanju za output datoteku
    output_file_path = os.path.join(output_folder_path, output_file_name)

    # Otvara input CSV datoteku
    with open(input_file_path, 'r') as csv_file:
        # Kreira CSV reader
        reader = csv.DictReader(csv_file)

        # Kreira listu za spremanje ekstrahiranih podataka
        data = []

        # Petlja koja prolazi svakim redom CSV datoteke
        for row in reader:
            # Provjerava da li 'url' ključ postoji
            if 'url' in row:
                # Izvlači URL iz 'url' stupca
                url = row['url']

                # Uklanja 'https://' prefix sa URL-a
                if url.startswith('https://'):
                    url = url[8:]

                # Pronalazi IP adresu za dobiveni URL
                try:
                    ip_address = socket.gethostbyname(url)
                except socket.gaierror:
                    ip_address = "Not Found"

                # Pronalazi NS zapise adresu za dobiveni URL
                try:
                    ns_records = dns.resolver.resolve(url, 'NS')
                    ns_records = [ns.target.to_text() for ns in ns_records]
                except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.DNSException):
                    ns_records = "Not Found"

                # Append the data to the list
                data.append({'URL': url, 'IP Address': ip_address, 'NS Records': ns_records})

    # Kreira izlaznu CSV datoteku
    with open(output_file_path, 'w', newline='') as output_file:
        # Definira imena poljua za CSV zapis
        fieldnames = ['URL', 'IP Address', 'NS Records']

        # Kreira CSV zapis
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        # Zapis headera
        writer.writeheader()

        # Zapis podatka u izlaznu CSV datoteku
        writer.writerows(data)