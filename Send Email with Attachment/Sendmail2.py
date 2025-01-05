def email(to,server,filepathandname,subject,filename):
    # --- Check for File and Size Before Attachement ----
    import os
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    # Static Values <<< Update as Needed <<<<<<
    sender_email = "scotthead37@gmail.com"
    password = "AddYourAppPassword"  # Use an app password if 2FA is enabled
    
    # Variable Values    
    receiver_email = to
    filename = filename  # Replace with your file's name
    filepath = filepathandname  # Replace with the full file path      

    # Check if the file exists
    if os.path.exists(filepath):
        # Get the file size
        file_size = os.path.getsize(filepath)        


        # --- Send Email With Attachement ---
        if file_size > 2048:
            print('File OK')
            subject = subject
            body = ("Attachment Sent From: " + server)
            # Create the email message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = to
            message["Subject"] = subject
            # Attach the email body
            message.attach(MIMEText(body, "plain"))

            # --- Sends the Email ---
            try:
                # Open the file in binary mode and attach it
                with open(filepath, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                    # Encode the file for safe transport
                    encoders.encode_base64(part)

                    # Add headers to the attachment
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={filename}",  # File name as it will appear in the email
                    )

                    # Attach the file to the email
                    message.attach(part)

                    # Send the email
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()  # Upgrade the connection to secure
                    server.login(sender_email, password)  # Log in to your email account
                    server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
                    return print("Email with Attachment Sent Successfully!")
            except Exception as e:
                    return print("Error:", e)


        # --- Send Email Without Attachement and Warning ---
        else:
            print('File to Small')
            subject = ('Error File Too Small Check Write Permissions: ' + subject)
            body = ("No Attachment Sent From: " + server)
            # Create the email message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = to
            message["Subject"] = subject
            # Attach the email body
            message.attach(MIMEText(body, "plain"))

            # --- Sends the Email ---
            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()  # Upgrade the connection to secure
                    server.login(sender_email, password)  # Log in to your email account
                    server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
                    return print("Error: File Size too Small: Email Sent Successfull!")
            except Exception as e:
                    return print("Error:", e)
            
    # --- Send EMail with Error Message ---
    else:
        print('File Not Found')
        subject = ('Error File Not Found: ' + subject)
        body = ("No Attachment Found From: " + server)
        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = to
        message["Subject"] = subject
        # Attach the email body
        message.attach(MIMEText(body, "plain"))

        # --- Sends the Email ---
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Upgrade the connection to secure
                server.login(sender_email, password)  # Log in to your email account
                server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
                return print("Error: File Not Found: Email Sent Successfully")
        except Exception as e:
                return print("Error:", e)
