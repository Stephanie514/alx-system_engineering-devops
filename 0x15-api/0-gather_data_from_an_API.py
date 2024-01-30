#!/usr/bin/python3
"""This Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    employee_id = sys.argv[1]

    user_resp = requests.get(url + "users/{}".format(employee_id))

    user = user_resp.json()

    params = {"userId": employee_id}

    todos_resp = requests.get(url + "todos", params=params)

    todos = todos_resp.json()

    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{})".format(
        user.get("name"), len(completed), len(todos)))

    for complete in completed:
        print("\t{}".format(complete))
