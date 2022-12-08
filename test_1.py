from unittest import TestCase, main
from whiteboard import *

from demo import check_palindrome

# Demo
class MatchTestCase(TestCase):
    def test_pal(self):
        self.assertTrue(check_palindrome('racecar'))
    def test_pal_with_caps(self):
        self.assertTrue(check_palindrome('Racecar'))
    def test_no_pal(self):
        self.assertFalse(check_palindrome('asymmetrical'))
    def test_no_wrong(self):
        self.assertFalse(check_palindrome('asymmetrical'))
#
class MatchTestCase_Make_Acronym(TestCase):
    def test_1(self):
        self.assertEqual(to_acronym("Code Wars"), "CW")
    def test_2(self):
        self.assertEqual(to_acronym("hyper text markup language"), "HTML")
#
class MatchTestCase_Add_Count(TestCase):
    def test_empty(self):
        self.assertFalse(count_positives_sum_negatives([]))
    def test_pal_with_caps(self):
        self.assertEqual(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
class MatchTestCase_Add_Count_Recur(TestCase):
    def test_empty(self):
        self.assertFalse(count_p_sum_n_recur([]))
    def test_pal_with_caps(self):
        self.assertEqual(count_p_sum_n_recur([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
#
class MatchTestCase_Permute_a_Palindrome(TestCase):
    def test_1(self):
        self.assertEqual(permute_a_palindrome("a"), True)
    def test_4(self):
        self.assertEqual(permute_a_palindrome("aA"), True)
    def test_2(self):
        self.assertEqual(permute_a_palindrome("baabcd"), False)
    def test_3(self):
        self.assertEqual(permute_a_palindrome("racecars"), False)
#
class MatchTestCase_ReverseVowels(TestCase):
    def test_1(self):
        self.assertEqual(reverseVowels('hello'),'holle')
    def test_2(self):
        self.assertEqual(reverseVowels('leetcode'),"leotcede")
#
class MatchTestCase_Find_Missing(TestCase):
    def test_1(self):
        self.assertEqual(find_missing([1,2,3,4,5], [3,4,1,5]), 2)
    def test_2(self):
        self.assertEqual(find_missing([1,2,3,4,5,6,7,8,9], [1,9,7,4,6,2,3,8]),5)
    def test_3(self):
        self.assertEqual(find_missing([1,2,3,4,5,6,7,8,9], [5,7,6,9,4,8,1,2,3]), 0)
#Done
class MatchTestCase_Stanton_Measure(TestCase):
    def test_1(self):
        self.assertEqual(stanton_measure([1, 4, 3, 2, 1, 2, 3, 2]), 3)
    def test_2(self):
        self.assertEqual(stanton_measure([1, 3, 5, 2, 3, 1, 3, 11, 1, 13, 0, 3, 10, 3, 9, 4, 6, 12, 8, 7, 3, 3]),7)
#
class MatchTestCase_Biggest_One(TestCase):
    def test_1(self):
        self.assertEqual(biggest_one([11,11,99,24,24,1,1,1]),99)
    def test_2(self):
        self.assertEqual(biggest_one([11,11,99,24,24,1,1,1,99,2]),2)
    def test_3(self):
        self.assertEqual(biggest_one([1,2,1,2,4,4,8,8]), -1)
#
class MatchTestCase_find_dups_miss(TestCase):
    def test_1(self):
        self.assertEqual(find_dups_miss([10, 9, 8, 9, 6, 1, 2, 4, 3, 2, 5, 5, 3]),
        [7, [2, 3, 5, 9]])
    def test_2(self):
        self.assertEqual(find_dups_miss([20, 19, 6, 9, 7, 17, 16, 17, 12, 5, 6, 8, 9, 10, 14, 13, 11, 14, 15, 19]),
        [18, [6, 9, 14, 17, 19]])
class MatchTestCase_Sort_Dict(TestCase):
    def test_1(self):
        self.assertEqual(sort_dict({3:1, 2:2, 1:3}), [(1,3), (2,2), (3,1)])
    def test_2(self):
        self.assertEqual(sort_dict({1:2, 2:4, 3:6}), [(3,6), (2,4), (1,2)])
# 
class MatchTestCase_Feast(TestCase):
    def test_1(self):
        self.assertTrue(feast("great blue heron", "garlic naan"), True)
    def test_2(self):
        self.assertTrue(feast("chickadee", "chocolate cake"), True)
    def test_3(self):
        self.assertFalse(feast("brown bear", "bear claw"), False)
# 
class MatchTestCase_Last(TestCase):
    def test_1(self):
        self.assertEqual(last([1,2,3]), 3)
    def test_2(self):
        self.assertEqual(last([]), -1)
    def test_3(self):
        self.assertEqual(last([3,5,78,97,888,[1,2,3],5,10]), 10)
#   reduce directions
class MatchTestCase_Reduce_Directions(TestCase):
    def test_1(self):
        self.assertEqual(dirReduc(['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']), ["WEST"])
    def test_2(self):
        self.assertEqual(dirReduc([]),[])
    def test_3(self):
        self.assertEqual(dirReduc(['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH', 'SOUTH', 'NORTH']),['NORTH', 'NORTH', 'EAST', 'SOUTH', 'EAST', 'EAST', 'SOUTH', 'SOUTH'])
# 
class MatchTestCase_StreetLights(TestCase):
    def test_1(self):
        self.assertEqual(streetLights(['T',"F","F",'F']), "Outage")
    def test_2(self):
        self.assertEqual(streetLights(['T',"T"]),'Power')
    def test_3(self):
        self.assertEqual(streetLights(['T','T','F']),'Power')
# narcissistic 
class MatchTestCase_Narcissistic(TestCase):
    def test_1(self):
        self.assertTrue(is_narcissistic(153))
    def test_2(self):
        self.assertFalse(is_narcissistic(201))
    def test_3(self):
        self.assertFalse(is_narcissistic(259))
    def test_4(self):
        self.assertTrue(is_narcissistic(1634))
# 
class MatchTestCase_Product_Array(TestCase):
    def test_1(self):
        self.assertEqual(product_array([12,20]), [20,12])
    def test_2(self):
        self.assertEqual(product_array([3,27,4,2]), [216,24,162,324])
    def test_3(self):
        self.assertEqual(product_array([16,17,4,3,5,2]), [2040,1920,8160,10880,6528,16320])  
# 
class MatchTestCase_Add_10(TestCase):
    def test_1(self):
        self.assertEqual(move_ten("testcase"), "docdmkco")
    def test_2(self):
        self.assertEqual(move_ten("exampletesthere"), "ohkwzvodocdrobo")
# 
#Strings:starts with 
# class MatchTestCase_Starts_With(TestCase):
#     def test_1(self):
#         self.assertEqual(starts_with"hello world!", "hello"), True)
#     def test_2(self):
#         self.assertEqual(starts_with("hello world!", "HELLO"), False)
#     def test_3(self):
#         self.assertEqual(starts_with("nowai", "nowaisir"), False)

# 
class MatchTestCase_arr_adder(TestCase):
    def test_1(self):
        self.assertEqual(arr_adder([
            ['J','L','L','M'],
            ['u','i','i','a'],
            ['s','v','f','n'],
            ['t','e','e','' ]
        ]),"Just Live Life Man")
    def test_2(self):
        self.assertEqual(arr_adder([
            ['T','M','i','t','p','o','t','c'],
            ['h','i','s','h','o','f','h','e'],
            ['e','t','', 'e','w','', 'e','l'],
            ['', 'o','', '', 'e','', '', 'l'],
            ['', 'c','', '', 'r','', '', '' ],
            ['', 'h','', '', 'h','', '', '' ],
            ['', 'o','', '', 'o','', '', '' ],
            ['', 'n','', '', 'u','', '', '' ],
            ['', 'd','', '', 's','', '', '' ],
            ['', 'r','', '', 'e','', '', '' ],
            ['', 'i','', '', '', '', '', '' ],
            ['', 'a','', '', '', '', '', '' ]
        ]), "The Mitochondria is the powerhouse of the cell")
# 
class MatchTestCase_I(TestCase):
    def test_1(self):
        self.assertEqual(i("Phone"), 'iPhone')
    def test_2(self):
        self.assertEqual(i('World'),'iWorld')
    def test_3(self):
        self.assertEqual(i('road'),'Invalid word')
    def test_4(self):
        self.assertEqual(i('Inspire'),'Invalid word')
    def test_5(self):
        self.assertEqual(i('Peace'),'Invalid word')


# What adds up - 6
# class MatchTestCase_Adds_Up(TestCase):
#     def test_1(self):
#         self.assertEqual(addsup([1,2,5],[3,1],[5,4,6]), [[1,3,4], [2,3,5], [5,1,6]])
#     def test_2(self):
#         self.assertEqual(addsup([1, 3, 4], [], [4, 6, 5]), [])
#     def test_3(self):
#         self.assertEqual(addsup([39], [10], [26, 8, 2, 23, 11, 23, 33]), [])

# get_length_of_missing_array -6
# class MatchTestCase_get_length_of_missing_array(TestCase):
#     def test_1(self):
#         self.assertEqual(get_length_of_missing_array([[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]), 3)
#     def test_2(self):
#         self.assertEqual(get_length_of_missing_array([[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]), 2)
#     def test_3(self):
#         self.assertEqual(get_length_of_missing_array([[5, 2, 9], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]],[1,3]),0)
#     def test_4(self):
#         self.assertEqual(get_length_of_missing_array([]), 0)
#     def test_5(self):
#         self.assertEqual(get_length_of_missing_array([[5, 2, 9], None, [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]),0)

class MatchTestCase_Morse_Code(TestCase):
    def test_1(self):
        self.assertEqual(morseCode(["gin","zen","gig","msg"]), 2)
    def test_2(self):
        self.assertEqual(morseCode(['hello']), 1)

class MatchTestCase_Merged_Lists(TestCase):
    def test_1(self):
        self.assertEqual(merge_lists([1,2,3,0,0,0], 3, [2,5,6], 3),[1,2,2,3,5,6])
    def test_2(self):
        self.assertEqual(merge_lists([1], 1, [], 0),[1])
    def test_3(self):
        self.assertEqual(merge_lists( [0], 0, [1], 1),[1])

class MatchTestCase_Ransom_Note(TestCase):
    def test_1(self):
        self.assertEqual(isRansomNote('a','b'),False)
    def test_2(self):
        self.assertEqual(isRansomNote('aa','ab'),False)
    def test_3(self):
        self.assertEqual(isRansomNote('aa','aab'),True)
    def test_4(self):
        self.assertEqual(isRansomNote("give me your chicken sandwhich",'proof birds are drones'),False)



if __name__ == '__main__':
    main()
