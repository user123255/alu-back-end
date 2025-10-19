#!/usr/bin/python3
"""
Exports data for all employees to a JSON file
Format:
{
    "USER_ID": [
        {"username": "USERNAME",
         "task": "TASK_TITLE",
         "completed": TASK_COMPLETED_STATUS},
        ...
    ],
    ...
}
File: todo_all_employees.json
"""

import json
import requests

if __name__ == "__main__":
    # Base URLs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users
    users = requests.get(users_url).json()

    # Prepare dictionary to hold all users’ tasks
    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Fetch tasks for the current user
        todos = requests.get(todos_url, params={"userId": user_id}).json()

        # Build a list of task dictionaries for this user
        user_tasks = []
        for task in todos:
            user_tasks.append({
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            })

        # Add this user’s data to the main dictionary
        all_data[user_id] = user_tasks

    # Export all data to JSON file
    with open("todo_all_employees.json", "w", encoding="utf-8") as json_file:
        json.dump(all_data, json_file)
