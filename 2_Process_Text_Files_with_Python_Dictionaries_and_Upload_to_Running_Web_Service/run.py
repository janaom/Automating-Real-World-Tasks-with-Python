#!/usr/bin/env python3
import os
import requests

# Set the directory where feedback files are located
feedback_directory = "/data/feedback/"

# Get the list of feedback files in the directory
feedback_files = os.listdir(feedback_directory)

# Function to read lines from a file and return them as a list
def read_lines(file):
    with open(os.path.join(feedback_directory, file)) as f:
        lines = f.read().splitlines()
    return lines

# Load the feedback entries into a list of dictionaries
feedback_list = []
keys = ["title", "name", "date", "feedback"]
for file in feedback_files:
    lines = read_lines(file)
    feedback_dict = dict(zip(keys, lines))
    feedback_list.append(feedback_dict)

# Set the URL for submitting feedback entries
url = "http://<corpweb external IP address>/feedback/"

# Submit the feedback entries
for entry in feedback_list:
    response = requests.post(url, json=entry)
    if response.ok:
        print("Successfully submitted feedback entry")
    else:
        print(f"Error submitting feedback entry: {response.status_code}")
