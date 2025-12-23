import smtplib
import pandas as pd
import time
import logging
from email.message import EmailMessage

# =====================
# CONFIG
# =====================
EMAIL_ADDRESS = "your_email" # tukar
EMAIL_PASSWORD = "your_app_password" # tukar 
EXCEL_FILE = "list_test.xlsx" # tukar, this one just for testing

SEND_DELAY = 3
RETRY_DELAY = 5
MAX_RETRIES = 3

# =====================
# LOGGING
# =====================
logging.basicConfig(
    filename="email_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# =====================
# LOAD EXCEL
# =====================
df = pd.read_excel(EXCEL_FILE)

# =====================
# SMTP CONNECT
# =====================
def connect_smtp():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    return server

server = connect_smtp()

# =====================
# SEND FUNCTION
# =====================
def send_email(server, email, name):
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = email
    msg["Subject"] = "Important Announcement for testing"

    msg.set_content(f"Hi {name},\n\nThis is an important announcement.\n\nRegards,\nAhmad")

    # custom content email kat sini
    msg.add_alternative(f"""
    <html>
    <body style="font-family:Arial;">
        <h2>Hello {name}</h2>
        <p>This is an <b>important announcement</b>.</p>
        <p>Regards,<br><b>Fikri</b></p>
    </body>
    </html>
    """, subtype="html")

    server.send_message(msg)

# =====================
# MAIN LOOP
# =====================
for _, row in df.iterrows():
    email = row["Email"]
    name = row["Name"]

    attempt = 1
    sent = False

    while attempt <= MAX_RETRIES and not sent:
        try:
            send_email(server, email, name)
            print(f"Sent → {email}")
            logging.info(f"Sent {email} (Attempt {attempt})")
            sent = True
            time.sleep(SEND_DELAY)

        except Exception as e:
            print(f"Retry {attempt} failed → {email}")
            logging.warning(f"Retry {attempt} failed for {email}: {e}")
            attempt += 1
            time.sleep(RETRY_DELAY)

            try:
                server.quit()
            except:
                pass
            server = connect_smtp()

    if not sent:
        print(f"FAILED → {email}")
        logging.error(f"FAILED {email}")

server.quit()
print("All emails processed.")
