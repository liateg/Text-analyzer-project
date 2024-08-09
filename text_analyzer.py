# Importing all necessary libraries
import pandas as pd  # For data manipulation and analysis
import os  # For interacting with the operating system
import re  # For regular expressions
import nltk  # For natural language processing tasks

# Downloading necessary NLTK data
nltk.download('punkt')  # Tokenizer models
nltk.download('wordnet')  # WordNet lexical database
nltk.download("stopwords")  # Stopwords list

# Importing specific functions from NLTK
from nltk.tokenize import word_tokenize  # For tokenizing words
from nltk.corpus import stopwords  # For accessing stopwords

# Importing custom functions from IPA_dict&unction module
from IPA_dict_function import *

"""
In order to differentiate the two texts, we use 'a' for Amharic text manipulation and
't' for Tigrigna text manipulations. So any similar variable or object name will have 
a difference in these two alphabets.
"""

def load_data(file_path):
    """
    Load data from a fixed-width formatted file.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    DataFrame: The loaded data.
    """
    try:
        return pd.read_fwf(file_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please check the file path and ensure the file exists.")
        exit()

def clean_data(df, column_name):
    """
    Clean the data by removing everything except for spaces and word characters.
    
    Parameters:
    df (DataFrame): The data frame containing the text data.
    column_name (str): The name of the column to clean.
    
    Returns:
    DataFrame: The cleaned data frame.
    """
    for i in range(len(df.axes[0])):
        df.loc[i, column_name] = re.sub(r'[^\w\s]', '', df[column_name][i])
    return df

def tokenize_data(df, column_name):
    """
    Tokenize the cleaned text data.
    
    Parameters:
    df (DataFrame): The data frame containing the text data.
    column_name (str): The name of the column to tokenize.
    
    Returns:
    list: The tokenized words.
    """
    tokens = []
    for i in range(len(df.axes[0])):
        tokens += nltk.word_tokenize(df[column_name][i])
    return tokens

def remove_stopwords(tokens, language):
    """
    Remove stopwords from the tokenized data.
    
    Parameters:
    tokens (list): The list of tokenized words.
    language (str): The language of the stopwords to remove.
    
    Returns:
    list: The list of words without stopwords.
    """
    try:
        stop_words = stopwords.words(language)
    except OSError:
        print(f"Error: The stopwords for the language '{language}' were not found. The stop words can't be removed.")
        print("Please add the stopwords file for this language to the NLTK data path.")
        return tokens  # Return the original tokens if stopwords are not found
    
    return [word for word in tokens if word not in stopwords.words(language)]


def count_frequency(tokens):
    """
    Count the frequency of each word in the tokenized data.
    
    Parameters:
    tokens (list): The list of tokenized words.
    
    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    """
    counter = {}
    for word in tokens:
        if word not in counter:
            counter[word] = tokens.count(word)
    return counter

def get_unique_words(counter):
    """
    Get all unique words (words that appear only once).
    
    Parameters:
    counter (dict): A dictionary with words as keys and their frequencies as values.
    
    Returns:
    list: A list of unique words.
    """
    return [word for word in counter.keys() if counter[word] == 1]

def get_overlapping_words(counter1, counter2):
    """
    Find overlapping words between two datasets.
    
    Parameters:
    counter1 (dict): The first word frequency dictionary.
    counter2 (dict): The second word frequency dictionary.
    
    Returns:
    list: A list of overlapping words.
    """
    return [word for word in counter1.keys() if word in counter2.keys()]

def extract_alphabets(counter):
    """
    Extract each alphabet separately from the words.
    
    Parameters:
    counter (dict): A dictionary with words as keys and their frequencies as values.
    
    Returns:
    list: A list of alphabets.
    """
    return [char for word in counter.keys() for char in word]

def count_alphabet_frequency(alphabets):
    """
    Count the frequency of each alphabet.
    
    Parameters:
    alphabets (list): A list of alphabets.
    
    Returns:
    dict: A dictionary with alphabets as keys and their frequencies as values.
    """
    counter = {}
    for char in alphabets:
        if char not in counter:
            counter[char] = alphabets.count(char)
    return counter

# Load the data
dfa = load_data('C:\\Users\\Liya\\Desktop\\5k\\Project\\Amharic.txt')
dft = load_data('C:\\Users\\Liya\\Desktop\\5k\\Project\\Tegrigna.txt')

# Clean the data
dfa = clean_data(dfa, "Amharic")
dft = clean_data(dft, "Tigregna")

# Tokenize the data
dfa_t = tokenize_data(dfa, "Amharic")
dft_t = tokenize_data(dft, "Tigregna")

# Remove stopwords
dfa_t = remove_stopwords(dfa_t, 'amharic')
dft_t = remove_stopwords(dft_t, 'tigregna')

# Print the cleaned data

print(f'The preprocessed Amharic text: \n\n {dfa_t}\n')
print(f'The preprocessed Tigrigna text: \n\n {dft_t}\n')

# Count word frequency
acounter = count_frequency(dfa_t)
tcounter = count_frequency(dft_t)

# Print word frequency
print(f'The word frequency in the given Tigrigna and Amharic text is shown below \n Tigrigna \n\n{tcounter}')
print('Amharic \n\n',acounter)

# Get unique words
aunique_word = get_unique_words(acounter)
tunique_word = get_unique_words(tcounter)

# Print unique words
print(f'Unique words for the given Tigrigna text are\n\n {tunique_word}\n')
print(f'Unique words for the given Amharic text are\n \n{aunique_word}\n')


# Extract alphabets
aalphabet = extract_alphabets(acounter)
talphabet = extract_alphabets(tcounter)

# Count alphabet frequency
aalphabet_counter = count_alphabet_frequency(aalphabet)
talphabet_counter = count_alphabet_frequency(talphabet)

# Print alphabet frequency
print(f'Alphabetical frequency in the given Amharic text: \n\n {aalphabet_counter}\n')
print(f'Alphabetical frequency in the given Tigrigna text: \n\n {talphabet_counter}\n')

#Clculate word and alphabet level overlap
# Find overlapping words
overlapped_word =get_overlapping_words(acounter, tcounter)
# Print overlapping words
print(f'The number of words that are in both Amharic and Tigrigna texts are\n {len(overlapped_word)} \nHere are the words\n\n {overlapped_word}\n')
#Find overlapping Alphabets
overlapped_alphabet= get_overlapping_words(talphabet_counter, aalphabet_counter)
print(f'The number of letters in both Amharic and Tigrigna texts is\n {len(overlapped_alphabet)} \nHere are the letters\n \n{overlapped_alphabet}\n')
# Converting Ethiopic alphabets into their phonetic representations
aipa_converted_alphabet = ipa_convertor_alpahbet(aalphabet)  # alphabet level
tipa_converted_alphabet = ipa_convertor_alpahbet(talphabet)

aipa_converted_df = ipa_convert(dfa_t)  # Text level
tipa_converted_df = ipa_convert(dft_t)

#Print the  phoneme of the given text
print(f'The phoenem of the given Amharic text\n')
aipa_converted_alphabet_single=[]
for word in aipa_converted_df:
    print(word,'',end='')
    for char in word:
        aipa_converted_alphabet_single.append(char)
print()

print(f'The phoenem of the given Tigregna text\n')

tipa_converted_alphabet_single=[]
for word in tipa_converted_df:
    print(word,'',end='')
    for char in word:
        tipa_converted_alphabet_single.append(char)

   
# Counting the frequency of each phonetic character
aipa_converted_alphabet_counter = {}
for char in aipa_converted_alphabet:
    if char not in aipa_converted_alphabet_counter:
        aipa_converted_alphabet_counter[char] = aipa_converted_alphabet.count(char)

tipa_converted_alphabet_counter = {}
for char in tipa_converted_alphabet:
    if char not in tipa_converted_alphabet_counter:
        tipa_converted_alphabet_counter[char] = tipa_converted_alphabet.count(char)

#Print the alphabet  phoneme frequancy
print()
print(f'Alphabetical  phoneme frequency in the given Amharic text: \n\n {aipa_converted_alphabet_counter}\n')
print(f'Alphabetical  phoneme  frequency in the given Tigrigna text: \n \n{tipa_converted_alphabet_counter}\n')


aipa_converted_single_alphabet_counter = count_alphabet_frequency(aipa_converted_alphabet_single)

tipa_converted_single_alphabet_counter = count_alphabet_frequency(tipa_converted_alphabet_single)

print(f'Single phoneme  frequency in the given Amharic text: \n\n{aipa_converted_single_alphabet_counter}\n')
print(f'Single phoneme  frequency in the given Tigrigna text: \n\n{tipa_converted_single_alphabet_counter}')
