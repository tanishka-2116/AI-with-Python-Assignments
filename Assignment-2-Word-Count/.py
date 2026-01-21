# Assignment 2: Count word occurrences in a sentence

def count_words(sentence):
    words = sentence.lower().split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

# Example usage
sentence = "hello world hello Python"
print(count_words(sentence))
