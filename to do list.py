import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel, QMessageBox, QHBoxLayout

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.tasks = []
        self.initUI()

    def initUI(self):
        # Layout
        self.setWindowTitle('To-Do List Application')
        layout = QVBoxLayout()
        # Task List
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)
        # Input fields
        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Task Title")
        layout.addWidget(self.title_input)
        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText("Task Description")
        layout.addWidget(self.description_input)
        # Priority Input
        self.priority_input = QLineEdit(self)
        self.priority_input.setPlaceholderText("Priority (low, medium, high)")
        layout.addWidget(self.priority_input)
        # Deadline Input
        self.deadline_input = QLineEdit(self)
        self.deadline_input.setPlaceholderText("Deadline (optional)")
        layout.addWidget(self.deadline_input)
        # Buttons
        button_layout = QHBoxLayout()
        add_button = QPushButton("Add Task", self)
        add_button.clicked.connect(self.add_task)
        button_layout.addWidget(add_button)

        delete_button = QPushButton("Delete Task", self)
        delete_button.clicked.connect(self.delete_task)
        button_layout.addWidget(delete_button)

        save_button = QPushButton("Save Tasks", self)
        save_button.clicked.connect(self.save_tasks)
        button_layout.addWidget(save_button)

        load_button = QPushButton("Load Tasks", self)
        load_button.clicked.connect(self.load_tasks)
        button_layout.addWidget(load_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def add_task(self):
        title = self.title_input.text()
        description = self.description_input.text()
        priority = self.priority_input.text()
        deadline = self.deadline_input.text()

        if title and priority:
            task = {
                'title': title,
                'description': description,
                'priority': priority,
                'deadline': deadline,
                'completed': False
            }
            self.tasks.append(task)
            self.task_list.addItem(f"{title} [{priority}]")
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Error", "Title and Priority are required fields!")

    def delete_task(self):
        selected_task = self.task_list.currentRow()
        if selected_task >= 0:
            self.task_list.takeItem(selected_task)
            del self.tasks[selected_task]
        else:
            QMessageBox.warning(self, "Error", "Please select a task to delete!")

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)
        QMessageBox.information(self, "Success", "Tasks saved successfully!")

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
                self.task_list.clear()
                for task in self.tasks:
                    self.task_list.addItem(f"{task['title']} [{task['priority']}]")
            QMessageBox.information(self, "Success", "Tasks loaded successfully!")
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "No saved tasks found!")

    def clear_inputs(self):
        self.title_input.clear()
        self.description_input.clear()
        self.priority_input.clear()
        self.deadline_input.clear()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec_())

       
