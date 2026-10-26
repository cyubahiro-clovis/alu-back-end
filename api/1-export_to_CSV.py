#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file using a REST API."""
import csv
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

    # 3. write one row per task to USER_ID.csv
    with open("{}.csv".format(employee_id), "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            status = todo.get("completed")
            title = todo.get("title")
            writer.writerow([employee_id, username, status, title])
