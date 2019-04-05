import database

class Category:
    """Hold information about a category."""

    def __init__(self, name, code):
        """Initialize a new category."""
        self.id = {"name": name, "code": code}

def setup(name, code):
    """Set up a category"""
    return Category(name, code)
