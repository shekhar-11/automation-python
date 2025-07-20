import smtplib
from dotenv import load_dotenv

load_dotenv()
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("MAIL_ID", "MAIL_PASS")
# message to be sent
message = "Hello maa"
# sending the mail
receiver_pass="abc@gmail.com"
s.sendmail("MAIL_ID", receiver_pass, message)
# terminating the session
s.quit()