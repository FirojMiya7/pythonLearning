# Project 3: Word Counter
"""
Requirements:

Read text from file
Count each word frequency
Print output like:
python : 3
code   : 5
"""


# Word Counter Project
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def clean_text(text):
    text = text.lower()
    for ch in ",.!?;:\"'()":            # Punctuation haru lai text bata remove garne
        text = text.replace(ch, "")
    return text

def count_words(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def print_results(word_count):
    for word, count in word_count.items():
        print(f"{word} : {count}")

# Main execution
text = read_file("PracticeProblem/MiniProjects/WordCounter/text.txt")
text = clean_text(text)
words = text.split()
word_count = count_words(words)
print_results(word_count)
    
# Print garda for word , count in word_count.items() use gareko cuz word_count is a dictionary ho and items() method le key ra value return garcha. Tesaile word ma key (word) rakhne ra count ma value (frequency) rakhne.
# Output print garda f-string use gareko ho, jasma {word} ra {count} le respective word ra usko frequency print garne.
