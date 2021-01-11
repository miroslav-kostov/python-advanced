text = "ILovePython"
#text = input()
VOWELS = {'a', 'o', 'u', 'e', 'i'}
VOWELS = VOWELS.union(x.upper() for x in VOWELS)

print(VOWELS)

print("".join([x for x in text if x not in VOWELS]))
