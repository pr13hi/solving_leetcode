# Concept name : Hash Map / Set

# Question : Determine if Two Strings Are Close

#            Two strings are considered close if you can attain one from the other using the following operations:
          
#            Operation 1: Swap any two existing characters.
#            For example, abcde -> aecdb
#            Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#            For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
#            You can use the operations on either string as many times as necessary.
          
#            Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
          
#                       Example 1:
                      
#                       Input: word1 = "abc", word2 = "bca"
#                       Output: true
#                       Explanation: You can attain word2 from word1 in 2 operations.
#                       Apply Operation 1: "abc" -> "acb"
#                       Apply Operation 1: "acb" -> "bca"
          
# Solution : 

class Solution(object):
    def closeStrings(self, word1, word2):
        s1 = set(word1)
        s2 = set(word2)

        if s1 != s2:
            return False
        
        freq_word1=Counter(word1)
        freq_word2=Counter(word2)

        sorted_word1=sorted(freq_word1.values())
        sorted_word2=sorted(freq_word2.values())

        keys_match=set(freq_word1.keys())==set(freq_word2.keys())

        return sorted_word1==sorted_word2 and keys_match

# Explanation : Convert word1 and word2 to sets s1 and s2 → to check if both strings use the same set of characters.
#                       If s1 != s2, return False.
#               Use Counter to count the frequency of each character in both strings.
#               Sort the frequency values from both counters.
#               Check if:
#                       The sorted frequency values are the same.
#                       The keys (characters) in both counters match as sets.
#               Return True only if both sorted frequencies and character sets match.
