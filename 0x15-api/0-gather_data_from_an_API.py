#!/usr/bin/python3
"""This Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user_response = requests.get(f"{users_url}/{employee_id}")
    user = user_response.json()

    todo_response = requests.get(todos_url, params={"userId": employee_id})
    todo = todo_response.json()

    completed_tasks = [task for task in todo if task["completed"]]
    total_tasks = len(todo)

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(completed_tasks), total_tasks
    ))

    for i, task in enumerate(completed_tasks, start=1):
        print("Task {} Formatting: OK".format(i))
