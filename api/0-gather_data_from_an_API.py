#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
Fetches TODO list progress for a given employee ID using a REST API
"""

import sys
import requests


def fetch_employee_data(employee_id):
    """Fetch user data for a given employee ID."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)
    if response.status_code != 200:
        raise Exception(f"Error fetching user data: {response.status_code}")
    return response.json()


def fetch_todos(employee_id):
    """Fetch TODO list for a given employee ID."""
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(todos_url)
    if response.status_code != 200:
        raise Exception(f"Error fetching TODO list: {response.status_code}")
    return response.json()


def display_todo_progress(employee, todos):
    """Display TODO list progress in the specified format."""
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)

    print(f"Employee {employee['name']} is done with tasks "
          f"({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task['title']}")


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
        display_todo_progress(employee, todos)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()

