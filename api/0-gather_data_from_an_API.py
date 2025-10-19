#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
Fetches TODO list progress for a given employee ID using a REST API.
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee_id must be an integer")
        sys.exit(1)

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        # Get employee info
        user_resp = requests.get(user_url)
        user_resp.raise_for_status()
        employee_name = user_resp.json().get("name")

        # Get TODOs for employee
        todos_resp = requests.get(todos_url)
        todos_resp.raise_for_status()
        todos_data = todos_resp.json()

        # Filter completed tasks
        completed_tasks = [task["title"] for task in todos_data if task["completed"]]

        total_tasks = len(todos_data)
        done_tasks = len(completed_tasks)
        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for title in completed_tasks:
            print(f"\t {title}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

