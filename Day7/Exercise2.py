"""
Assignment 2: Multi-Format Log Converter (Text to CSV & JSON)
Scenario
A server records raw access events as unformatted plain-text log lines. 
You need to parse the log lines into structured records and export them to both CSV and JSON formats.


Problem Description
Create a function convert_log_file(input_log_path, output_csv_path, output_json_path):

Each line in input_log_path follows the format: "<TIMESTAMP> | <USER_ID> | <ENDPOINT> | <STATUS_CODE>" 
(e.g., "2026-09-01 10:15:30 | USR102 | /api/v1/predict | 200").
Parses each line into a dictionary containing keys: timestamp, user_id, endpoint, status_code (as integer).
Writes all parsed records to output_csv_path with a header row using csv.DictWriter.
Writes the list of records to output_json_path with an indentation of 2 spaces using json.dump().
Example Walkthrough
convert_log_file("server_access.log", "access_records.csv", "access_records.json")

"""

import csv
import json


def convert_log_file(input_log_path, output_csv_path, output_json_path):

    records = []

    with open(input_log_path, "r") as file:

        for line in file:

            line = line.strip()

            if line == "":
                continue

            parts = line.split("|")

            timestamp = parts[0].strip()
            user_id = parts[1].strip()
            endpoint = parts[2].strip()
            status_code = int(parts[3].strip())

            record = {
                "timestamp": timestamp,
                "user_id": user_id,
                "endpoint": endpoint,
                "status_code": status_code
            }

            records.append(record)

    with open(output_csv_path, "w", newline="") as file:

        fieldnames = [
            "timestamp",
            "user_id",
            "endpoint",
            "status_code"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(records)

    with open(output_json_path, "w") as file:

        json.dump(
            records,
            file,
            indent=2
        )

def main():
    convert_log_file("server_access.log","access_records.csv","access_records.json")
    print("Log conversion completed successfully.")

main()