import tkinter as tk
from tkinter import simpledialog, messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        # Task list
        self.tasks = []

        # Task entry
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task button
        tk.Button(master, text="Add Task", command=self.add_task).grid(row=0, column=1, padx=10, pady=10)

        # Task listbox
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        # Edit Task button
        tk.Button(master, text="Edit Task", command=self.edit_task).grid(row=2, column=0, padx=10, pady=10)

        # Delete Task button
        tk.Button(master, text="Delete Task", command=self.delete_task).grid(row=2, column=1, padx=10, pady=10)

        # Quit button
        tk.Button(master, text="Quit", command=self.master.destroy).grid(row=3, column=0, columnspan=2, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_to_edit = self.tasks[selected_index[0]]
            new_task = simpledialog.askstring("Edit Task", "Edit Task:", initialvalue=task_to_edit)
            if new_task:
                self.tasks[selected_index[0]] = new_task
                self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to edit.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Create the main window
root = tk.Tk()
app = TodoApp(root)

# Run the application
root.mainloop()
