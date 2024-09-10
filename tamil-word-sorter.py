# Import the Counter class from the collections module and the csv module
from collections import Counter
import csv

# Define the input and output file names
input_file = 'words'
output_file = 'tamil-words.txt'
unique_output_file = 'only_uniq_tamil_words.txt'
sorted_output_file = 'only_tamil_uniq_sorted_words.txt'
frequency_output_file = 'tamil_words_by_frequency.csv'

# Define a function to check if a word is in Tamil
def is_tamil(word):
    try:
        # Check the Unicode value of the first character of the word
        first_char = word[0]
        lang_number = ord(first_char)
        return 2944 <= lang_number <= 3071
    except (IndexError, TypeError):
        return False

# Open the input and output files for reading and writing, respectively
try:
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        # Read the input file line by line
        for line in infile:
            # Check if the line is a Tamil word
            if is_tamil(line):
                # Write the line to the output file
                outfile.write(line)
except FileNotFoundError:
    print(f"Error: The input file '{input_file}' does not exist.")
except IOError:
    print(f"Error: Could not open the input file '{input_file}' for reading.")

# Print a message to inform the user that the words are being analyzed
print("Analyzing words...")

# Open the output and unique output files for reading and writing, respectively
try:
    with open(output_file, 'r', encoding='utf-8') as outfile, open(unique_output_file, 'w', encoding='utf-8') as uniq_outfile:
        # Use a set to store the unique words
        unique_words = set()
        # Read the output file line by line
        for line in outfile:
            # Remove any leading or trailing whitespace from the line
            word = line.strip()
            # Add the word to the set of unique words
            unique_words.add(word)
        # Write each unique word to the unique output file, followed by a newline character
        for word in unique_words:
            uniq_outfile.write(word + "\n")
except FileNotFoundError:
    print(f"Error: The output file '{output_file}' does not exist.")
except IOError:
    print(f"Error: Could not open the output file '{output_file}' for reading.")

# Open the unique output and sorted output files for reading and writing, respectively
try:
    with open(unique_output_file, 'r', encoding='utf-8') as uniq_outfile, open(sorted_output_file, 'w', encoding='utf-8') as sorted_outfile:
        # Read all the unique words from the unique output file
        unique_words = uniq_outfile.readlines()
        # Sort the unique words
        unique_words.sort()
        # Write each sorted unique word to the sorted output file, followed by a newline character
        for word in unique_words:
            sorted_outfile.write(word)
        # Display the number of unique words in the file
        print(f"Number of unique words: {len(unique_words)}")
except FileNotFoundError:
    print(f"Error: The unique output file '{unique_output_file}' does not exist.")
except IOError:
    print(f"Error: Could not open the unique output file '{unique_output_file}' for reading.")

# Open the output and frequency output files for reading and writing, respectively
try:
    with open(output_file, 'r', encoding='utf-8') as outfile, open(frequency_output_file, 'w', newline='', encoding='utf-8') as freq_outfile:
        # Use a Counter object to count the frequency of each word
        word_counts = Counter(outfile.read().splitlines())
        # Sort the words by frequency in descending order
        sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        # Create a CSV writer object
        writer = csv.writer(freq_outfile)
        # Write the header row
        writer.writerow(['Word', 'Count'])
        # Write each word and its frequency to the frequency output file
        for word, count in sorted_words:
            writer.writerow([word, count])
except FileNotFoundError:
    print(f"Error: The output file '{output_file}' does not exist.")
except IOError:
    print(f"Error: Could not open the output file '{output_file}' for reading.")

# Print a message to inform the users about the output files created
print("The following output files have been created:")
print(f"- {output_file}: Contains all the Tamil words from the input file.")
print(f"- {unique_output_file}: Contains the unique Tamil words from the input file.")
print(f"- {sorted_output_file}: Contains the unique Tamil words from the input file, sorted in alphabetical order.")
print(f"- {frequency_output_file}: Contains the Tamil words from the input file, sorted by frequency in descending order, as a CSV file.")
