#!/usr/bin/python3
"""
Script to gather data from an API
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(base_url, employee_id)
    todos_url = '{}/todos?userId={}'.format(base_url, employee_id)

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()
    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

    if user_response.status_code != 200:
        print("Error: User data not found")
        sys.exit(1)

    if todos_response.status_code != 200:
        print("Error: TODO list not found")
        sys.exit(1)

    employee_name = user_data.get('name')
    if not employee_name:
        print("Error: Employee name not found")
        sys.exit(1)

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    num_completed_tasks = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_completed_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
