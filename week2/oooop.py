def solution(v):
    answer = []

    if int(v[0[0]]) == int(v[1[0]]):
        answer += v[2[0]]
    else:
        if int(v[0[0]]) == int(v[0[2]]):
            answer += v[1[0]]
        else:
            answer += v[0[0]]
    if int(v[0[1]]) == int(v[1[1]]):
        answer += v[2[1]]
    else:
        if int(v[0[1]]) == int(v[2[1]]):
            answer += v[1[1]]
        else:
            answer += v[0[1]]

    return answer
print(solution([[1,4],[3,4],[3,10]]))
