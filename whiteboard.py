# first 100 prime numbers
set(range(3, 100)).difference(set(x for x in range(3, 100)
    for y in range(2, x//2) if x % y == 0))

def mixing(astring):
    nums,letters=[num for num in astring if num.isdigit()],[letter for letter in astring if letter.isalpha()]
    if abs(len(nums)-len(letters)) > 1:
        return ''
    if len(letters) > len(nums):
        return ''.join(f'{letters[i]}{nums[i]}'for i in range(len(nums)))+letters[-1]
    numFirst = ''.join(f'{nums[i]}{letters[i]}'for i in range(len(letters)))
    return numFirst+nums[-1] if len(nums) > len(letters) else numFirst
    
# print(mixing("a0b1c2"))
# print(mixing("leetcode"))
# print(mixing("1229857369"))
# print(mixing("covid2019"))
# print(mixing("ab123"))

# Create a function that takes an array of letters, and combines them into words in a sentence.
# The array will be formatted as so:
# [['J','L','L','M']
# ,['u','i','i','a']
# ,['s','v','f','n']
# ,['t','e','e','']]
# The function should combine all the 0th indexed letters to create the word 'just', all the 1st indexed letters to
# create the word 'live', etc.
# Shorter words will have an empty string in the place once the word has already been mapped out
# (see the last element in the last element in the array).
# arrAdder([
# ['J','L','L','M'],
# ['u','i','i','a'],
# ['s','v','f','n'],
# ['t','e','e','']
# ]) // => "Just Live Life Man"
# arrAdder([
#   [ 'T', 'M', 'i', 't', 'p', 'o', 't', 'c' ],
#   [ 'h', 'i', 's', 'h', 'o', 'f', 'h', 'e' ],
#   [ 'e', 't', '', 'e', 'w', '', 'e', 'l' ],
#   [ '', 'o', '', '', 'e', '', '', 'l' ],
#   [ '', 'c', '', '', 'r', '', '', '' ],
#   [ '', 'h', '', '', 'h', '', '', '' ],
#   [ '', 'o', '', '', 'o', '', '', '' ],
#   [ '', 'n', '', '', 'u', '', '', '' ],
#   [ '', 'd', '', '', 's', '', '', '' ],
#   [ '', 'r', '', '', 'e', '', '', '' ],
#   [ '', 'i', '', '', '', '', '', '' ],
#   [ '', 'a', '', '', '', '', '', '' ] ])
#  // => "The Mitochondria is the powerhouse of the cell"
#
# Done
def arr_adder(arr):
    words = {}
    for alist in arr:
        for i, letter in enumerate(alist):
            words[i] = words.get(i, '')+ letter
    return ' '.join(words.values())

def findIntersect(l1,l2):
    return list(set(l1).intersection(set(l2)))

def intersect(l1, l2):
    return list(set(l1) & set(l2))

def compare_strings(s1, s2):
    new1, new2 = [], []
    for i in range(len(s1)):
        if s1[i] == '#' and new1:
            new1.pop()
        else:
            new1.append(s1[i])
    for i in range(len(s2)):
        if s2[i] == '#' and new2:
            new2.pop()
        else:
            new2.append(s2[i])
    return new1==new2
 
# print(compare_strings("ab#c", "ad#c"),True)
# print(compare_strings("ab##", "c#d#"),True)
# print(compare_strings("a#c", "b"),False)

def is_consec(alist):
    for i in range(len(alist)-1):
        if alist[i] + 1 != alist[i+1]:
            return False
        return True 

def permute_a_palindrome(astring): 
    hash_map,count={},0
    for letter in astring:
        hash_map[letter]=hash_map.get(letter,0)+1
    for letter in hash_map:
        if hash_map[letter]%2==1:
            count+=1
            if count > 1:
                return False
    return True
#
def growing_plant(upSpeed, downSpeed, desiredHeight):
    days, height = 0, 0
    while height < desiredHeight:
        if days > 0:
            height -= downSpeed
        days += 1
        height += upSpeed
    return days


def min_max(aString):
    numList = [int(num) for num in aString.split()]
    return f'{min(numList)} {max(numList)}'


def needle(h, n):
    return -1 if n.lower() not in h.lower() else h.lower().index(n.lower())


def search(alist, target):
    left, right = 0, len(alist)-1
    while left <= right:
        if alist[left] == target:
            return left
        if alist[right] == target:
            return right
        middle = left+right//2
        if alist[middle] > target:
            right = middle-1
            left += 1
        elif alist[middle] < target:
            left = middle+1
            right -= 1
        else:
            return middle
    return -1


def recursive_search2(alist, target, left=0, right=0):
    right = len(alist)-1 if right == 0 else right
    if alist[left] == target or alist[right] == target:
        return right if alist[right] == target else left
    middle = (left+right)//2
    left = middle if target > alist[middle] else left + 1
    right = middle if target < alist[middle] else right - 1
    return middle if alist[middle] == target else -1 if left >= right else recursive_search(alist, target, left, right)


def recursive_search(alist, target, left=0, right=0):
    return (lambda right: (lambda middle: (lambda middle, left, right: middle if alist[middle] == target else -1 if left >= right else recursive_search(alist, target, left, right))(middle, middle if target > alist[middle] else left + 1, middle if target < alist[middle] else right - 1))((left+right)//2) if alist[left] != target and alist[right] != target else right if alist[right] == target else left)(len(alist)-1 if right == 0 else right)


# print(recursive_search([1, 2, 3, 4, 5, 6, 7, 8], 5))
# print(recursive_search([1, 2, 3, 4, 6, 7, 8], 5))
# print(recursive_search([1, 2, 3, 4, 6, 7, 8], 8), 6)
# print(recursive_search([1, 2, 3, 4, 6, 7, 8], 1), 0)
# print(recursive_search([1, 2, 3, 4, 6, 7, 8, 10], 8), 6)

# Remove Duplicates return list in og order
# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118/train/python
#


def distinct(seq):
    hash_map = {}
    for num in seq:
        hash_map[num] = hash_map.get(num, 0)+1
    return [key for key in hash_map]


def in_place_distinct(seq):
    if len(seq) < 2:
        return seq
    i = len(seq)-1
    while i >= 0:
        if seq.count(seq[i]) > 1:
            seq.pop(i)
        i -= 1
    return seq
#


def remove_vowels(str):
    return ''.join(x for x in str if x.lower() not in {'a', 'e', 'i', 'o', 'u'})
#


def check_consec(alist, num1, num2):
    return abs(alist.index(num1) - alist.index(num2)) == 1
#


def birthstone(month):
    stones = {1: "Garnet", 2: "Amethyst", 3: "Aquamarine", 4: "Diamond", 5: "Emerald", 6: "Pearl",
              7: "Ruby", 8: "Peridot", 9: "Sapphire", 10: "Opal", 11: "Topaz", 12: "Turquoise"}
    return stones[month] if month < 13 else "Try again"
# Electric Company
# Create a function that given a list which represents street lights given as a parameter(l_street), determine if an outage has occurred. A street with a total number of “F” greater than or equal to 2 returns “Outage”, anything below returns “Power”
# Example Input: [ ‘T’, ‘F’, ‘F’, ‘F’ ]
# Example Output: “Outage”
#


def streetLights(alist):
    return 'Power' if alist.count('F') < 2 else 'Outage'
    left = 0
    right = len(alist)-1
    while left < right:
        if alist[left] == 'F' and alist[right] == 'F':
            return 'Outage'
        if alist[left] != 'F':
            left += 1
        if alist[right] != 'F':
            right -= 1
    return 'Power'
# Make Acronym https://www.codewars.com/kata/57a60bad72292d3e93000a5a/train/python
#


def to_acronym(astring):
    return ''.join(word[0].upper() for word in astring.split())
# count postivie sum negative https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
#


def count_positives_sum_negatives(arr):
    return [len(arr)-len([x for x in arr if x < 0]), sum([x for x in arr if x < 0])] if arr else []


def count_p_sum_n_recur(alist, i=0, count=0, add=0):
    if i >= len(alist):
        return [count, add] if alist else []
    if alist[i] > 0:
        count += 1
    else:
        add += alist[i]
    i += 1
    return count_p_sum_n_recur(alist, i, count, add)
#
# You are given a list of numbers and a second list which is a scrambled version of the
# of the first list. Here is the kicker one number may be missing. Your job is to return
#  the missing number or 0 if both lists contain all the same numbers.
#


def find_missing(l, mixed):
    # return 0 if len(l) == len(mixed) else list(set(l) - set(mixed))[0]
    counts = {}
    for i in range(len(l)):
        counts[l[i]] = counts.get(l[i], 0)+1
        if i < len(mixed):
            counts[mixed[i]] = counts.get(mixed[i], 0)-1
    for k in counts:
        if counts[k] == 1:
            return k
    return 0
#
# Permute a Palindrome https://www.codewars.com/kata/58ae6ae22c3aaafc58000079/train/python


def permute_a_palindrome(astring):
    hash_map, count = {}, 0
    for letter in astring.lower():
        hash_map[letter] = hash_map.get(letter, 0)+1
    for letter in hash_map:
        if hash_map[letter] % 2 == 1:
            count += 1
            if count > 1:
                return False
    return True
# Stanton Measure https://www.codewars.com/kata/59a1cdde9f922b83ee00003b
#


def stanton_measure(arr):
    hash_map = {}
    for num in arr:
        hash_map[num] = hash_map.get(num, 0)+1
    return hash_map[hash_map[1]]
#


def biggest_one(alist):
    counts = {}
    for num in alist:
        counts[num] = counts.get(num, 0)+1
    ones = [k for k in counts if counts[k] == 1]
    return max(ones) if ones else -1


def biggest_one_with_count(alist):
    occurs_once = [num for num in alist if alist.count(num) == 1]
    return max(occurs_once) if occurs_once else -1
#


def find_dups_miss(arr):
    num_hash = {}
    for num in arr:
        num_hash[num] = num_hash.get(num, 0)+1
    dups = [x for x in range(min(arr), max(arr))
            if x in num_hash and num_hash[x] > 1]
    for i in range(min(arr), max(arr)):
        if i not in num_hash:
            return [i, dups]


# In this kata, we have an unsorted sequence of consecutive numbers from a to b, such that a < b always (remember a, is
# the minimum, and b the maximum value). They were introduced an unknown amount of duplicates in this sequence and we
# know that there is an only missing value such that all the duplicate values and the missing value are between a and b,
# but never coincide with them. Find the missing number with the duplicate numbers (duplicates should be output in a sorted array).
# Let's see an example:
# arr = [10,9,8,9,6,1,2,4,3,2,5,5,3]
# find_dups_miss([10,9,8,9,6,1,2,4,3,2,5,5,3]) == [7,[2,3,5,9]]
# The code should be fast to process long arrays (maximum length aprox. = 1.000.000). The values for the randon tests:
# 500 <= a <= 50000
# a + k <= b and 100 <= k <= 1000000
# amount of duplicates variable, according to the length of the array
#
'''
Sorting Dictionaries - https://www.codewars.com/kata/53da6a7e112bd15cbc000012/train/python
'''


def sort_dict(d):
    flip_dict = {v: k for k, v in d.items()}
    return [(flip_dict[k], k) for k in sorted(flip_dict, reverse=True)]

# A Narcissistic Number is a number of length l in which the sum of its digits to the power of l is equal to the original number. If this seems confusing, refer to the example below.
# Ex: 153, where l = 3 ( the number of digits in 153 )
# 13 + 53 + 33 = 153
# Write a function that, given n, returns whether or not n is a Narcissistic Number.
#


def is_narcissistic(i):
    return sum([int(num)**len(str(i)) for num in str(i)]) == i
# Task
# Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].
# Notes
#     Array/list size is at least 2 .
#     Array/list's numbers Will be only Positives
#     Repetition of numbers in the array/list could occur.
# Input >> Output Examples
# productArray ({12,20}) ==>  return {20,12}
#


def product_array(numbers):
    prod, output = 1, []
    i, pointer = 0, 0
    while pointer < len(numbers):
        if i != pointer:
            prod *= numbers[i]
        i += 1
        if i == len(numbers):
            output.append(prod)
            i, prod = 0, 1
            pointer += 1
    return output


def product_array2(numbers):
    output = []
    prod = 1
    for num in numbers:
        prod *= num
    for num in numbers:
        output.append(prod/num)
    return output

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
#


def reverseVowels(astring):
    left, right, lFlag, rFlag = 0, len(astring)-1, False, False
    astring = list(astring)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    while left < right:
        if astring[left] not in vowels:
            left += 1
        else:
            lFlag = True
        if astring[right] not in vowels:
            right -= 1
        else:
            rFlag = True
        if lFlag == True and rFlag == True:
            astring[left], astring[right] = astring[right], astring[left]
            left += 1
            right -= 1
            lFlag, rFlag = False, False
    return ''.join(astring)
#
# https://www.codewars.com/kata/5aa736a455f906981800360d/train/python


def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


# Move every letter in the provided string forward 10 letters through the alphabet.
# If it goes past 'z', start again at 'a'.
# Input will be a string with length > 0.
#
def move_ten(st):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(alph[alph.index(letter) + 10] if alph.index(letter) < 16 else alph[alph.index(letter)-16] for letter in st)


# Many people know that Apple uses the letter "i" in almost all of its devices to
# emphasize its personality. And so John, a programmer at Apple, was given the task of making a program that would add
# that letter to every word.
# Let's help him do it, too.
# Task:
# Your task is to make a function that takes the value of word and returns it with an "i" at the beginning of the word.
# For example we get the word "Phone", so we must return "iPhone". But we have a few rules:
#     The word should not begin with the letter "I", for example Inspire.
#     The number of vowels should not be greater than or equal to the number of consonants, for example East or Peace.
#     ("y" is considered a consonant)
#     The first letter should not be lowercase, for example road.
# If the word does not meet the rules, we return "Invalid word".
# If the list is empty: return None or null (depending on language)
#


def i(word):
    return 'Invalid word' if len([l for l in word if l.lower() in {'a', 'e', 'i', 'o', 'u'}]) >= len(word)/2 or word == '' or word[0].islower() or word[0] == 'I' else f'i{word}'



# Write a function last that accepts a list and returns the last element in the list.


def last(lst):
    return lst[-1] if lst else -1


# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example 1:
ransomNote2 = "a"
magazine2 = "b"
# Output: false
# Example 2:
ransomNote1 = "aa"
magazine1 = "ab"
# Output: false
# Example 3:
ransomNote = "aa"
magazine = "aab"
# Output: true
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.
#


def isRansomNote(note, mag):
    noteDict, magDict = {}, {}
    for letter in note:
        noteDict[letter] = noteDict.get(letter, 0)+1
    for letter in mag:
        magDict[letter] = magDict.get(letter, 0)+1
    for key in noteDict:
        if key not in magDict or noteDict[key] > magDict[key]:
            return False
    return True
# return the only element in alist that appears only once


def find_one(alist):
    counts = {}
    for num in alist:
        counts[num] = counts.get(num, 0)+1
    for key in counts:
        if counts[key] == 1:
            return key
    return [key for key in counts if counts[key] == 1][0]


# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
# the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first melements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n. Solve with a linear solution
# Example 1:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:
nums1_2 = [1]
m_2 = 1
nums2_2 = []
n_2 = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:
nums1_3 = [0]
m_3 = 0
nums2_3 = [1]
n_3 = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


def merge_lists(nums1, m, nums2, n):
    iOne, iTwo, iFinal = m-1 if m > 0 else 0, n-1, len(nums1)-1
    while iOne >= 0 <= iTwo:
        nums1[iFinal] = nums1[iOne] if nums1[iOne] >= nums2[iTwo] else nums2[iTwo]
        iFinal -= 1
        if nums1[iOne] >= nums2[iTwo]:
            iOne -= 1
        else:
            iTwo -= 1
    return nums1


def merge_lists3(nums1, m, nums2, n):
    iOne, iTwo = m-1 if m > 0 else 0, n-1
    for i in range(len(nums1)-1, 1, -1):
        nums1[i] = nums1[iOne] if nums1[iOne] >= nums2[iTwo] else nums2[iTwo]
        if nums1[iOne] >= nums2[iTwo]:
            iOne -= 1
        else:
            iTwo -= 1
    return nums1


def mergeLists2(nums1, m, nums2, n):
    iOne, iTwo, iFinal = m-1 if m > 0 else 0, n-1, len(nums1) - 1
    while iOne >= 0 <= iTwo:
        if nums1[iOne] >= nums2[iTwo]:
            nums1[iFinal] = nums1[iOne]
            iOne -= 1
        else:
            nums1[iFinal] = nums2[iTwo]
            iTwo -= 1
        iFinal -= 1
    return nums1

# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:
# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.
# Example 1:
# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".


def morseCode(alist):
    morse, alph = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
                   ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."], 'abcdefghijklmnopqrstuvwxyz'
    mDict = {alph[i]: morse[i] for i in range(26)}
    return len({''.join(mDict[letter.lower()] for letter in word) for word in alist})

# def shorter_two(astring):
#     count,small,i=1,len(astring),0
#     while i < len(astring):
#         small = count if count < small else small
#         if astring[i].isalpha():
#             count+=1
#         else:
#             count=1
#         i+=1
#     return small

# print(shorter_two("We built a nest and tested it."))
# print(shorter_two("Hello World JavaScript!"))
