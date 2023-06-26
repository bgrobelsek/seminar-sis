#čita json zapise i sortira u csv datoteke prema tipu CMSa i SPREMA U ZASEBNI FOLDER "cms_csv"

import os
import json
import csv

def export_data_to_csv_and_txt(directory):
    wp_data = []
    shopify_data = []
    magento_data = []
    presta_data = []
    wix_data = []
    salesforce_data = []
    drupal_data = []
    other_data = []

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

    output_directory = 'Projekt/cms_csv'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Export to wp.csv
    if wp_data:
        csv_file_path = os.path.join(output_directory, 'wp.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(wp_data[0].keys())  # Write header row
            for data in wp_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'wp.csv'))

    # Export to shopify.csv
    if shopify_data:
        csv_file_path = os.path.join(output_directory, 'shopify.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(shopify_data[0].keys())  # Write header row
            for data in shopify_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'shopify.csv'))
    
    # Export to magento.csv
    if magento_data:
        csv_file_path = os.path.join(output_directory, 'magento.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(magento_data[0].keys())  # Write header row
            for data in magento_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'magento.csv'))
        
    # Export to presta.csv
    if presta_data:
        csv_file_path = os.path.join(output_directory, 'presta.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(presta_data[0].keys())  # Write header row
            for data in presta_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'presta.csv'))

    # Export to wix.csv
    if wix_data:
        csv_file_path = os.path.join(output_directory, 'wix.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(wix_data[0].keys())  # Write header row
            for data in wix_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'wix.csv'))

    # Export to salesforce.csv
    if salesforce_data:
        csv_file_path = os.path.join(output_directory, 'salesforce.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(salesforce_data[0].keys())  # Write header row
            for data in salesforce_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'salesforce.csv'))
    
    # Export to drupal.csv
    if drupal_data:
        csv_file_path = os.path.join(output_directory, 'drupal.csv')
        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(drupal_data[0].keys())  # Write header row
            for data in drupal_data:
                writer.writerow(data.values())
        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(os.path.join(output_directory, 'drupal.csv'))
            
    # Export to export.csv and export.txt
    if other_data:
        csv_file_path = os.path.join(output_directory, 'export.csv')

        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for data in other_data:
                csv_writer.writerow(data.values())

        print(f"Data exported to {csv_file_path} (CSV).")
    else:
        create_empty_file(csv_file_path)

def create_empty_file(file_path):
    open(file_path, 'a').close()

if __name__ == '__main__':
    directory = 'CMSeek/Result'

    export_data_to_csv_and_txt(directory)
