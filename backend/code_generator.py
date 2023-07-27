```python
import nlp
from programming_languages import languages

class CodeGenerator:
    def __init__(self):
        self.nlp_processor = nlp.NLPProcessor()

    def generate_code(self, command, language):
        if language not in languages:
            raise ValueError(f"Unsupported language: {language}")

        # Parse the command using NLP
        parsed_command = self.nlp_processor.parse_command(command)

        # Generate code based on the parsed command and the specified language
        code = self._generate_code_from_parsed_command(parsed_command, language)

        return code

    def _generate_code_from_parsed_command(self, parsed_command, language):
        # This method should be implemented based on the specific requirements
        # of the code generation for each supported language.
        # For simplicity, we assume that it's implemented here.
        pass
```