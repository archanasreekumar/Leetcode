def isPalindrome_bruteforce(s: str) -> bool:
    lower = ""
    for ch in s:
        if ch.isalnum():
            lower += ch
    # return lower == lower[::-1] # or use below function
    lower_reversed = ""
    for ch in lower:
        lower_reversed = ch + lower_reversed
    return lower == lower_reversed


print(isPalindrome_bruteforce("MamaM*"))
