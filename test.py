import database

def main():
    """Test the approximate library."""
    my_db = database.setup()
    my_db.add_task("Hello World!")
    my_db.add_task("This is a test for approximate.")
    my_db.add_task("There is still alot to do.")
    my_db.add_task("But each day we will make more progress.")

    print("tasks", my_db.tasks)
    print("in_progress", my_db.in_progress)
    print("finished", my_db.finished)


if __name__ == '__main__':
    main()
