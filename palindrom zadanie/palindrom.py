def is_palindrome(word):
    word = word.lower()
    letters_only = ''.join(char for char in word if char.isalnum())
    return letters_only == letters_only[::-1]
    
  


print(is_palindrome("radar"))
print(is_palindrome("Kobyća ma mały bok")) 
print(is_palindrome("A man, a plan, a canal - panama"))
print(is_palindrome("Definitely a palindrome")) 
print(is_palindrome("Łał")) 