import csv

# --- Example Usage ---
# -- Call and Update File Name --
#csv_exporter.export_to_csv(drives, filename="drives_info.csv")



# ---Filename will update with call to function ----
def export_to_csv(data, filename="output.csv"):
    """
    Exports data to a CSV file.
    
    Args:
        data (list of dict): The data to export.
        filename (str): The name of the CSV file.
    """
    if not data:
        print("No data to export.")
        return

    with open(filename, mode="w", newline="") as file:
        # Automatically derive fieldnames from the first dictionary entry
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        
        # Write header and data
        writer.writeheader()
        writer.writerows(data)

    print(f"Data has been saved to {filename}")
