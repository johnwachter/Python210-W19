#Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
  counter = []
  for i in nums:
    print(i)
    if i == 9:
      counter.append(1)
print(array_count9([1,2,9]))

#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
    desired = [1, 2, 3]
    print(str(desired)[1:-1])
    if str(desired)[1:-1] in str(nums):
        return True
    return False
