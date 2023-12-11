import streamlit as st
import function_todoapp

todos = function_todoapp.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function_todoapp.write_todos(todos)

st.title("Todo-App")
st.subheader("This is a todo app")
st.write("This is to increase your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function_todoapp.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="",placeholder="Enter a todo....",
              on_change=add_todo,key='new_todo')

