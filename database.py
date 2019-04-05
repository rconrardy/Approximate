import task
import category

class Database:
    """Mock database with task and categories.
    Need to make a actual database and API."""

    def __init__(self):
        """Initialize a new database."""
        self.num_tasks = 0
        self.num_categories = 0
        self.tasks = {}
        self.categories = {}
        self.in_progress = []
        self.finished = []

    def add_task(self, name):
        """Add a task to the database."""
        code = self.num_tasks
        self.num_tasks += 1
        self.tasks[code] = task.setup(name, code)
        self.in_progress.append(code)

    def remove_task(self, code):
        """Remove a task from the database."""
        if code in self.tasks:
            del self.tasks[code]
        if code in self.in_progress:
            self.in_progress.remove(code)
        if code in self.finished:
            self.finished.remove(code)

    def start_task(self, code):
        """Start the timer on a task."""
        pass

    def stop_task(self, code):
        """Stop the timer on a task."""
        pass

    def finish_task(self, code):
        """Move a task from 'in_progress' to 'finished'."""
        if code in self.in_progress:
            self.in_progress.remove(code)
            self.finished.append(code)

    def add_category(self, name):
        """Add a category to the database."""
        code = self.num_categories
        self.num_categories += 1
        self.categories[code] = category.setup(name, code)

    def assign_category(self, category_code, task_code):
        """Assign a category to a task."""
        if category_code in self.categories and task_code in self.tasks:
            if category_code not in self.tasks[task_code].categories:
                self.tasks[task_code].categories.append(category_code)

    def remove_category(self, code):
        """Remove a category from the database."""
        if code in self.categories:
            del self.categories[code]

def setup():
    """Set up a mock database."""
    return Database()
