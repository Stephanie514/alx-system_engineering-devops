#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import urllib.parse
import urllib.request
import sys


def get_user_info(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    with urllib.request.urlopen(url) as response:
        user = json.loads(response.read().decode())
    return user


def get_user_todos(employee_id):
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": employee_id}
    data = urllib.parse.urlencode(params).encode()
    with urllib.request.urlopen(url, data=data) as response:
        todos = json.loads(response.read().decode())
    return todos


def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    user = get_user_info(employee_id)
    todos = get_user_todos(employee_id)

    completed = [t.get("title") for t in todos if t.get("completed")]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), total_tasks))

    for c in completed:
        print("\t{}".format(c))


if __name__ == "__main__":
    main()
