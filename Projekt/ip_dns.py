# Ovaj Python kod ima svrhu demonstracije određenih funkcionalnosti pomoću CSV datoteka, radom s mrežom i DNS upitima.
# Ovaj kod se pruža samo u informativne svrhe i ne predstavlja gotovo rješenje za stvarne primjene.
# Prije korištenja ovog koda u stvarnom okruženju, preporučuje se pažljiva prilagodba koda specifičnim potrebama,
# provjera sigurnosnih aspekata i poštivanje pravila o zaštiti podataka. 
# Autori ovog koda ne snose odgovornost za bilo kakve gubitke ili probleme nastale korištenjem ovog koda.

#################################################################################################################

# Učitavanje potrebnih modula
import csv  # Modul za rad s CSV datotekama
import os  # Modul za rad s putanjama i direktorijima
import socket  # Modul za rad s mrežnim operacijama
import dns.resolver  # Modul za rad s DNS upitima


# Specificiranje imena ulaznog direktorija
import csv
import os
import socket
import dns.resolver

# Dohvaćanje putanje do korijenskog direktorija
root_folder_path = os.getcwd()

# Kreiranje putanje do ulaznog direktorija
input_folder_name = 'Projekt/cms_csv/'

# Kreiranje putanje do ulaznog direktorija
input_folder_path = os.path.join(root_folder_path, input_folder_name)

# Specificiranje imena izlaznog direktorija
output_folder_name = 'Projekt/IP-DNS'

# Stvara putanju do output foldera
output_folder_path = os.path.join(root_folder_path, output_folder_name)

# Kreiranje izlaznog direktorija ako ne postoji
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Dohvaćanje liste svih CSV datoteka u ulaznom direktoriju
csv_files = [file for file in os.listdir(input_folder_path) if file.endswith('.csv')]

# Petlja prolazi kroz svaku CSV datoteku
for file in csv_files:
    # Konstruiranje putanje za ulaznu datoteku
    input_file_path = os.path.join(input_folder_path, file)

    # Izvlačenje imena datoteke bez ekstenzije
    file_name = os.path.splitext(file)[0]

    # Konstruiranje imena izlazne datoteke s sufiksom "IP-dns"
    output_file_name = file_name + "_IP-dns.csv"

    # Konstruiranje putanje za izlaznu datoteku
    output_file_path = os.path.join(output_folder_path, output_file_name)

    # Otvaranje ulazne CSV datoteke s odgovarajućim kodiranjem
    with open(input_file_path, 'r', encoding='ISO-8859-1') as csv_file:
        # Kreiranje CSV čitača
        reader = csv.DictReader(csv_file)

        # Pronalaženje stupca 'url' u poljima CSV datoteke
        url_field = None
        fields = reader.fieldnames
        if 'url' in fields:
            url_field = 'url'
        else:
            for field in fields:
                if 'url' in field.lower():
                    url_field = field
                    break

        # Ako je pronađeno polje 'url'
        if url_field:
            # Kreiranje liste za spremanje izvučenih podataka
            data = []

            # Petlja koja prolazi kroz svaki redak CSV datoteke
            for row in reader:
                # Izvlačenje URL-a iz odgovarajućeg stupca
                url = row[url_field]

                # Uklanjanje prefiksa 'https://' iz URL-a
                if url.startswith('https://'):
                    url = url[8:]

                # Pronalaženje IP adrese za dobiveni URL
                try:
                    ip_address = socket.gethostbyname(url)
                except socket.gaierror:
                    ip_address = "Nije pronađeno"

                # Pronalaženje NS zapisa za dobiveni URL
                try:
                    ns_records = dns.resolver.resolve(url, 'NS')
                    ns_records = [ns.target.to_text() for ns in ns_records]
                except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.DNSException):
                    ns_records = "Nije pronađeno"

                # Dodavanje podataka u listu
                data.append({'URL': url, 'IP adresa': ip_address, 'NS zapisi': ns_records})

            # Kreiranje izlazne CSV datoteke (overwrite existing file)
            with open(output_file_path, 'w', newline='', encoding='utf-8') as output_file:
                # Definiranje imena stupaca za CSV pisca
                fieldnames = ['URL', 'IP adresa', 'NS zapisi']

                # Kreiranje CSV zapis
                writer = csv.DictWriter(output_file, fieldnames=fieldnames)

                # Pisanje zaglavlja u datoteku
                writer.writeheader()

                # Pisanje podataka u izlaznu CSV datoteku
                writer.writerows(data)
        else:
            print(f"Upozorenje: Nije pronađeno polje 'url' u datoteci {file}. Preskačem datoteku.")