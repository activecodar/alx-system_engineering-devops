#!/usr/bin/python3
"""
Exports data in JSON format from a REST API.

This script retrieves a list of users and todos from the JSONPlaceholder API,
and generates a JSON file that lists all the todos for each user.

Example:
    To run the script, simply execute it from the command line:
        $ python3 3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests


def get_all_users():
    """
    Retrieves a list of all users from the API.

    Returns:
        list: A list of dictionaries, each representing a user.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/users/")
    return response.json()


def get_all_todos():
    """
    Retrieves a list of todos from the API.

    Returns:
        list: A list of dictionaries, each representing a todo.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/todos/")
    return response.json()


def get_user_todos(user, todos):
    """
    Returns a list of todos for a given user ID.

    Args:
        user (dict): The user object.
        todos (list): A list of dictionaries, each representing a todo.

    Returns:
        list: A list of all todos for user.
    """
    username = user.get('username')
    user_id = user.get('id')
    user_todos = []
    for todo in todos:
        if todo.get('userId') == user_id:
            user_todos.append({'username': username,
                               'task': todo.get('title'),
                               'completed': todo.get('completed')})
    return user_todos


def export_data():
    """
    Exports data in JSON format.

    This function retrieves the users and todos from the API,
    generates a dictionary of todos for each user,
    and writes the dictionary to a JSON file.

    Returns:
        None
    """
    users = get_all_users()
    todos = get_all_todos()
    data = {str(user.get("id")): get_user_todos(user, todos) for user in users}
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    export_data()
