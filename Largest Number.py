class Solution:
    def largestNumber(self, nums):
        temp_max,output = "" , ""

        nums = [str(i) for i in nums]
        while nums:
            for i in nums:
                if not temp_max: temp_max = i
                else:
                    if i + temp_max > temp_max + i: temp_max=i
            output += temp_max
            nums.remove(temp_max)
            temp_max = ""
        return output if not output.startswith("0") else "0"