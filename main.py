from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    result = list()
    length = len(nums)

    done = False
    for i in range(length):
        for j in range(i+1, length):
            if (nums[i] + nums[j] == target):
                result.append(i)
                result.append(j)
                done = True
                break
        if (done):
            break


    return result