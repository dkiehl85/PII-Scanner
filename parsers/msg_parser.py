import extract_msg


def read_msg(file_path):
    msg = extract_msg.Message(file_path)
    msg_message = msg.body or ""
    msg_subject = msg.subject or ""

    # Combine subject and body, split by lines
    text = msg_subject + "\n" + msg_message
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return lines
