import database

def main():
    """Test the approximate library."""
    my_db = database.setup()
    my_db.add_task("Task 0")
    my_db.add_task("Task 1")
    my_db.add_task("Task 2")
    my_db.add_task("Task 3")
    my_db.add_task("Task 4")
    my_db.add_task("Task 5")
    my_db.add_task("Task 6")
    my_db.add_task("Task 7")
    my_db.remove_task(2)
    my_db.finish_task(3)
    my_db.finish_task(1)
    my_db.add_category("Memo")
    my_db.add_category("Email")
    my_db.assign_category(0, 1)
    my_db.assign_category(1, 1)
    my_db.assign_category(1, 3)
    for code, task in my_db.tasks.items():
        print(task.id["name"])
        print("\tcode:", task.id["code"])
        print("\tcategories:", task.categories)
        for category in task.categories:
            print("\t\t", my_db.categories[category].id["name"])

    print()
    print("Tasks in progress:", my_db.in_progress)
    print("Tasks finished:", my_db.finished)


if __name__ == '__main__':
    main()
