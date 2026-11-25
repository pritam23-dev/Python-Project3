import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """আগের save করা tasks file থেকে tasks পড়ে"""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        print("⚠️ tasks.json পড়া যায়নি, নতুন করে শুরু হচ্ছে।")
        return []


def save_tasks(tasks):
    """tasks গুলো file-এ save করে"""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def show_tasks(tasks):
    if not tasks:
        print("📭 কোনো task নেই।")
        return
    print("\n--- আপনার Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")
    print()


def add_task(tasks):
    title = input("Task লেখো: ").strip()
    if not title:
        print("❌ খালি task যোগ করা যাবে না।")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("✅ Task যোগ হয়েছে!")


def get_task_index(tasks, action):
    """user-এর দেওয়া নম্বর নিয়ে list-এর index ফেরত দেয়"""
    if not tasks:
        print("📭 কোনো task নেই।")
        return None
    show_tasks(tasks)
    try:
        number = int(input(f"কোন task টা {action}? নম্বর লেখো: "))
    except ValueError:
        print("❌ সঠিক সংখ্যা লেখো।")
        return None
    if 1 <= number <= len(tasks):
        return number - 1
    print("❌ এই নম্বরের কোনো task নেই।")
    return None


def complete_task(tasks):
    index = get_task_index(tasks, "complete")
    if index is None:
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print("🎉 Task complete হয়েছে!")


def delete_task(tasks):
    index = get_task_index(tasks, "delete")
    if index is None:
        return
    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"🗑️ '{removed['title']}' delete হয়েছে।")


def main():
    tasks = load_tasks()

    while True:
        print("""
=== To-Do List ===
1. Task যোগ করো
2. সব Task দেখো
3. Task complete করো
4. Task delete করো
5. বের হও""")

        choice = input("আপনার choice লেখো (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 আবার দেখা হবে!")
            break
        else:
            print("❌ ১ থেকে ৫ এর মধ্যে একটা সংখ্যা লেখো।")


if __name__ == "__main__":
    main()


