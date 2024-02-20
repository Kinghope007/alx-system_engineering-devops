#!/usr/bin/python3
"""
Script to gather data from an API and export to CSV
"""

import requests
import csv
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

    employee_name = user_data.get('username')
    if not employee_name:
        print("Error: Employee name not found")
        sys.exit(1)

    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            writer.writerow([employee_id, employee_name, task.get('completed'), task.get('title')])
