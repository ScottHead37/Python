import psutil
import importlib.util
import sys

# Dynamically load the module using the full path
module_path = r"C:\PYTHON\modules\Module CSV Exporter.py"
spec = importlib.util.spec_from_file_location("csv_exporter", module_path)
csv_exporter = importlib.util.module_from_spec(spec)
sys.modules["csv_exporter"] = csv_exporter
spec.loader.exec_module(csv_exporter)

# --------- Get Drive Information ----------------------
def get_drive_info():
    drives = []
    for partition in psutil.disk_partitions(all=False):
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            drives.append({
                "Device": partition.device,
                "Total Size (GB)": round(usage.total / (1024 ** 3), 2),
                "Used (GB)": round(usage.used / (1024 ** 3), 2),
                "Free (GB)": round(usage.free / (1024 ** 3), 2),
                "Usage (%)": usage.percent,
            })
        except PermissionError as e:
            print('Drive Error - Permission Denied', partition.device)           
    return drives

if __name__ == "__main__":
    # Get drive information
    drives = get_drive_info()
    
    # Print the data to screen
    for drive in drives:
        print(drive)

    # Export to CSV using the dynamically imported module
    csv_exporter.export_to_csv(drives, filename="drives_info.csv")
