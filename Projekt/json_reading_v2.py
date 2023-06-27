# -*- coding: utf-8 -*-
# CMS (eng. Content Management System, (sustav za upravljanje sadržajem))
#
# OPCA NAMJENA PROGRAMA
#
# Python kod nakon komentara cita JSON datoteke koje su pronadjene putem CMSeek aplikacije.
# Sve datoteke koje se nalaze u direktoriju 'Result' biti ce procitane i sortirane te ce program kreirati nove CSV i TXT datoteke.
# Program cita CMS modul i prema njihovim identifikacijskim oznakama ih sortira, te kreira ili dodaje zapis u CSV datoteke odgovarajuceg modula.
# Novo kreirane CSV datoteke ce biti pospremljene u novi direktorij nazvan "cms_csv" koji se nalazi u root-u programa.
# Svaka CSV datoteka ce biti sortirana po odgovarajucem CMS-u (npr. WordPress = wp.csv; Shopify=shopify.csv).
# Novo kreirane CSV datoteke ce sadrzavati uzglavlje i atribute CMS-ova.
# U slucaju da ne prepozna trazeni identifikator CMS modula, podatci iz JSON datoteke se zapisuju u "export.csv" i "export.txt" koji se nalazi u "cms_csv" direktoriju.



# Modul pomocu kojega citamo i komuniciramo sa OS komponentama.
import os
# Modul potreban za citanje JSON file-ova
import json
# Modul potreban za citanje CSV file-ova
import csv

# Funkcija za citanje i spremanje CMS modula u listu, po kategorijama
def export_data_to_csv_and_txt(directory):
    wp_data = []
    shopify_data = []
    magento_data = []
    presta_data = []
    wix_data = []
    salesforce_data = []
    drupal_data = []
    other_data = []

# Citanje direktorija koji je zadan parametrom funkcije os.walk(directory) i pokretanje petlje citanja datoteka koje zavrsavaju ekstenzijom .json.
# Ukoliko takve datoteke postoje, otvaraju se, te se sukladno cms_id-u (koji se nalazi u samoj datoteci) zapisuje u odgovarajucu listu.
# U slucaju da se ciljana datoteka ne uspije procitati, ispisuje se greska. 
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    try:
                        data = json.load(f)
                        cms_id = data.get('cms_id', '')
                        if cms_id == 'wp':
                            wp_data.append(data)
                        elif cms_id == 'shopify':
                            shopify_data.append(data)
                        elif cms_id == 'mg':
                            magento_data.append(data)
                        elif cms_id == 'presta':
                            presta_data.append(data)
                        elif cms_id == 'wix':
                            wix_data.append(data)
                        elif cms_id == 'sfcc':
                            salesforce_data.append(data)
                        elif cms_id == 'dru':
                            drupal_data.append(data)                
                        elif cms_id != '':
                            other_data.append(data)
                    except json.JSONDecodeError:
                        print(f"Error: Failed to decode JSON file '{file_path}'")

    # Lokacija za spremanje CMS modula u CSV obliku.
    # Kreiranje novog direktorija na lokaciji gdje je program pokrenut, ukoliko takav direktorij vec ne postoji.
    output_directory = 'Projekt/cms_csv'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Spremanje WordPress CMS modula, iz liste "wp_data", u "wp.csv" datoteku
    if wp_data:
        csv_file_path = os.path.join(output_directory, 'wp.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(wp_data[0].keys())  # Zapisivanje atributa CMS-a u prvu liniju CSV datoteke
            for data in wp_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'wp.csv'))

    # Spremanje Magento CMS modula, iz liste "magento_data", u "magento.csv" datoteku
    if shopify_data:
        csv_file_path = os.path.join(output_directory, 'shopify.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(shopify_data[0].keys())  # Zapisivanje atributa CMS-a u prvu liniju CSV datoteke
            for data in shopify_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'shopify.csv'))
    
    # Spremanje Magento CMS modula, iz liste "magento_data", u "magento.csv" datoteku
    if magento_data:
        csv_file_path = os.path.join(output_directory, 'magento.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(magento_data[0].keys())  # Zapisuje atribute CMS-a u prvu liniju CSV datoteke
            for data in magento_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'magento.csv'))
        
    # Spremanje Presta CMS modula, iz liste "presta_data", u "presta.csv" datoteku
    if presta_data:
        csv_file_path = os.path.join(output_directory, 'presta.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(presta_data[0].keys())  # Zapisuje atribute CMS-a u prvu liniju CSV datoteke
            for data in presta_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'presta.csv'))

    # Spremanje Wix CMS modula i njezine podatke, iz liste "wix_data", u "wix.csv" datoteku
    if wix_data:
        csv_file_path = os.path.join(output_directory, 'wix.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(wix_data[0].keys())  # Zapisuje atribute CMS-a u prvu liniju CSV datoteke
            for data in wix_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'wix.csv'))

    # Spremanje Salesforce CMS modula i njezine podatke, iz liste "salesforce_data", u "salesforce.csv" datoteku
    if salesforce_data:
        csv_file_path = os.path.join(output_directory, 'salesforce.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(salesforce_data[0].keys())  # Zapisuje atribute CMS-a u prvu liniju CSV datoteke
            for data in salesforce_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'salesforce.csv'))
    
    # Spremanje Drupal CMS modula i njezine podatke, iz liste "drupal_data", u "drupal.csv" datoteku
    if drupal_data:
        csv_file_path = os.path.join(output_directory, 'drupal.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(drupal_data[0].keys())  # Zapisuje atribute CMS-a u prvu liniju CSV datoteke
            for data in drupal_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'drupal.csv'))
            
    # U slucaju da program nije procitao trazeni CMS modul, kreira CSV datoteku "export.csv"
    # i zapisuje podatke iz JSON datoteke
    if other_data:
        csv_file_path = os.path.join(output_directory, 'export.csv')

        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for data in other_data:
                csv_writer.writerow(data.values())

        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(csv_file_path)

# Funkcija za kreiranje praznog direktorija u glavnom direktoriju, gdje se nalazi program.
def create_empty_file(file_path):
    open(file_path, 'a').close()

# Blok koda koji provjerava pokrece li se program samostalno ili ne.
if __name__ == '__main__':
    directory = 'CMSeek/Result'

    export_data_to_csv_and_txt(directory)
