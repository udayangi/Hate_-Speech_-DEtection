import re

def read_hate_words_from_files(file_paths):
    hate_words = []
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as hate_words_file:
                hate_words.extend([line.strip() for line in hate_words_file.readlines()])
        except FileNotFoundError:
            print(f"Warning: Hate words file '{file_path}' not found.")

    return hate_words

def find_hate_text(text, hate_words):
    found_hate_words = []

    for keyword in hate_words:
        if re.search(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE):
            found_hate_words.append(keyword)

    return found_hate_words

try:
    with open("ConvertText.txt", 'r') as file:
        transcript_text = file.read()

    hate_word_files = ["HateWords1.txt", "HateWords2.txt", "HateWords3.txt"]  # Add more file names as needed
    hate_words = read_hate_words_from_files(hate_word_files)

    found_hate_words = find_hate_text(transcript_text, hate_words)

    if found_hate_words:
        with open("HateResults.txt", 'w') as result_file:
            result_file.write("Potentially hateful content found in the transcript. Hate words:\n")
            for word in found_hate_words:
                result_file.write(f"- {word}\n")
    else:
        with open("HateResults.txt", 'w') as result_file:
            result_file.write("No potentially hateful content found in the transcript.")
except FileNotFoundError:
    print("Error: 'ConvertText.txt' or hate words file(s) not found.")
except Exception as e:
    print(f"An error occurred: {e}")