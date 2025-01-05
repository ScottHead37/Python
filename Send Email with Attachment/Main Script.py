# --- Import my Mail Module ---
import sys
sys.path.append(r"C:\PYTHON\modules")
import sendmail2

# ---Run your script here and export data to a file ---




#-----------------------------------------------------


# ---Update as Needed ---
to = "shead@scriptsbyscott.com"
server = "From Server: WINSQL19"
# Path to Attachment
filepathandname = r"C:/PYTHON/Att/ServiceFile.csv"
subject = "Windows Services with Attached Email"
filename = "ServiceFile.csv"

# --- Call the email function ---
sendmail2.email(to, server, filepathandname, subject, filename)
