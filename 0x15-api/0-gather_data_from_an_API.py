#!/usr/bin/python3

"""
This script retrieves and prints the progress of an employee's TODO list.

The script takes an employee ID as input and uses the JSONPlaceholder REST API
to retrieve the employee's TODO list items. The progress of the TODO list is
then calculated and printed to standard output.

Example usage:
    $ python script.py 1

Output:
    Employee Leanne Graham is done with tasks (12/20):
         delectus aut autem
         ...

The script uses the following third-party libraries:
    - requests: To make HTTP requests to the JSONPlaceholder API.
"""
import requests

import sys


def get_user_data(user_id: int) -> dict:
    """Retrieve user data for the given user ID.

    Args:
        user_id: An integer representing the user ID.

    Returns:
        A dictionary containing the user's data.
    """
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    if response.ok:
        return response.json()


def get_user_todos(user_id: int) -> list:
    """Retrieve TODO list items for the given user ID.

    Args:
        user_id: An integer representing the user ID.

    Returns:
        A list of dictionaries representing
        the user's TODO list items.
    """
    url = "https://jsonplaceholder.typicode.com/" \
          "todos?userId={}".format(user_id)
    response = requests.get(url)
    if response.ok:
        return response.json()


def get_employee_todo_progress(employee_id: int) -> None:
    """Print the progress of the employee's TODO list.

    Args:
        employee_id: An integer representing the ID of the employee.

    Returns:
        None
    """
    user_bio = get_user_data(employee_id)
    todos = get_user_todos(employee_id)

    num_done_tasks = sum(todo.get("completed", None) for todo in todos)
    num_total_tasks = len(todos)
    employee_name = user_bio.get("name", None)
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks"
          "({}/{}):".format(employee_name, num_done_tasks, num_total_tasks))
    [print("\t {}".format(c)) for c in completed]


if __name__ == '__main__':
    get_employee_todo_progress(int(sys.argv[1]))
