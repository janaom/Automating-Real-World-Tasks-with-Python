import shutil
import psutil
import socket
import emails
import os


def check_disk_usage():
    """Checks disk usage and sends an email if available space < 20%."""
    du = shutil.disk_usage("/")
    du_percentage = du.free / du.total * 100
    if du_percentage < 20:
        subject = "Error - Available disk space is less than 20%"
        message = emails.generate_error_email(sender, receiver, subject, body)
        emails.send_email(message)


def check_cpu_usage():
    """Checks CPU usage and sends an email if usage > 80%."""
    cpu_percentage = psutil.cpu_percent(1)
    if cpu_percentage > 80:
        subject = "Error - CPU usage is over 80%"
        message = emails.generate_error_email(sender, receiver, subject, body)
        emails.send_email(message)


def check_memory():
    """Checks available memory and sends an email if < 500MB."""
    threshold = 500 * 1024 * 1024  # 500MB
    available_memory = psutil.virtual_memory().available
    if available_memory < threshold:
        subject = "Error - Available memory is less than 500MB"
        message = emails.generate_error_email(sender, receiver, subject, body)
        emails.send_email(message)


def check_hostname_resolution():
    """Checks if the hostname can be resolved to '127.0.0.1' and sends an email if not."""
    hostname = socket.gethostbyname('localhost')
    if hostname != '127.0.0.1':
        subject = "Error - 'localhost' cannot be resolved to '127.0.0.1'"
        message = emails.generate_error_email(sender, receiver, subject, body)
        emails.send_email(message)


if __name__ == "__main__":
    sender = "automation@example.com"
    receiver = "<USERNAME>@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."

    check_disk_usage()
    check_cpu_usage()
    check_memory()
    check_hostname_resolution()
