def aFunction(word):
    if len(word)<1:
        return 'a\n'
    for c in word:
        if c=='a':
            return 'a\n'
    return '\n'

def digitOrder(num):
    nums=[0 for a in range(10)]
    for n in str(num):
        nums[int(n)]+=1
    output=""
    d=-1
    for n in nums:
        d+=1
        for a in range(n):
            output=str(d)+output
    return output+'\n'
print(digitOrder('9876543210'))