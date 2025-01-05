# --- Import Custom SQL Module ---|
import csv
import sys
sys.path.append(r"C:\PYTHON\modules")
import SQL_Connect

# --- Customize Your Reader Query ----|
Query="SELECT name, address, phone FROM Customer_Info"

# --- Call SQL Module Function and Pass Query ---
rows=SQL_Connect.fetch_and_export_data(Query)

# --- Print rows to the screen
for row in rows:
    # --- Printing to Screen Formatted ----
    print(f"{row.name:<20} {row.address:<30} {row.phone:<15}")
    # --- Export results to CSV
    output_file = "Customer_Info_Export_Function.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        # --- Write header
        writer.writerow(["Name", "Address", "Phone"])
        # --- Write data rows
        writer.writerows(rows)
print(f"\nData exported to {output_file}")
