#https://app.codesignal.com/interview-practice/task/gxzW6jpXXkr3JNwXy/description

def productExceptSelf(nums, m):
    left = []
    right = []

    #calculate left cumulative products
    for i,num in enumerate(nums):
        if i > 0:
            left.append((left[i-1]*(num%m))%m)
        else:
            left.append(num%m)

    #calculate right cumulative products
    for i,num in enumerate(reversed(nums)):
        if i > 0:
            right.append((right[i-1]*(num%m))%m)
        else:
            right.append(num%m)
    right = list(reversed(right))
    ans = 0

    # the f_i = (left_i-1 * right_i+1)%M
    for i, num in enumerate(nums):
        if i == 0:
            ans = (ans + right[i+1])%m
        elif i == len(nums)-1 :
            ans = (ans + left[i-1])%m
        else:
            ans = (ans + (left[i-1] * right[i+1])%m)%m
    return ans