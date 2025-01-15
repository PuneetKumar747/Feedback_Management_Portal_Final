import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import os

def send_email():
    sender_email = "kpuneet474@gmail.com"
<<<<<<< HEAD:utils.py
    # receiver_emails = ["su-cof2027@sitare.org"]  # List of recipient emails
    receiver_emails = ["su-23028@sitare.org"]  # List of recipient emails
=======
    receiver_emails = ["su-2308@sitare.org"]
>>>>>>> 0e5b3eef703f42d95c39efd7f6b1b764f0362d4d:sheduler.py
    subject = "Weekly Reminder for feedback"
    body = "All students, please fill the feedback for all subjects."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
<<<<<<< HEAD:utils.py

    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')
 # Use app-specific password for security
=======
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')
>>>>>>> 0e5b3eef703f42d95c39efd7f6b1b764f0362d4d:sheduler.py

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        
        for recipient_email in receiver_emails:
            msg['To'] = recipient_email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email sent to {recipient_email}")
        
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

<<<<<<< HEAD:utils.py
# Schedule the email to be sent every Monday at 10:48 AM
schedule.every().monday.at("19:17").do(send_email)
=======
# Schedule the email to be sent every Monday at 11:21 AM
# Additionally, check for pending tasks every 30 minutes
schedule.every(30).minutes.do(send_email)
>>>>>>> 0e5b3eef703f42d95c39efd7f6b1b764f0362d4d:sheduler.py

# Run the scheduling loop
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait a minute before checking again
