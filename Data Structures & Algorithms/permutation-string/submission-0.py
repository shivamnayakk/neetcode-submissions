class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        # Frequency of s1
        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1

        # First window
        for i in range(len(s1)):
            freq2[ord(s2[i]) - ord('a')] += 1

        if freq1 == freq2:
            return True

        left = 0

        # Sliding window
        for right in range(len(s1), len(s2)):
            # Add right character
            freq2[ord(s2[right]) - ord('a')] += 1

            # Remove left character
            freq2[ord(s2[left]) - ord('a')] -= 1
            left += 1

            # Compare frequencies
            if freq1 == freq2:
                return True

        return False