import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title):
    if not title.strip():
        print("Ошибка: пустая задача")
        return
    tasks = load_tasks()
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Задача '{title}' добавлена")

def main():
    add_task("Купить молоко")
    tasks = load_tasks()
    print(tasks)

if __name__ == "__main__":
    main()