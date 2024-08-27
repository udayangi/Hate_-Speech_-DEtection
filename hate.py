import re

def find_hate_text(text):
    hate_keywords = {
        'racial': ['a', 'we', 'you', 'i'],
        'offensive': ['Name', 'in the', 'sky'],
        'threat': ['Live','without', 'me']
    }

    found_hate_words = {category: [] for category in hate_keywords}

    for category, keywords in hate_keywords.items():
        for keyword in keywords:
            if re.search(rf'\b{re.escape(keyword)}\b', text, re.IGNORECASE):
                found_hate_words[category].append(keyword)

    return found_hate_words

try:
    with open("ConvertText.txt", 'r') as file:
        transcript_text = file.read()

    found_hate_words = find_hate_text(transcript_text)

    with open("HateResults.txt", 'w') as result_file:
        if any(found_hate_words.values()):
            result_file.write("Potentially hateful content found in the transcript. Hate words:\n")
            for category, words in found_hate_words.items():
                if words:
                    result_file.write(f"{category.capitalize()}:\n")
                    for word in words:
                        result_file.write(f"- {word}\n")
        else:
            result_file.write("No potentially hateful content found in the transcript.")

except FileNotFoundError:
    print("Error: 'ConvertText.txt' file not found.")
except Exception as e:
    print(f"An error occurred: {e}")