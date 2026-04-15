import streamlit as sl
from modules import functions

todos = functions.get_todos()

sl.title("My To-Do App")
sl.subheader("This is my todo app.")
sl.write("This app is to increase the productivity")

for todo in todos:
    sl.checkbox(todo)

sl.text_input(label="", placeholder="Add new todo....")