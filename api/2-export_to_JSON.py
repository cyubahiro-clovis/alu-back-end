#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file using a REST API."""
import json
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # 1. GET the user and keep its "username"
    url = BASE_URL + "/users/" + employee_id
    response = requests.get(url)
    user = response.json()
    username = user.get("username")

    # 2. GET this user's todos
    todos_url = BASE_URL + "/todos?userId=" + employee_id
    response = requests.get(todos_url)
    todos = response.json()

    # 3. build one dictionary per task
    tasks = []
    for todo in todos:
        tasks.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username
        })

    # 4. write {USER_ID: [tasks]} to USER_ID.json
    with open("{}.json".format(employee_id), "w") as f:
        json.dump({employee_id: tasks}, f)
