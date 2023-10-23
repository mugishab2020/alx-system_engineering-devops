#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_response = requests.get(f'{base_url}users/{employee_id}')
    user_data = user_response.json()
    name = user_data.get('name')
    todo_response = requests.get(f'{base_url}todos?userId={employee_id}')
    todo_data = todo_response.json()
    total_tasks = len(todo_data)
    tasks = sum(1 for task in todo_data if task['completed'])
    print(f"Employee {name} is done with tasks({tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"    {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
