arr = [1,1,3,3,0,1,1]
def solution(arr):
    answer = []
    for v in arr:
        if not answer or answer[-1] != v:
            answer.append(v)
    print(answer)
    return answer

solution(arr)