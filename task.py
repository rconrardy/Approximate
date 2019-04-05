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


def setup(name, code):
    """Set up a task"""
    return Task(name, code)
