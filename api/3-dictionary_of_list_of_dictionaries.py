#!/usr/bin/python3
"""Export every employee's TODO list to one JSON file using a REST API."""
import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    # 1. GET all users and all todos: two requests in total
    users = requests.get(BASE_URL + "/users").json()
    todos = requests.get(BASE_URL + "/todos").json()

    # 2. for each user, collect their todos like in task 2
    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        tasks = []
        for todo in todos:
            if todo.get("userId") == user_id:
                tasks.append({
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                })
        all_tasks[str(user_id)] = tasks

    # 3. write everything to todo_all_employees.json
    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)
