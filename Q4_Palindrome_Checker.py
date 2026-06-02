def is_palindrome(text): # function to check palindrome

text = text.replace(" ", "").lower()        # remove spaces and convert into lowercase

return text == text[::-1]            # compare original and reverse string

print(is_palindrome("level"))            # testing values

print(is_palindrome("Hello"))

print(is_palindrome("racecar"))

print(is_palindrome("A man a plan a canal Panama"))
