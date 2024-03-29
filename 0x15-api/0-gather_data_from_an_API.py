#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        prin("Usage: ./file_name id")
    id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    req = requests.get(url).json()
    tasks_url = url + "/todos"
    tasks = requests.get(tasks_url).json()

    completed_tasks = []
    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):"
          .format(req['name'], len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t {}".format(task))
