# https://school.programmers.co.kr/learn/courses/30/lessons/118666
from collections import defaultdict


def solution(survey, choices):
    scores = defaultdict(int)

    for s, c in zip(survey, choices):
        left = s[0]
        right = s[1]

        if c < 4:
            scores[left] += 4 - c
        elif c > 4:
            scores[right] += c - 4
    # print(scores)

    answer = ''
    metrics = ['RT', 'CF', 'JM', 'AN']
    for m in metrics:
        if scores[m[0]] >= scores[m[1]]:
            answer += m[0]
        else:
            answer += m[1]
    return answer
