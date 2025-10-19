#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
Fetches TODO list progress for a given employee ID using a REST API.
"""

import sys
import requests


def fetch_employee_data(employee_id):
    """Fetch employee info and TODO list from API."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        # Get employee info
        user_resp = requests.get(user_url)
        user_resp.raise_for_status()
        employee = user_resp.json()
        employee_name = employee.get("name")
        if not employee_name:
            print(f"No employee found with ID {employee_id}")
            sys.exit(1)

        # Get TODOs
        todos_resp = requests.get(todos_url)
        todos_resp.raise_for_status()
        todos = todos_resp.json()

        return employee_name, todos

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


def display_completed_tasks(employee_name, todos):
    """Print completed tasks in the required format."""
    completed_tasks = [task["title"] for task in todos if task["completed"]]
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for title in completed_tasks:
        print(f"\t{title}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee_id must be an integer")
        sys.exit(1)

    name, todos_list = fetch_employee_data(employee_id)
    display_completed_tasks(name, todos_list)

