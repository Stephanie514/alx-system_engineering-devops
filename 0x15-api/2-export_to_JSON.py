#!/usr/bin/python3
"""Exports to-do list information for a given employee
ID to JSON format."""
import json
import requests
import sys


def export_to_json(user_id, user, todos):
    username = user.get("username")
    json_data = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos
        ]
    }

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(json_data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    user_response = requests.get(url + "users/{}".format(user_id))
    user = user_response.json()

    todos_response = requests.get(url + "todos", params={"userId": user_id})
    todos = todos_response.json()

    export_to_json(user_id, user, todos)
