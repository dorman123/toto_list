# Set the Execution Policy to allow scripts to run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# for activating the venv: .\venv\Scripts\activate.bat
# for running the code in the terminal: python -m streamlit run c:/visualstodio_projects/udemy-learning-lessons-1-20/project_todo_list/to_to_list_project_website/web.py

import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo.title() + '\n')
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo)
    if checkbox:
        todos.pop(index)

        functions.write_todos(todos)

st.text_input(label="", placeholder='Add new todo:', on_change=add_todo, key='new_todo')
