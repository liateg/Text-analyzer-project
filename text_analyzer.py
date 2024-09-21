# Importing all necessary libraries
import pandas as pd  # For data manipulation and analysis
import os  # For interacting with the operating system
import re  # For regular expressions
import nltk  # For natural language processing tasks

# Downloading necessary NLTK data
nltk.download('punkt')  # Tokenizer models
#nltk.download('wordnet')  # WordNet lexical database
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
        return pd.read_fwf(os.path.abspath(file_path))
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

#Write Geeze charachters
def Title_write(text):
    op=open('Output.doc',mode='a')
    op.write(text)
    op.close()
    
    
def list_Geez_write(token):
    with open ('Output.doc', encoding='utf-8', mode='a') as report_file:
       
        for word in token:
            report_file.write(f'{word} ')

def dect_Geez_write(counter):
 
    with open ('Output.doc', encoding='utf-8', mode='a') as report_file:
        for key,value in counter.items() :

            report_file.write(f'{key}:{value} ')

def overllaping_calc(counter1,counter2):

    overllaped_phonem=set.intersection(set(counter2),set(counter1))
    Union=set.union(set(counter1),set(counter2))

    return (len(overllaped_phonem)/len(Union))*100  

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

# Count word frequency
acounter = count_frequency(dfa_t)
tcounter = count_frequency(dft_t)

# Get unique words
aunique_word = get_unique_words(acounter)
tunique_word = get_unique_words(tcounter)

# Extract alphabets
aalphabet = extract_alphabets(acounter)
talphabet = extract_alphabets(tcounter)

# Count alphabet frequency
aalphabet_counter = count_alphabet_frequency(aalphabet)
talphabet_counter = count_alphabet_frequency(talphabet)

#Clculate word and alphabet level overlap
# Find overlapping words
overlapped_word =get_overlapping_words(acounter, tcounter)

#Find overlapping Alphabets
overlapped_alphabet= get_overlapping_words(talphabet_counter, aalphabet_counter)

# Converting Ethiopic alphabets into their phonetic representations
aipa_converted_alphabet = ipa_convertor_alpahbet(aalphabet)  # alphabet level
tipa_converted_alphabet = ipa_convertor_alpahbet(talphabet)

aipa_converted_df = ipa_convert(dfa_t)  # Text level
tipa_converted_df = ipa_convert(dft_t)
# Print the cleaned data
op=open('Output.doc','w')
op.write('This is all the output of the code\n')
op.close()
         

Title_write('The preprocessed Amharic text:\n')
list_Geez_write(dfa_t)

Title_write('The preprocessed Tigregna text:\n')
list_Geez_write(dft_t)

Title_write('The word frequency in the given Tigrigna and Amharic text is shown below\nTigregna\n')
dect_Geez_write(tcounter)
Title_write('Amharic')
dect_Geez_write(acounter)
Title_write('Unique words for the given Tigrigna text are\n')
Title_write('Total number of unique words in the Tigrigna text:  ')
Title_write(str(len(tunique_word)))
list_Geez_write(tunique_word)
Title_write('Unique words for the given Amharic text are\n')
Title_write('Total number of unique words in the Amharic text:  ')
Title_write(str(len(aunique_word)))
list_Geez_write(aunique_word)

Title_write('Alphabetical frequency in the given Amharic text: \n')
dect_Geez_write(aalphabet_counter)
Title_write('Alphabetical frequency in the given Tigregna text: \n')
dect_Geez_write(talphabet_counter)
Title_write('The number of words that are in both Amharic and Tigrigna texts are: ')
Title_write(str(len(overlapped_word)))
Title_write('Here are the words\n')
list_Geez_write(overlapped_word)
Title_write('The number of alphabets that are in both Amharic and Tigrigna texts are: ')
Title_write(str(len(overlapped_alphabet)))
Title_write('Here are the words\n')
list_Geez_write(overlapped_alphabet)

# #Print the  phoneme of the given text
Title_write('\nThe phoenem of the given Amharic text\n')
aipa_converted_alphabet_single=[]
for word in aipa_converted_df:
    op=open('Output.doc',encoding='utf-8',mode='a')
    op.write(word)
    for char in word:
        aipa_converted_alphabet_single.append(char)

Title_write('\nThe phoenem of the given Tigregna text\n')
tipa_converted_alphabet_single=[]
for word in tipa_converted_df:
    op=open('Output.doc',encoding='utf-8',mode='a')
    op.write(word)
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
#print()
Title_write('\n\nAlphabetical  phoneme frequency in the given Amharic text: \n') 
dect_Geez_write(aipa_converted_alphabet_counter)

Title_write('\n\nAlphabetical  phoneme frequency in the given Tigregna text: \n') 
dect_Geez_write(tipa_converted_alphabet_counter)
#print(f'Alphabetical  phoneme frequency in the given Tigrigna text: \n \n{tipa_converted_alphabet_counter}\n')

aipa_converted_single_alphabet_counter = count_alphabet_frequency(aipa_converted_alphabet_single)
tipa_converted_single_alphabet_counter = count_alphabet_frequency(tipa_converted_alphabet_single)

#print(f'Single phoneme  frequency in the given Amharic text: \n\n{aipa_converted_single_alphabet_counter}\n')
Title_write('\n\nSingle phoneme  frequency in the given Amharic text: \n')
dect_Geez_write(aipa_converted_single_alphabet_counter)
#print(f'Single phoneme  frequency in the given Tigrigna text: \n\n{tipa_converted_single_alphabet_counter}')
Title_write('\n\nSingle phoneme  frequency in the given Tigregna text: \n')
dect_Geez_write(tipa_converted_single_alphabet_counter)
#Phonetic overllaping analysis-character level 

#Phonetic overllaping analysis-phonem level 
single_phonem_overllaped=set.intersection(set(aipa_converted_single_alphabet_counter),set(tipa_converted_single_alphabet_counter))
vowels={'a','e','o','ə', 'u','i', 'ɨ','ɒ','ʌ','æ','ɔ','ɜ'}
single_phonem_overllaped.difference_update(vowels)  #Remove Vowels-> short vowels: /ɪ/ /ʊ/ /ə/ /e/ /ɒ/ /ʌ/ /æ/ 5 long vowels: /iː/ /uː/ /ɑː/ /ɔː/ /ɜː/
Union=set.union(set(tipa_converted_single_alphabet_counter),set(aipa_converted_single_alphabet_counter))
Union.difference_update(vowels)
single_phonem_overllaped_phonem=len(single_phonem_overllaped)/len(Union)*100

#Analysis
Title_write(f'\n\nAnalysis\nWord level overlaping in percentache is: {overllaping_calc(acounter, tcounter)}%\nCharacter level overlaping in percentache is: {overllaping_calc(aalphabet, talphabet)}%\nCombined Phonem level overlap in percentage is: {overllaping_calc(tipa_converted_alphabet_counter, aipa_converted_alphabet_counter)}%\n Phonem level overlap is: {single_phonem_overllaped_phonem}%\n--------END------------')



