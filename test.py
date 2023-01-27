nums=[1,4,4,4]
target = 8

hashmap = {}
for i in range(len(nums)):
    hashmap[nums[i]] = i
print(hashmap)
for i in range(len(nums)):
    complement = target - nums[i]
    if complement in hashmap and hashmap[complement] != i:
        print([i, hashmap[complement]])