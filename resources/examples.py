```python
# resources/examples.py

class Examples:
    def __init__(self):
        self.examples = {
            'python': {
                'Hello World': 'print("Hello, World!")',
                'For Loop': 'for i in range(10):\n\tprint(i)',
                'If Statement': 'if 10 > 5:\n\tprint("10 is greater than 5")',
            },
            'javascript': {
                'Hello World': 'console.log("Hello, World!");',
                'For Loop': 'for (let i = 0; i < 10; i++) {\n\tconsole.log(i);\n}',
                'If Statement': 'if (10 > 5) {\n\tconsole.log("10 is greater than 5");\n}',
            },
            # Add more languages and examples as needed
        }

    def get_examples(self, language):
        return self.examples.get(language, {})

    def get_example(self, language, example_name):
        return self.examples.get(language, {}).get(example_name, "Example not found")
```