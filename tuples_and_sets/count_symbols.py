text = input()
chars = {}

for char in text:
    if char not in chars:
        chars[char] = 1
    else:
        chars[char] += 1

sorted_chars = dict(sorted(chars.items(), key=lambda item: item[0]))

for char in sorted_chars:
    print(f"{char}: {chars[char]} time/s")