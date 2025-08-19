def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    freq = {}
    for ch in word1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in word2:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    # final leftover check
    return all(v == 0 for v in freq.values())

word1 = "arrrchanaa"
word2 = "rrachana"
print(is_anagram(word1, word2))