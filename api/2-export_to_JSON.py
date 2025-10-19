#!/usr/bin/python3
"""
2-export_to_JSON.py
Exports TODO list progress for a given employee ID to a JSON file.
"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch user data for a given employee ID."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching user data: {response.status_code}")
    return response.json()


def fetch_todos(employee_id):
    """Fetch TODO list for a given employee ID."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching TODO list: {response.status_code}")
    return response.json()


def export_to_json(employee, todos):
    """Export all tasks for the employee to a JSON file."""
    data = {
        str(employee['id']): [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee['username']
            }
            for task in todos
        ]
    }

    filename = f"{employee['id']}.json"
    with open(filename, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile)


def main():
    """Main function to run the script."""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee_id must be an integer")
        sys.exit(1)

    try:
        employee = fetch_employee_data(employee_id)
        todos = fetch_todos(employee_id)
        export_to_json(employee, todos)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
