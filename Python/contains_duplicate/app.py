
def containsDuplicate(nums):
    cash = set()
    for num in nums:
        if num in cash:
            return True
        cash.add(num)
    return False
