#Longest Substring Without Repeating Characters
s = "abcabcbb"

char_set = set()
left = 0
max_len = 0

for right in range(len(s)):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1

    char_set.add(s[right])
    max_len = max(max_len, right - left + 1)

print(max_len)

#Product of Array Except Self
nums = [1,2,3,4]

n = len(nums)
answer = [1]*n

prefix = 1
for i in range(n):
    answer[i] = prefix
    prefix *= nums[i]

suffix = 1
for i in range(n-1,-1,-1):
    answer[i] *= suffix
    suffix *= nums[i]

print(answer)

#Majority Element
nums = [2,2,1,1,1,2,2]

candidate = None
count = 0

for num in nums:
    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

print(candidate)

#Valid Palindrome
s = "A man, a plan, a canal: Panama"

new = ""

for ch in s:
    if ch.isalnum():
        new += ch.lower()

print(new == new[::-1])

#Search in Rotated Sorted Array
nums = [4,5,6,7,0,1,2]
target = 0

left = 0
right = len(nums)-1

while left <= right:

    mid = (left+right)//2

    if nums[mid] == target:
        print(mid)
        break

    if nums[left] <= nums[mid]:

        if nums[left] <= target < nums[mid]:
            right = mid-1
        else:
            left = mid+1

    else:

        if nums[mid] < target <= nums[right]:
            left = mid+1
        else:
            right = mid-1
else:
    print(-1)

#Find Missing and Repeating Number
nums = [3,1,2,5,3]

n = len(nums)

count = [0]*(n+1)

for num in nums:
    count[num] += 1

for i in range(1,n+1):

    if count[i] == 2:
        repeating = i

    if count[i] == 0:
        missing = i

print("Repeating:", repeating)
print("Missing:", missing)

#Merge Overlapping Intervals
intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()

merged = [intervals[0]]

for current in intervals[1:]:

    last = merged[-1]

    if current[0] <= last[1]:
        last[1] = max(last[1], current[1])

    else:
        merged.append(current)

print(merged)

#Detect Cycle in Linked List
slow = head
fast = head

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True

return False