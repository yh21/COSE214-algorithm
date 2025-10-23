# code of Radix Sort

nums = [329, 457, 657, 839, 436, 720, 355]
dig = int(len(str(max(nums))))

def digit(n, d):
    if n >= 10 ** (d - 1):
        return int(str(n)[-d])
    else:
        return 0
    
for i in range(1, dig + 1):
    bucket = [[] for _ in range(10)]
    for number in nums:
        bucket[digit(number, i)].append(number)
    nums = list()
    for j in range(10):
        for number in bucket[j]:
            nums.append(number)
    
print(nums)