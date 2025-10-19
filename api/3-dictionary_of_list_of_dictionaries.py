#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py
Exports all TODO list progress for all employees to a JSON file.
"""

import json
import requests


def fetch_all_users():
    """Fetch all users from the API."""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching users: {response.status_code}")
    return response.json()


def fetch_todos_for_user(user_id):
    """Fetch TODO list for a specific user."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching TODOs for user {user_id}: {response.status_code}")
    return response.json()


def export_all_to_json(users):
    """Export all tasks for all users to a JSON file."""
    all_data = {}

    for user in users:
        todos = fetch_todos_for_user(user['id'])
        all_data[str(user['id'])] = [
            {
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            }
            for task in todos
        ]

    with open("todo_all_employees.json", mode='w', encoding='utf-8') as jsonfile:
        json.dump(all_data, jsonfile)


def main():
    """Main function to execute the script."""
    try:
        users = fetch_all_users()
        export_all_to_json(users)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
