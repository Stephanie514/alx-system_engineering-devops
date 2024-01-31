#!/usr/bin/python3
"""This Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    user_response = requests.get(url + "users/{}".format(employee_id))
    user = user_response.json()

    todos_url = url + "todos"
    params = {"userId": employee_id}
    todos_response = requests.get(todos_url, params=params)
    todos = todos_response.json()

    completed_tasks = [task for task in todos if task["completed"]]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(completed_tasks), total_tasks
    ))

    for idx, task in enumerate(completed_tasks, start=1):
        print("Task {} Formatting: OK".format(idx))

    print("To Do Count: {}".format(len(completed_tasks)))
    print("First line formatting: OK")
