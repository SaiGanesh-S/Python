# Input: 
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums= [3,3]#[3,2,4]#[2,7,11,15]
target = 6

#brute force 
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print("BruteForce>",i,j,end=" ")
            break
print()
#hash map
hashMap = {}
for i,n in enumerate(nums):
    diff = target - n
    if diff in hashMap:
        print("hashmap>" ,i,hashMap[diff])
    hashMap[n]=i