#!/usr/bin/python3
"""show an employee's TODO list progress from a REST API."""
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # 1. GET the user and keep its "name"
    url = BASE_URL + "/users/" + employee_id
    response = requests.get(url)
    user = response.json()
    name = user.get("name")

    # 2. GET this user's todos
    todos_url = BASE_URL + "/todos?userId=" + employee_id
    response = requests.get(todos_url)
    todos = response.json()
    # 3. keep the completed ones
    done = []
    for todo in todos:
        if todo.get("completed"):
            done.append(todo)
    # 4. print the first line in the exact format
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done), len(todos)))
    # 5. print each completed title after a tab and a space
    for todo in done:
        print("\t " + todo.get("title"))
