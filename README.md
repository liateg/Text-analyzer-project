# Text-analyzer-project

## Project Overview
TextAnalyzer is a Python project designed to manipulate text and analyze Amharic and Tigrigna texts. It includes functionalities for loading data, cleaning text, tokenizing, removing stopwords, counting word frequencies, extracting unique and overlapping words, and converting graphemes to phonemes using IPA (International Phonetic Alphabet).

## Installation Instructions
To install and set up the project, follow these steps:

### Clone the repository:
```
git clone https://github.com/liateg/Text-analyzer-project.git
cd Text-analyzer-project
```

### Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate 
```
### Install the required libraries:
`pip install pandas nltk`

### Download necessary NLTK data:

```
import nltk
nltk.download('punkt')
nltk.download('stopwords')

```
Add Amharic and Tigrigna stopwords files: NLTK does not natively support Amharic and Tigrigna stopwords. To use these languages, you need to add custom stopword files to the NLTK data path.
Save the Files: `amharic` and `tigregna` in this repository in the` nltk_data/corpora/stopwords` directory. If this directory does not exist, you can create it.

## Usage
### Here’s how you can use the various functions in this project:

### Loading Data
### To load data from a fixed-width formatted file:
```
from text_analyzer import load_data
file_path = 'path/to/your/file.txt'
data = load_data(file_path)
```
### Note: Ensure that the first line of the Amharic text file is “Amharic” and the first line of the Tigrigna text file is “Tigregna”.
## Cleaning Data
### To clean the text data by removing everything except for spaces and word characters:
```
from text_analyzer import clean_data
cleaned_data = clean_data(data, 'column_name')
```
## Tokenizing Data
### To tokenize the cleaned text data:
```
from text_analyzer import tokenize_data
tokens = tokenize_data(cleaned_data, 'column_name')
```
## Removing Stopwords
### To remove stopwords from the tokenized data:
```
from text_analyzer import remove_stopwords
stopwords_file = 'path/to/stopwords.txt'
filtered_tokens = remove_stopwords(tokens, stopwords_file)
```
## Counting Word Frequency
### To count the frequency of each word in the tokenized data:
```
from text_analyzer import count_frequency
word_count = count_frequency(filtered_tokens)
```
## Getting Unique Words
### To get all unique words (words that appear only once):
```
from text_analyzer import get_unique_words

unique_words = get_unique_words(word_count)
```

## Finding Overlapping Words
### To find overlapping words between two datasets:
```
from text_analyzer import get_overlapping_words
overlapping_words = get_overlapping_words(word_count1, word_count2)
```

## Extracting Alphabets
### To extract each alphabet separately from the words:
```
from text_analyzer import extract_alphabets
alphabets = extract_alphabets(word_count)
```
## Dependencies
### This project depends on the following libraries:

* pandas
* nltk
* re
* os
## Recommendation
In future work,we consider extending our analysis to other related languages using multilingual models. Transfer learning from large-scale language models can enhance performance, especially with limited labeled data. Explore named entity recognition (NER) and dialect identification. Phonetic transcription tools can aid in phoneme-level analysis. Collect more labeled data through crowdsourcing. Document best practices, collaborate with linguists, and continually analyze model errors to refine your approach.
## Contributing
### If you would like to contribute to this project, please follow these guidelines:

### Fork the repository.
Create a new branch (`git checkout -b feature-branch`).
### Make your changes.
Commit your changes (`git commit -m 'Add some feature' `).
Push to the branch (`git push origin feature-branch`).
### Open a pull request.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
