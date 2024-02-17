#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests


def export_all_to_json(users):
    url = "https://jsonplaceholder.typicode.com/"

    all_data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        all_data[user_id] = [
            {
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed"),
            } for t in todos
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    export_all_to_json(users)
