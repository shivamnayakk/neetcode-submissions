class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for word in strs:

            sorted(word)

            key = "".join(sorted(word))

            if key not in hashmap:

                hashmap[key] = []

            
            hashmap[key].append(word)
            
        return list(hashmap.values())
        
        