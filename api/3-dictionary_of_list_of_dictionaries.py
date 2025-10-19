#!/usr/bin/python3
"""
Exports all employee tasks to JSON format.
File: todo_all_employees.json
"""

import json
import requests


if __name__ == "__main__":
    # Base URLs for users and todos endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all users
    users = requests.get(users_url).json()

    # Dictionary to hold all users' tasks
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # Fetch tasks for each user
        todos = requests.get(todos_url, params={"userId": user_id}).json()

        # Structure data for each user
        user_tasks = []
        for todo in todos:
            task_data = {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            user_tasks.append(task_data)

        # Assign to main dictionary
        all_tasks[user_id] = user_tasks

    # Write data to JSON file
    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        json.dump(all_tasks, f)

