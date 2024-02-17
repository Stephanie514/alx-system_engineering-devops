#!/usr/bin/python3
"""This exports to-do list information for a given
employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    todos_url = f"{url}todos"
    todos_params = {"userId": user_id}

    todos_response = requests.get(todos_url, params=todos_params)
    todos = todos_response.json()

    if todos:
        user = todos[0].get("user", {})
        username = user.get("username", "")
    else:
        print(f"No todos found for user ID: {user_id}")
        sys.exit(1)

    csv_file_path = f"{user_id}.csv"

    with open(csv_file_path, "w", newline="") as csvfile:
        fieldnames = [
            "USER_ID",
            "USERNAME",
            "TASK_COMPLETED_STATUS",
            "TASK_TITLE"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for task in todos:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": task.get("completed"),
                "TASK_TITLE": task.get("title")
            })
