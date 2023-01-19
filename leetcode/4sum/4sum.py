
def xsum(nums: list[int], sum: int, x: int) -> list[list[int]]:
    res = []

    if not nums:
        return res

    if x == 2:
        return twosum(nums, sum)

    # for each number in the list, append it to the results from a recursive call
    # using the rest of the list and a sum that is less 'this number'
    for i in range(len(nums) - 2):
        # detect and skip duplicates
        if i == 0 or nums[i] != nums[i - 1]:
            for subnums in xsum(nums[i + 1 :], sum - nums[i], x - 1):
                res.append([nums[i]] + subnums)

    return res

def twosum(nums: list[int], sum: int) -> list[list[int]]:
    res = []
    b = 0
    e = len(nums) - 1
    # walk from both ends of the list, finding all pairs equaling the sum
    while b < e:
        cs = nums[b] + nums[e]
        # if our sum is too high or nums[e] is the same as last time (prevent dups)
        if cs > sum or (e < len(nums) - 1 and nums[e] == nums[e + 1]):
            e = e - 1
        # if our sum is too low or nums[b] is the same as last time (prevent dups)
        elif cs < sum or (b > 0 and nums[b] == nums[b - 1]):
            b = b + 1
        else:
            res.append([nums[b], nums[e]])
            b = b + 1
            e = e - 1

    return res


def main():
    a = [1, 4, 5, 2, 2, 4]
    s = 6
    res = twosum(sorted(a), s)
    print(res)
    assert res == [[1, 5], [2, 4]]

    a = [1, 4, 5, 2, 2, 4]
    s = 10
    res = xsum(sorted(a), s, 3)
    print(res)
    assert res == [[1, 4, 5], [2, 4, 4]]

    a = [1, 0, -1, 0, -2, 2]
    s = 0
    res = xsum(sorted(a), s, 4)
    print(res)
    assert res == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    a = [2, 2, 2, 2, 2]
    s = 8
    res = xsum(sorted(a), s, 4)
    print(res)
    assert res == [[2, 2, 2, 2]]


if __name__ == "__main__":
    main()
