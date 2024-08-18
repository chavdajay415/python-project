import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email account credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'chavdakundan59@gmail.com'
password = "mshu wusn rjjy rrfx"

# Email details
from_email = 'chavdakundan59@gmail.com'
to_email = 'chavdajay@415gmail.com'
subject = 'Welcome to mumbai'
body = "Hii im jaychavda from mumbai"

# Create a MIME object
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

# Attach the email body to the MIME object
msg.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server and send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(username, password)
        server.send_message(msg)
        print("Email sent successfully.")
except Exception as e:
    print(f"Error: {e}")
