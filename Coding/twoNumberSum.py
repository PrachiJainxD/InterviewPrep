def twoNumberSum(array, targetSum):
    # Bruteforce
    # Time O(n^2) | Space O(1)
    # for i in range(len(array) - 1):
    #     firstNum = array[i]
    #     for j in range(i + 1, len(array)):#* range till last num 
    #         secondNum = array[j]
    #         if(firstNum + secondNum == targetSum):
    #             return [firstNum, secondNum]
    # return []
    #
    # Using HashTable
    # Time  O(n) | Space O(n)
    # numbers = {}
    # for num in array: #*accesing each elemnt
    #     potentialMatch = targetSum - num
    #     if potentialMatch in numbers:
    #         return [potentialMatch, num]
    #     else:
    #         numbers[num] = True
    # return []  
    #
    # Without Hashtable
    # Time  O(n log n) | Space O(1)
    array.sort()
    left = 0
    right = len(array) - 1
    while(left < right):
        currentSum = array[left] + array[right] 
        if(currentSum == targetSum):
            return [array[left], array[right]]
        elif(currentSum < targetSum):
            left += 1
        else:
            right -= 1
    
    return []     