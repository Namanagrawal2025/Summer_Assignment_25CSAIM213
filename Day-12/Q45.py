def is_palindrome(text):
    clean_text = str(text).replace(" ", "").lower()
    return clean_text == clean_text[::-1]
print(is_palindrome("radar"))  # True
print(is_palindrome(12321))    # True
