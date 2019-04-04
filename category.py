import database

class Category:
    """Hold information about a category."""

    def __init__(self, name):
        """Initialize a new category."""
        self.id = {"name": "", "code": ""}

def setup(name):
    print("NEW CATEGORY:", name)
    return Category(name)
