import category
import database


class Task:
    """Hold information about a category."""

    def __init__(self, name, code):
        """Initialize a new task."""
        self.id = {"name": name, "code": code}
        self.desc = ""
        self.categories = []
        self.actual_time = None
        self.approx_time = None

    def add_category(self, name):
        """Add a category to a task."""
        category.setup(name)


def setup(name, code):
    """Set up a tasks"""
    return Task(name, code)
