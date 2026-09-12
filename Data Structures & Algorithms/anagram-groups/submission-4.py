class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for word in strs:

            sorted_words = ''.join(sorted(word))

            if sorted_words not in hashmap:

                hashmap[sorted_words] = []

            hashmap[sorted_words].append(word)
        
        return list(hashmap.values())






            
       
        