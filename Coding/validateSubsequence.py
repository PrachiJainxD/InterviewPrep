def isValidSubsequence(array, sequence):
    # Time O(n) | Space O(1)
    # seqIdx = 0
    # arrIdx = 0
    # while seqIdx < len(sequence) and arrIdx < len(array):
    #     if sequence[seqIdx] == array[arrIdx]:
    #         seqIdx +=1
    #     arrIdx +=1
    
    # return seqIdx == len(sequence)    

    # Time O(n) | Space O(1)
    seqIdx = 0
    for value in array: 
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx +=1
    
    return seqIdx == len(sequence)  
        