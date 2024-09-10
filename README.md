# Tamil Wikipedia Word Frequency Analyzer

## Download Tamil Wikipedia Dump

* Get the Tamil Wikipedia dump from the following url ~[http://dumps.wikimedia.org/tawiki/latest/](http://dumps.wikimedia.org/tawiki/latest/)~
* You will download a file named  tawiki-latest-pages-articles.xml.bz2
* Extract it using the following command:

`bunzip2 tawiki-latest-pages-articles.xml.tar.bz2`


This project consists of a Bash script (`line.sh`) and a Python script (`tamil.py`) that work together to process a text file, extract Tamil words, and analyze their frequency.

## Files

- `line.sh`: Bash script for initial text processing and word extraction
- `tamil.py`: Python script for Tamil word identification, sorting, and frequency analysis
- Input text file (user-provided)

## Prerequisites

- Bash shell
- Python 3.x
- The following Python modules (all part of the standard library):
  - `collections`
  - `csv`

## Usage

1. Run the Bash script to process the input file and create a list of words:

   ```
   bash line.sh
   ```
   
   You will be prompted to enter the filename of your input text file. Enter the file name you downloaded and extracted from Tamil Wikipedia dump.

2. After the Bash script completes, run the Python script:

   ```
   python3 tamil.py
   ```

## Input

- You will be prompted to enter the filename of your input text file. Enter the file name you downloaded and extracted from Tamil Wikipedia dump. You can also use this project to process any word file with Tamil content provided you input the corresponding .txt file name.

## Output

The Python script generates several output files:

1. `tamil-words.txt`: Contains all Tamil words extracted from the input file
2. `only_uniq_tamil_words.txt`: Contains unique Tamil words
3. `only_tamil_uniq_sorted_words.txt`: Contains unique Tamil words sorted alphabetically
4. `tamil_words_by_frequency.csv`: A CSV file with Tamil words sorted by frequency (descending order)

## Functionality

### line.sh

This Bash script does the following:
- Prompts the user for an input filename
- Checks if the file exists
- Processes the file by:
  - Removing English characters
  - Replacing various punctuation and special characters with newlines
  - Removing leading/trailing whitespace
  - Removing empty lines
- Outputs the processed words to a file named `words`

### tamil.py

This Python script performs the following operations:
- Defines a function `is_tamil()` to identify Tamil words based on Unicode character ranges
- Reads the `words` file created by `line.sh`
- Filters out non-Tamil words
- Generates various output files as described in the Output section
- Counts word frequencies and sorts words by frequency
- Provides console output about the number of unique words and the files created

## Notes

- The scripts assume UTF-8 encoding for input and output files
- Error handling is implemented for file operations
- The Tamil word identification is based on the Unicode range 2944-3071

## Contributing

Feel free to fork this project and submit pull requests with any enhancements.

## License

The license for the code is GPL V3.