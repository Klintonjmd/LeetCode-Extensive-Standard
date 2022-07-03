#217 Contains Duplicate --- Hashing and Arrays --- Easy

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


#242 Valid Anagram --- Hashing and Arrays --- Easy
#Method 1 --- 2 Hashing
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            #These lines count the occurences of each character in their respective word.
            #The get function is used in case there is not an index for the letter.
            #The 0 is there as a default to initialize the counter with the "1 +" from the beginning.
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countS.get(t[i], 0)
        for j in countS:
            #This checks if the counts match and the get is there to catch key errors if the letter is not in T
            if countS[j] != countT.get(j, 0):
                return False
        
        return True

#Method 2 --- sort and check
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

#1 Two Sum --- Hashing and Arrays --- Easy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val -> index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

#49 Group Anagrams --- Hashing and Arrays --- Medium --- Needs Review
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values

        #This is the optimal O(m*n) solution.