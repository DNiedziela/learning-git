import string

def is_palindrome(word):
    word = word.lower()
    letters_only = ''.join(char for char in word if char in string.ascii_lowercase)
    return letters_only == letters_only[::-1]
    
  


print(is_palindrome("radar"))
print(is_palindrome("bulbula@Eto@#346 r")) 
print(is_palindrome("A man, a plan, a canal - panama"))
print(is_palindrome("Definitely a palindrome")) 
print(is_palindrome("B")) 