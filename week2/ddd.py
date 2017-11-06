def solution(arr):
    answer = []
    i=0
    for i in range(len(arr)):
        while arr[i] != arr[i+1]:
            if arr[i] != arr[i+1] :
                arr.remove(arr[i+1])
        i += 1    
    return answer