class Solution:
    def reverseBits(self, n):
        n = format(n, 'b')
        n = n.zfill(32)
        return int(n[::-1], 2)
