from nltk.corpus import words



signatures = {}
count = 0
for word in words.words():
    signatures[word] = sorted(word)

print(len(signatures))
def findAnagrams(aWord):
    word_sig = sorted(aWord)
    anagramWords = []
    for word, sig in signatures.items():
        if sig == word_sig:
            anagramWords.append(word)
    return anagramWords
            

print(findAnagrams("steal"))
print(findAnagrams("eat"))
print(findAnagrams("cat"))
print(findAnagrams("pears"))
