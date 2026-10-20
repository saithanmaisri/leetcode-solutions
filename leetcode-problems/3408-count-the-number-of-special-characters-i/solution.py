
class Solution(object):
    def numberOfSpecialChars(self, word):
        count = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":
            if ch in word and ch.upper() in word:
                count += 1

        return count

