STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
punc = "\!()-[]{};:',<>./?@#$%^&*_~" + '"'
wordCount = {}
badWords = {}


# opens and reads provided file
def open_and_read_file(file):
    with open(file, 'r') as reader:
        file1 = reader.read()
    return file1


# fucntion removes all punctuation from file if it is in string punc. returns file1 without punctuation
def removePunctation(file1):
    for line in file1:
        for word in line.split():
            if word in punc:
                file1 = file1.replace(word, "")
    return file1        


# counts each word in the file and sorts good words from stop words. returns dictionary of good word counts
def count_words(file1):
    for word in file1.split():
        word = word.lower()
        if word in STOP_WORDS:
            if word in badWords:
                badWords[word] += '*'
            else:
                badWords[word] = '*'
        else:
            if word in wordCount:
                wordCount[word] += '*'
            else:
                wordCount[word] = '*'
    return wordCount


# calls all functions. prints the final word count for each good word
def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""    
    file1 = open_and_read_file(file)
    file1 = removePunctation(file1)
    wordCount = count_words(file1)

    for key, value in wordCount.items():
        print(key, ':', value)


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
