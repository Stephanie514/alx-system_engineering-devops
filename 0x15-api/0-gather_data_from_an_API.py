#!/usr/bin/python3
"""This Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    t_compl = [o.get("title") for o in todos if o.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(t_compl), len(todos)))
    [print("\t {}".format(a)) for a in t_compl]
