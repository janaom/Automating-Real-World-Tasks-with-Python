import email.message
import mimetypes
import os.path
import smtplib


def generate_email(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachment."""
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as attachment_file:
        message.add_attachment(
            attachment_file.read(),
            maintype=mime_type,
            subtype=mime_subtype,
            filename=attachment_filename
        )

    return message


def generate_error_email(sender, recipient, subject, body):
    """Creates an email without an attachment."""
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    return message


def send_email(message):
    """Sends the message to the configured SMTP server."""
    with smtplib.SMTP('localhost') as mail_server:
        mail_server.send_message(message)
