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
import json
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


def get_all_tasks(employee_id: int) -> tuple:
    """
    Fetch all tasks owned by the user.
    Args:
        employee_id: An integer representing the ID of the employee.
    Returns:
        tuple(user_data, todos)
    """
    return get_user_data(employee_id), get_user_todos(employee_id)


def export_to_json(user_data, todo_list):
    """
    Export all tasks owned by the user to a CSV file.
    Args:
        user_data: A dictionary containing the user's data.
        todo_list: A list of dictionaries representing the user's TODO list
    """
    try:
        user_id = user_data.get("id")
        username = user_data.get("username")
        filename = "{}.json".format(user_id)
        with open(filename, "w") as jsonfile:
            json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todo_list]}, jsonfile)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    user_bio, todos = get_all_tasks(int(sys.argv[1]))
    export_to_json(user_data=user_bio, todo_list=todos)
