from services.imap_client import fetch_emails
from utils.email_parser import extract_from_sender,extract_from_body
from utils.file_writer import save_to_excel
def main():
    print("🔄 Fetching emails...")
    all_emails=[]
    for email in fetch_emails(limit=1000):
        all_emails+=extract_from_sender(email)
        all_emails+=extract_from_body(email)
    print(f"📬 Total emails extracted (raw): {len(all_emails)}")
    save_to_excel(all_emails)
if __name__=="__main__":
    main()