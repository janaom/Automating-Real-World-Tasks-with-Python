import os
import datetime
import reports
import emails

# Get current date in the required format
current_date = datetime.date.today().strftime("%B %d, %Y")
date = "Processed Update on " + current_date

# Initialize lists to store fruit names and weights
names = []
weights = []

# Set the path to the directory containing the fruit description files
path = "./supplier-data/descriptions/"

# Iterate over the files in the description directory
for file in os.listdir(path):
    with open(os.path.join(path, file)) as f:
        for line in f:
            line = line.strip()

            # Check if the line contains the fruit name
            if len(line) <= 10 and len(line) > 0 and "lb" not in line:
                fruit_name = "name: " + line
                names.append(fruit_name)

            # Check if the line contains the fruit weight
            if "lbs" in line:
                fruit_weight = "weight: " + line
                weights.append(fruit_weight)

# Create a summary string with fruit names and weights
summary = ""
for name, weight in zip(names, weights):
    summary += name + '<br />' + weight + '<br />' + '<br />'

if __name__ == "__main__":
    # Generate the PDF report with the summary
    reports.generate_report("/tmp/processed.pdf", date, summary)

    # Set the sender, receiver, subject, and body for the email
    sender = "automation@example.com"
    receiver = "<USERNAME>@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    # Generate the email message with the PDF attachment
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")

    # Send the email
    emails.send_email(message)
