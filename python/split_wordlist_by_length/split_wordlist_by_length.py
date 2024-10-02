import os

# Takes the given wordlist and outputs individual lists by given length

def separate_words_by_length(words):
    length_dict = {}
    for word in words:
        word_length = len(word)
        if word_length not in length_dict:
            length_dict[word_length] = []
        length_dict[word_length].append(word.capitalize())  # Export as capital
        # length_dict[word_length].append(word)  # Export as inputted
    return length_dict

def export_to_files(length_dict, output_path):
    for length, word_list in length_dict.items():
        filename = os.path.join(output_path, f'length_{length}.txt')
        with open(filename, 'w') as file:
            file.write('\n'.join(word_list))
        print(f"Exported words of length {length} to {filename}")

def load_words(source_path):
    with open(source_path) as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

if __name__ == '__main__':
    source_path = os.path.join('.', 'wordlist.txt')
    output_path = os.path.join('.', 'Output')

    # Ensure the output directory exists
    os.makedirs(output_path, exist_ok=True)

    english_words = load_words(source_path)
    length_dict = separate_words_by_length(english_words)
    export_to_files(length_dict, output_path)
