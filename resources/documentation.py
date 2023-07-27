```python
class Documentation:
    def __init__(self):
        self.documentation = {
            "Python": "https://docs.python.org/3/",
            "JavaScript": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
            "Java": "https://docs.oracle.com/javase/tutorial/",
            "C++": "http://www.cplusplus.com/doc/tutorial/",
            "C#": "https://docs.microsoft.com/en-us/dotnet/csharp/",
            "Ruby": "https://ruby-doc.org/",
            "Swift": "https://docs.swift.org/swift-book/",
            "Kotlin": "https://kotlinlang.org/docs/home.html",
            "Go": "https://golang.org/doc/",
            "Rust": "https://doc.rust-lang.org/book/",
            "TypeScript": "https://www.typescriptlang.org/docs/",
        }

    def get_documentation_link(self, language):
        return self.documentation.get(language, "Language not supported")

documentation = Documentation()
```