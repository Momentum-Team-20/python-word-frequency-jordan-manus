import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
wordCount = {}
badWords = {}


# opens and reads provided file
def open_and_read_file(file):
    with open(file, 'r') as reader:
        file1 = reader.read()
    return file1


# fucntion removes all punctuation from file if it is in string punc. returns file1 without punctuation
def remove_punctation(file1):
    for line in file1:
        for word in line.split():
            if word in string.punctuation:
                file1 = file1.replace(word, "")
    return file1        


# def addWhiteSpace(wordCount):
#     for word in wordCount:
#         print(word)

# counts each word in the file and sorts good words from stop words. returns dictionary of good word counts
def count_words(file1):
    for word in file1.split():
        word = word.lower()
        if word in STOP_WORDS:
            if word in badWords:
                badWords[word] += 1
            else:
                badWords[word] = 1
        else:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount[word] = 1
    return wordCount


# calls all functions. prints the final word count for each good word
def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""    
    file1 = open_and_read_file(file)
    file1 = remove_punctation(file1)
    wordCount = count_words(file1)

    sortedWordCount = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)
    wordCount = dict(sortedWordCount)

    for key, value in wordCount.items():
        print(f'{key:>15s} | {value} {value * '*'}')


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)


#  print(f'{word:>15s}', f'| {count}', count * '*')