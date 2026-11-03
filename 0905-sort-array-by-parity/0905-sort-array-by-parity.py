class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        pare = []
        impare = []

        for x in nums:
            if x % 2 == 0:
                pare.append(x)
            else:
                impare.append(x)

        return pare + impare