word_string = input("Text: ")
words = word_string.split()
# print(words)
word_lengths = []
word_to_count = {}
for word in words:
    word_lengths.append(len(word))
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
longest_length = max(word_lengths)
# print(word_to_count)
for word, count in word_to_count.items():
    print(f"{word:{longest_length}} : {count}")
