
class Solution(object):
    def minElement(self, nums):
        digit_sums = []

        for num in nums:
            total = 0

            while num > 0:
                digit = num % 10
                total += digit
                num //= 10

            digit_sums.append(total)

        return min(digit_sums)

