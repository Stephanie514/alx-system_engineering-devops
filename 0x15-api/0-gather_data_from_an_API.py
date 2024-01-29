#!/usr/bin/python3
"""This Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    use = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    t_compl = [o.get("title") for o in todo if o.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        use.get("name"), len(t_compl), len(todo)))
    [print("\t {}".format(a)) for a in t_compl]
