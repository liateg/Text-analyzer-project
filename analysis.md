# Final Analysis
The TextAnalyzer project successfully processes and analyzes Amharic and Tigrigna texts through various stages, including data loading, cleaning, tokenization, stopword removal, and grapheme-to-phoneme conversion. The key findings and outputs from the analysis are as follows:


## Data Loading
The text data is loaded from fixed-width formatted files, ensuring that the data is accurately read into a structured format for further processing.
## Data Cleaning
The text data is cleaned by removing all non-word characters, leaving only spaces and word characters. This step ensures that the text is in a consistent format for analysis.
## Tokenization
The cleaned text is tokenized into individual words, allowing for detailed analysis of word usage and frequency.
## Stopword Removal
Custom stopwords for Amharic and Tigrigna are successfully removed from the tokenized data, focusing the analysis on meaningful words.
## Word Frequency Analysis
The frequency of each word is counted, providing insights into the most commonly used words in the text. Unique words (words that appear only once) are identified, highlighting rare or specific terms.
## Overlapping Words
The analysis identifies overlapping words between two datasets, revealing common terms used across different texts.
## Alphabet Extraction
Individual alphabets are extracted from the words, allowing for phonetic analysis and further linguistic studies.
## Grapheme-to-Phoneme Conversion
The project converts graphemes to phonemes using the International Phonetic Alphabet (IPA), providing a phonetic representation of the text. This step is crucial for linguistic analysis and pronunciation studies.
Overall, the TextAnalyzer project provides a comprehensive toolkit for analyzing Amharic and Tigrigna texts, offering valuable insights into word usage, frequency, and phonetic representation. The project can be further extended to include additional languages and more advanced text analysis techniques.


# Numerical Analysis

This section presents the quantitative findings from the text analysis:

## Word Frequency Analysis
- **Total number of words in the analyzed amharic text is**: `1916`
- **Total number of words in the analyzed tigregna text is**: `2044`

- **Unique Words**: The total number of unique words (words that appear only once) in Amharic.txt is: `637`
- **Unique Words**: The total number of unique words (words that appear only once) in Tegrigna.txt is: `659`

## Overlapping Words
- **Common Words**: The number of overlapping words between the Amharic and Tigrigna datasets is: `74`, `3.6399409739301523%`
- The overlapped words can be seen in the `Output.doc` in this repository.
  
## Overlapping Alphabet
- **Common Alphabet**: The number of overlapping alphabet between the Amharic and Tigrigna datasets is: `143`,`65.29680365296804%`
- The overlapped alphabet can be seen in the `Output.doc` in this repository.
## Phonem level analysis
- **Combined Phonem(character)** overlap in percentage is: `75.52083333333334%`
- **Phonem(character)** overlap in percentage is: `100.0%` ,this is because both langueage use same characters with subtle difference


 
