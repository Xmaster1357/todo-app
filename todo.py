import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Загружает задачи из файла с явной UTF-8 кодировкой и обработкой ошибок."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        # Если файл повреждён или не читается, начинаем с пустого списка
        print("Предупреждение: файл задач повреждён. Будет создан новый список.")
        return []

def save_tasks(tasks):
    """Сохраняет задачи в файл с явной UTF-8 кодировкой."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(title):
    if not title.strip():
        print("Ошибка: название задачи не может быть пустым")
        return
    tasks = load_tasks()
    tasks.append({"title": title.strip(), "done": False})
    save_tasks(tasks)
    print(f"Задача '{title}' добавлена")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Список задач пуст.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['title']} [{status}]")

def complete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        print(f"Задача {index} отмечена как выполненная.")
    else:
        print("Неверный номер задачи.")

def delete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"Задача '{removed['title']}' удалена.")
    else:
        print("Неверный номер задачи.")

def main():
    """Интерактивное меню."""
    while True:
        print("\n=== Менеджер задач ===")
        print("1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Отметить задачу выполненной")
        print("4. Удалить задачу")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название задачи: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            idx = input("Введите номер задачи для отметки: ")
            if idx.isdigit():
                complete_task(int(idx))
            else:
                print("Ошибка: введите число.")
        elif choice == "4":
            list_tasks()
            idx = input("Введите номер задачи для удаления: ")
            if idx.isdigit():
                delete_task(int(idx))
            else:
                print("Ошибка: введите число.")
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()