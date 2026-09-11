class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        count = {}
        best = 0
        max_freq = 0

        for right in range(len(s)):

            # add current character into hashmap
            count[s[right]] = count.get(s[right], 0) + 1

            # store highest frequency character
            max_freq = max(max_freq, count[s[right]])

            # if replacements needed > k
            # shrink window
            while (right - left + 1) - max_freq > k:

                count[s[left]] -= 1
                left += 1

            # store maximum valid window
            best = max(best, right - left + 1)

        return best