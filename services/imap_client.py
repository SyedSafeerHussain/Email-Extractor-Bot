from imap_tools import MailBox,AND
from config.config import EMAIL,PASSWORD,FOLDER
from datetime import datetime

def fetch_emails(limit=1000,before_date=datetime(2025,7,1)):
    with MailBox("imap.gmail.com").login(EMAIL,PASSWORD,initial_folder=FOLDER) as mailbox:
        all_emails=list(mailbox.fetch(limit=limit))
        return all_emails
    