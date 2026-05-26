import csv
import os
from datetime import datetime

FILE_NAME = "user_feedback.csv"

def save_feedback(domain_id, feedback):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write header only once
        if not file_exists:
             writer.writerow(["timestamp", "domain_id", "feedback"])

        writer.writerow([datetime.now(), domain_id, feedback])