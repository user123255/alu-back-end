#!/usr/bin/python3
"""
Exports data for a given employee ID to CSV format.

Requirements:
- Records all tasks owned by this employee
- Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
- File name: USER_ID.csv
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Ensure user provided an employee ID
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # API endpoints (line split to follow PEP8 line length rule)
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = base_url + employee_id
    todos_url = base_url + employee_id + "/todos"

    # Fetch user and tasks data
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    # Extract username
    username = user.get("username")

    # File name based on employee ID
    filename = f"{employee_id}.csv"

    # Write data to CSV
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
