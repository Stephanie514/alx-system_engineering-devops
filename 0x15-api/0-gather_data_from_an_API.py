#!/usr/bin/python3
"""This Returns to-do list information for a given employee ID."""
import json
import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    with urllib.request.urlopen(
            url + "users/{}".format(employee_id)) as response:
        user = json.loads(response.read().decode())

    with urllib.request.urlopen(
            url + "todos", data=b'userId={}'.format(
                employee_id.encode())) as response:
        todos = json.loads(response.read().decode())

    completed = [t.get("title") for t in todos if t.get("completed")]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), total_tasks))

    for c in completed:
        print("\t {}".format(c))
