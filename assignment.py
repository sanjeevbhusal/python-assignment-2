import time
visited_word = {}

sentence_list = ["Hello World", "Hello Again", "Hello There", "Apple", "Anaconda"]


def get_sentences(word):
    if word in visited_word:
        return visited_word[word]

    # simulating a operation that takes a long time
    print("Performing search operation...")
    time.sleep(3)

    sentence_list = []
    for sentence in sentence_list:
        if word in sentence:
            sentence_list.append(sentence)

    visited_word[word] = sentence_list
    return sentence_list


print(get_sentences("Hello"))
print(get_sentences("Hello"))