# Find Palindrome
# Given a string of lowercase letters, write a function to see if the word is a palindrome 
# (the same word spelled forward and backwards).
# Example Input: ‘Racecar’
# Example Output: True 

def check_palindrome(word):
    left  = 0
    right =  len(word)-1
    while left < right:
        if word[left].lower() != word[right].lower():
            return False
        left+=1
        right = right - 1
    return True
    
    # return word.lower() == word[::-1].lower()

# print(check_palindrome("racecar"))
# print(check_palindrome("elephant"))

