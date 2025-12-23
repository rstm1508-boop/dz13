import json


class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def __repr__(self):
        status = "Выполнено" if self.is_done else "Не выполнено"
        return f"{self.title} - {status}"


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        try:
            self.load_from_file()
        except FileNotFoundError:
            pass  # Файл отсутствует, создадим пустой список задач

    def add_task(self, title):
        """Добавляем новую задачу"""
        new_task = Task(title)
        self.tasks.append(new_task)
        print(f"Задача '{new_task.title}' добавлена.")

    def mark_task_done(self, title):
        found = None
        for task in self.tasks:
            if task.title.lower() == title.lower():
                found = task
                break

        if found:
            found.mark_done()
            print(f"Задача '{found.title}' отмечена как выполненная.")
        else:
            print("Задача не найдена.")

    def show_tasks(self):
        if len(self.tasks) > 0:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Список задач пуст.")

    def save_to_file(self):
        serialized_data = [
            {
                "title": task.title,
                "is_done": task.is_done
            }
            for task in self.tasks
        ]
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(serialized_data, file, ensure_ascii=False, indent=4)
        print("Данные сохранены.")

    def load_from_file(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            loaded_data = json.load(file)
        self.tasks = [Task(task["title"]) for task in loaded_data]
        for i, task in enumerate(self.tasks):
            task.is_done = loaded_data[i]["is_done"]



def main():
    manager = TaskManager()
    while True:
        command = input("\nВведите команду (add/done/show/exit): ").strip().lower()
        if command == "add":
            title = input("Введите название задачи: ")
            manager.add_task(title)
        elif command == "done":
            title = input("Введите название задачи: ")
            manager.mark_task_done(title)
        elif command == "show":
            manager.show_tasks()
        elif command == "exit":
            manager.save_to_file()
            print("Приложение закрыто.")
            break
        else:
            print("Некорректная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()