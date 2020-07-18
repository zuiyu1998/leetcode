def twoSum(nums, target: int):
    hashmap = {};
    for (i, num) in enumerate(nums):
        if hashmap.get(target-num) is not None:
            return [i, hashmap.get(target-num)]
        hashmap[num] = i