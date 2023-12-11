"""
 pip freeze > requirements.txt
So what is requirements.txt?
This is a file which will be uploaded to the server
where we host this web app.
So that server should know
all the Python libraries the server needs to install
in order to run the web app correctly.
So the server has Python installed.
"""



import streamlit as st
import functions

st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This app used to increase the productivity")

todos = functions.get_todos()
print("1hello")
def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

for index,todo in enumerate(todos):
    checkbox= st.checkbox(todo, key=todo)
    print(checkbox)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")
print("2Hello")
st.session_state