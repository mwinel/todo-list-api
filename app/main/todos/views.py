from flask import jsonify, request
from app.main.todos import api
from app.main.todos.todo import create_new_todo, get_todo_by_title


@api.route("/todo", methods=['POST'])
def add_todo():
    title = request.json.get('title')
    if title == "":
        return jsonify({"message": "Fields cannot be left empty."}), 400
    if len(title) < 10:
        return jsonify({"message": "Title too short."}), 400
    todo_exists = get_todo_by_title(title)
    if todo_exists:
        return jsonify({"message": "Todo list already exists."}), 400
    return create_new_todo(title), 201
