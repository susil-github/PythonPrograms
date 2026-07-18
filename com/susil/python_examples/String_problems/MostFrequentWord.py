from collections import Counter

text = """
spark python spark aws spark python
"""

word_list = text.split(" ")
count = Counter(word_list)
max_count = max(count.values())
word = ''
for key, value in count.items():
    if value == max_count:
        word=key
        break
print('The most frequent word is : ',word)