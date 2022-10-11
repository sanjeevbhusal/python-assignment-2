import time
visited_word = {}

sentence_list = ["Hello World", "Hello Again", "Hello There", "Apple", "Apple and Anaconda"]


def get_sentences(word):
    if word in visited_word:
        print("Already Visited Word. Fetch from database")
        return visited_word[word]

    # simulating a operation that takes a long time
    print("Performing search operation...")
    time.sleep(3)

    sentences = []
    for sentence in sentence_list:
        if word in sentence:
            sentences.append(sentence)

    visited_word[word] = sentences
    return sentences


print(get_sentences("Hello"))
print(get_sentences("Hello"))
print(get_sentences("Apple"))
print(get_sentences("Apple"))