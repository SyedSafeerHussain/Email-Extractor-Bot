import re
def extract_from_sender(email_obj):
    return [email_obj.from_]
def extract_from_body(email_obj):
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email_obj.text)
