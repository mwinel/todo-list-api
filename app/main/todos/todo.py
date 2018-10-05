from flask import jsonify
from app.models import Todo
from app.db import Database


db = Database()


def create_new_todo(title):
    """
    This method creates a new todo.
    parameters: title
    returns: a json dictionary of a todo
    """
    todo = Todo(title=title)
    db.insert_todo_data(title)
    return jsonify(Todo=todo.serialize)


def get_all_todos():
    """
    This method returns a list of todos.
    """
    todos = db.fetch_all_todos()
    return jsonify(Todos=todos)


def get_todo_by_title(title):
    """
    This method checks for the todo-list given its title.
    parameters: title
    returns: todo-list
    """
    todo = db.get_by_argument('todos', 'title', title)
    return todo


def get_todo_by_id(todo_id):
    """
    This method checks for the todo-list given its id.
    parameters: todo_id
    returns: todo-list
    """
    todo = db.get_by_argument('todos', 'todo_id', todo_id)
    return jsonify(Todo={'todo_id': todo[0], 'title': todo[1]})
