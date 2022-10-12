from collections import defaultdict
visited_word = defaultdict(list)

sentence_list = ["Hello Hello", "Hello Again", "Hello There", "Apple", "Apple and Anaconda"]

for sentence in sentence_list:
    word_list = sentence.split()
    for word in word_list:
        visited_word[word].append(sentence)


def get_sentences(word):
    return visited_word[word]


print(get_sentences("Hello"))
print(get_sentences("Hello"))
print(get_sentences("Apple"))
print(get_sentences("Apple"))
