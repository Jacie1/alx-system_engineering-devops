#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""
import requests
import sys

EMPLOYEE_API_ENDPOINT = 'https://jsonplaceholder.typicode.com/users/{}'
TODO_API_ENDPOINT = 'https://jsonplaceholder.typicode.com/todos?userId={}'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python todo_progress.py [employee_id]')
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch employee name
    employee_response = requests.get(EMPLOYEE_API_ENDPOINT.format(employee_id))
    employee_response.raise_for_status()
    employee = employee_response.json()

    # Fetch employee's TODO list
    todo_response = requests.get(TODO_API_ENDPOINT.format(employee_id))
    todo_response.raise_for_status()
    todo_list = todo_response.json()

    # Calculate TODO list progress
    total_tasks = len(todo_list)
    done_tasks = sum(1 for task in todo_list if task['completed'])

    # Print progress report
    print('Employee {} is done with tasks({}/{})'.format(employee['name'], done_tasks, total_tasks))
    for task in todo_list:
        if task['completed']:
            print('\t{} {}'.format('\t', task['title']))
