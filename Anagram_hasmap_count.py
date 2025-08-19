def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    freq = {}
    for ch in word1:
        freq[ch] = word1.count(ch)

    for ch in word2:
        if ch not in map:
            return False

    return True



word1 = "arrrchanaa"
word2 = "rrachana"
print(is_anagram(word1, word2))