import imaplib
import email
from email.header import decode_header
from text_preprocessor import preprocess_text

def connect_to_email(username, password, imap_server):
    server = imaplib.IMAP4_SSL(imap_server)
    server.login(username, password)
    server.select("inbox")
    return server

def fetch_emails(server):
    status, messages = server.search(None, 'ALL')
    email_ids = messages[0].split()[-20:]  # Fetch the last 20 emails
    emails = []

    for email_id in email_ids:
        res, msg = server.fetch(email_id, "(RFC822)")
        for response_part in msg:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                subject, encoding = decode_header(msg["Subject"])[0]
                subject = subject.decode(encoding if encoding else "utf-8") if isinstance(subject, bytes) else subject
                sender = msg.get("From")

                body = None
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()
                else:
                    body = msg.get_payload(decode=True).decode()

                if body:
                    preprocessed_body = preprocess_text(body)
                    emails.append({
                        "subject": subject,
                        "sender": sender,
                        "snippet": body[:100],
                        "preprocessed_body": preprocessed_body
                    })

    return emails
