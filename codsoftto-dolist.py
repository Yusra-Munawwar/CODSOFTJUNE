import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        task_listbox.delete(index)
        if index < len(tasks):
            del tasks[index]
            save_tasks()


def update_task():
    selected_task = task_listbox.curselection()
    new_task = task_entry.get()
    if selected_task and new_task:
        index = selected_task[0]
        tasks[index] = new_task
        task_listbox.delete(index)
        task_listbox.insert(index, new_task)
        task_entry.delete(0, tk.END)
        save_tasks()

def mark_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        task = tasks[index]
        if not task.startswith("[Completed] "):
            tasks[index] = "[Completed] " + task
            task_listbox.delete(index)
            task_listbox.insert(index, tasks[index])
            save_tasks()

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            tasks = [task.strip() for task in tasks]
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

# Set background color
root.configure(bg="#f0f0f0")

tasks = []

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white")
add_button.pack()

task_listbox = tk.Listbox(root, width=40)
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#FF5733", fg="white")
delete_button.pack()

update_button = tk.Button(root, text="Update Task", command=update_task, bg="#4B0082", fg="white")
update_button.pack()

mark_completed_button = tk.Button(root, text="Mark as Completed", command=mark_completed, bg="#1E90FF", fg="white")
mark_completed_button.pack()

load_tasks()

root.mainloop()
