import csv
import requests
import time

def get_addresses(filename):
    """Reads a CSV file and returns a list of IP addresses."""
    all_addresses = []
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        all_addresses = list(reader)  # Read all at once
    return all_addresses

def get_geolocation_and_whois(all_the_ip_address):
    """Fetches geolocation and WHOIS data for each IP address in the list."""
    print("Getting geo and WHOIS information...")

    if not all_the_ip_address:
        print("No IPs found in CSV!")
        return []

    headers = ['IP Address', 'Country', 'City', 'Organization', 'ASN']  # Add WHOIS headers
    updated_addresses = [headers]  # Start with headers

    for counter, line in enumerate(all_the_ip_address, start=1):
        ip_address = line[0]  # Extract IP
        print(f"Grabbing geo and WHOIS info for row #{counter}: {ip_address}")
        
        try:
            # Fetch geolocation data
            geo_response = requests.get(f'https://ipinfo.io/{ip_address}/json')
            geo_response.raise_for_status()
            geo_data = geo_response.json()
            country = geo_data.get('country', 'N/A')
            city = geo_data.get('city', 'N/A')
            
            # Fetch WHOIS data
            whois_response = requests.get(f'https://ipwhois.app/json/{ip_address}')
            whois_response.raise_for_status()
            whois_data = whois_response.json()
            organization = whois_data.get('org', 'N/A')
            asn = whois_data.get('asn', 'N/A')
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {ip_address}: {e}")
            country, city, organization, asn = 'N/A', 'N/A', 'N/A', 'N/A'

        updated_addresses.append([ip_address, country, city, organization, asn])  # Append data
        time.sleep(1)  # Avoid rate limits

    return updated_addresses

def create_csv(updated_address_list):
    """Writes the updated list to a CSV file."""
    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(updated_address_list)
    print("✅ Data written to output.csv!")

if __name__ == '__main__':
    csv_file = 'Book1.csv'
    all_the_ip_address = get_addresses(csv_file)
    updated_address_list = get_geolocation_and_whois(all_the_ip_address)
    create_csv(updated_address_list)
