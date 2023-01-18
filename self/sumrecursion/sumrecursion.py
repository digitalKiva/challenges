# O(n) recursion algorithm to calculate the sum of an `int` list

def sum(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + sum(nums[1:])

def main():
    assert(sum([1,3,4]) == 8)
    assert(sum([10]) == 10)
    assert(sum([]) == 0)
    assert(sum([-1, 0, 1]) == 0)

    print(f"Success!")


if __name__ == "__main__":
    main()