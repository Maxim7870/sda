
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        mijloc = len(nums) // 2

        stanga = self.sortArray(nums[:mijloc])
        dreapta = self.sortArray(nums[mijloc:])

        rezultat = []
        i = 0
        j = 0

        while i < len(stanga) and j < len(dreapta):
            if stanga[i] <= dreapta[j]:
                rezultat.append(stanga[i])
                i += 1
            else:
                rezultat.append(dreapta[j])
                j += 1

        while i < len(stanga):
            rezultat.append(stanga[i])
            i += 1

        while j < len(dreapta):
            rezultat.append(dreapta[j])
            j += 1

        return rezultat
