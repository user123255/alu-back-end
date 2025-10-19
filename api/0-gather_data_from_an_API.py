#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee ID.

Requirements:
- Uses requests module
- Accepts employee ID as a parameter
- Displays progress in the format:
  Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
     TASK_TITLE
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(base_url, employee_id)
    todos_url = "{}todos?userId={}".format(base_url, employee_id)

    # Fetch user and todo data
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")

    # Calculate task stats
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    # Print header line
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done_tasks, total_tasks
        )
    )

    # Print titles of completed tasks
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
