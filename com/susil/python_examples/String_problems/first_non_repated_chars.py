from collections import Counter
s = "aabbccddef"

count = Counter(s)
print(count)
first_non_repeated_chars = ''
for key, value in count.items():
    if value == 1:
        first_non_repeated_chars=key
        break

print(first_non_repeated_chars)
