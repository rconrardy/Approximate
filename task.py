class Task:
    """Provides a task with similarity ids (SID)."""

    def __init__(self, name):
        """Initialize a new task"""
        self.name = name


def setup(name):
    return Task(name)
