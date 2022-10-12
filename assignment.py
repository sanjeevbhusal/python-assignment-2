visited_word = {}

sentence_list = ["Hello World", "Hello Again", "Hello There", "Apple", "Apple and Anaconda"]

for sentence in sentence_list:
    word_list = sentence.split()
    for word in word_list:
        if word in visited_word:
            associated_sentences = visited_word[word]
            associated_sentences.append(sentence)
        else:
            visited_word[word] = [sentence]


def get_sentences(word):
    return visited_word[word]


print(get_sentences("Hello"))
print(get_sentences("Hello"))
print(get_sentences("Apple"))
print(get_sentences("Apple"))

