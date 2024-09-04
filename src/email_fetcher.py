import imaplib
import email
from email.header import decode_header
import configparser

def connect_to_email():

    config = configparser.ConfigParser()
    config.read("config.ini")
    
    IMAP_SERVER = config["EMAIL"]["IMAP_SERVER"]
    EMAIL_ADDRESS = config["EMAIL"]["EMAIL_ADDRESS"]
    PASSWORD = config["EMAIL"]["PASSWORD"]
    
    server = imaplib.IMAP4_SSL(IMAP_SERVER)
    server.login(EMAIL_ADDRESS, PASSWORD)
    server.select("inbox")
    return server

def fetch_emails(server, num_emails=10):
    # Search for all emails in the inbox
    status, messages = server.search(None, 'ALL')
    email_ids = messages[0].split()[-num_emails:]  # Get the last num_emails

    email_data = []
    
    for e_id in email_ids:
        # Fetch the email by ID
        status, msg_data = server.fetch(e_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                # Decode the email subject
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                
                # Decode the email sender
                sender, encoding = decode_header(msg.get("From"))[0]
                if isinstance(sender, bytes):
                    sender = sender.decode(encoding if encoding else "utf-8")
                
                # Get the email content
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        
                        # Get the email body
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            body = part.get_payload(decode=True).decode()
                            break
                else:
                    body = msg.get_payload(decode=True).decode()

                # Store the fetched data
                email_data.append({
                    "subject": subject,
                    "sender": sender,
                    "body": body  
                })
    
    return email_data

# Example usage
server = connect_to_email()
emails = fetch_emails(server)
for email in emails:
    print(f"Subject: {email['subject']}")
    print(f"From: {email['sender']}")
    print(f"body: {email['body']}")
    print("-" * 40)
