#!/usr/bin/python3
"""
Export data in the JSON format.
"""
import json
import requests
from sys import argv


def export_to_json():
    """
    Exports data in the JSON format.
    """
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user_tasks = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        tasks = requests.get(
            'https://jsonplaceholder.typicode.com/todos',
            params={'userId': user_id}).json()

        user_tasks[user_id] = []
        for task in tasks:
            user_tasks[user_id].append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed'),
            })

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_tasks, json_file)


if __name__ == "__main__":
    export_to_json()
