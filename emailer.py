from email.mime.text import MIMEText
from datetime import date
import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = open('_user.txt', 'r').read().strip()
SMTP_PASSWORD = open('_pwd.txt', 'r').read().strip()

EMAIL_FROM = "testing123@gmail.com"

DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "

def send_email(subject, body, recipients):
    msg = MIMEText(body)
    msg['Subject'] = subject + " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(recipients)
    msg['From'] = EMAIL_FROM

    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, recipients, msg.as_string())
    mail.quit()

if __name__=='__main__':
    addr = "some_address@place.com"
    send_email("Python", "Once you learn branches (if's), I'll teach you this ;)", addr)
