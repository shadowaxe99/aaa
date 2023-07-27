```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class NLPProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def process_command(self, command):
        tokenized_command = word_tokenize(command)
        filtered_command = [word for word in tokenized_command if not word in self.stop_words]
        lemmatized_command = [self.lemmatizer.lemmatize(word) for word in filtered_command]
        return lemmatized_command

nlp_processor = NLPProcessor()
```