def inplaceqs(s, a, b):
    def swapElements(s, a, b):
        tmp = s[a]
        s[a] = s[b]
        s[b] = tmp
    if a >= b: return
    pivot = s[b] # select last element as pivot
    left = a
    right = b - 1
    while left <= right:
        while left <= right and left <= right and s[left] <= pivot:  # find an element larger than the pivot
            left += 1   
        while left <= right and right >= left and s[right] >= pivot: # find an element larger than the pivot
            right -= 1  
        if left < right: 
            swapElements(s, left, right)
    swapElements(s, left, b) # put the pivot its final place
    #recursice calls
    inplaceqs(s, a, left-1) 
    inplaceqs(s, left+1, b)

### Test
arr = [19,13,1,5,3,4,111,34,141,22,78,23,55]
inplaceqs(arr, 0, 12)
print arr
