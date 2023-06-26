import csv
import os
import socket
import dns.resolver

# Get the root project folder path
root_folder_path = os.getcwd()

# Specify the input folder name
input_folder_name = 'Projekt/cms_csv'

# Create the input folder path
input_folder_path = os.path.join(root_folder_path, input_folder_name)

# Specify the output folder name
output_folder_name = 'Projekt/IP-DNS'

# Create the output folder path
output_folder_path = os.path.join(root_folder_path, output_folder_name)

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Get a list of all CSV files in the input folder
csv_files = [file for file in os.listdir(input_folder_path) if file.endswith('.csv')]

# Iterate over each CSV file
for file in csv_files:
    # Construct the full input file path
    input_file_path = os.path.join(input_folder_path, file)

    # Extract the file name without extension
    file_name = os.path.splitext(file)[0]

    # Construct the output file name with the suffix "IPdns"
    output_file_name = file_name + "_IP-dns.csv"

    # Construct the full output file path
    output_file_path = os.path.join(output_folder_path, output_file_name)

    # Open the input CSV file
    with open(input_file_path, 'r') as csv_file:
        # Create a CSV reader
        reader = csv.DictReader(csv_file)

        # Create a list to store the extracted data
        data = []

        # Iterate over each row in the CSV
        for row in reader:
            # Check if the 'url' key exists
            if 'url' in row:
                # Extract the URL from the 'url' column
                url = row['url']

                # Remove the 'https://' prefix from the URL
                if url.startswith('https://'):
                    url = url[8:]

                # Find the IP address for the URL
                try:
                    ip_address = socket.gethostbyname(url)
                except socket.gaierror:
                    ip_address = "Not Found"

                # Find the NS records for the URL
                try:
                    ns_records = dns.resolver.resolve(url, 'NS')
                    ns_records = [ns.target.to_text() for ns in ns_records]
                except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.DNSException):
                    ns_records = "Not Found"

                # Append the data to the list
                data.append({'URL': url, 'IP Address': ip_address, 'NS Records': ns_records})

    # Create the output CSV file
    with open(output_file_path, 'w', newline='') as output_file:
        # Define the field names for the CSV writer
        fieldnames = ['URL', 'IP Address', 'NS Records']

        # Create a CSV writer
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the data to the output CSV file
        writer.writerows(data)