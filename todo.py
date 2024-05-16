import streamlit as st
from datetime import datetime

class ToDoApp:
    def __init__(self):
        self.session = st.session_state
        if "active_tasks" not in self.session:
            self.session.active_tasks = []
        if "completed_tasks" not in self.session:
            self.session.completed_tasks = []

    def run(self):
        st.title("To-Do List App")

        # Sidebar for navigation
        selected_tab = st.sidebar.radio("Navigation", ["Active Tasks", "Completed Tasks"])

        if selected_tab == "Active Tasks":
            self.display_active_tasks()
        elif selected_tab == "Completed Tasks":
            self.display_completed_tasks()

    def display_active_tasks(self):
        task_input = st.text_input("Task:")
        priority_input = st.selectbox("Priority:", ["Low", "Medium", "High"])
        due_date_input = st.date_input("Due Date:", min_value=datetime.now())

        if st.button("Add Task"):
            if task_input:
                self.session.active_tasks.append((task_input, priority_input, due_date_input))
                st.success("Task added successfully.")

        st.write("## Active Tasks")
        for i, (task, priority, due_date) in enumerate(self.session.active_tasks, start=1):
            st.write(f"{i}. **{task}** - Priority: {priority}, Due Date: {due_date}")

            # Add complete task button
            if st.button(f"Complete Task {i}"):
                self.complete_task(i)

    def display_completed_tasks(self):
        st.write("## Completed Tasks")
        for i, (task, priority, due_date) in enumerate(self.session.completed_tasks, start=1):
            st.write(f"{i}. **{task}** - Priority: {priority}, Due Date: {due_date}")

    def complete_task(self, index):
        completed_task, priority, due_date = self.session.active_tasks.pop(index - 1)
        self.session.completed_tasks.append((completed_task, priority, due_date))

# Create an instance of ToDoApp and run the app
app = ToDoApp()
app.run()
