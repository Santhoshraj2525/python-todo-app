import streamlit as sl
from modules import functions

todos = functions.get_todos()


def add_todo():
    todo = sl.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



sl.title("My To-Do App")
sl.subheader("This is my todo app.")
sl.write("This app is to increase the productivity")

for todo in todos:
    sl.checkbox(todo)

sl.text_input(label="", placeholder="Add new todo....", on_change=add_todo, key='new_todo')