from pprint import pprint
sentence = "This is the common interview question"

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(sorted(char_frequency.items(), key=lambda kv: kv[1]), width=1)