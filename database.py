import task
import category

class Database:
    """Mock database with task and categories.
    Need to make a actual database and API."""

    def __init__(self):
        """Initialize a new database."""
        self.num_tasks = 0
        self.num_categories = 0
        self.tasks = []
        self.categories = []
        self.in_progress = []
        self.finished = []

    def add_task(self, name):
        """Add a task to the database."""
        code = self.num_tasks
        self.num_tasks += 1
        new_task = task.setup(name, code)
        self.tasks.append(new_task)
        self.in_progress.append(code)

    def remove_task(self, code):
        """Remove a task from the database."""
        pass

    def start_task(self, code):
        """Start the timer on a task."""
        pass

    def stop_task(self, code):
        """Stop the timer on a task."""
        pass

    def finish_task(self, code):
        """Move a task from 'in_progress' to 'finished'."""
        pass

    def add_category(self, name):
        """Add a category to the database."""
        pass

    def remove_category(self, code):
        """Remove a category from the database."""

def setup():
    """Set up a mock database."""
    return Database()
