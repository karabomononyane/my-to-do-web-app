import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)



st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

'''
st.checkbox("Buy grocery")
st.checkbox("Throw the trash")
'''

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key = 'new_todo')

print("Hello")

st.session_state
