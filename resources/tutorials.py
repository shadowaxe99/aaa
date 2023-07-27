```python
class Tutorial:
    def __init__(self, title, content, language):
        self.title = title
        self.content = content
        self.language = language

tutorials = [
    Tutorial("Python Basics", "This tutorial covers the basics of Python programming...", "Python"),
    Tutorial("JavaScript for Beginners", "This tutorial introduces the fundamentals of JavaScript...", "JavaScript"),
    Tutorial("Introduction to Java", "This tutorial is a comprehensive guide to Java programming...", "Java"),
    # Add more tutorials as needed
]

def get_tutorials(language=None):
    if language:
        return [tutorial for tutorial in tutorials if tutorial.language == language]
    return tutorials

def get_tutorial(title):
    for tutorial in tutorials:
        if tutorial.title == title:
            return tutorial
    return None
```