def is_palindrome(seq):
    return seq == seq[::-1]

words = input('Put your word : ').split()
print("YES" if is_palindrome(words) else "NO")
