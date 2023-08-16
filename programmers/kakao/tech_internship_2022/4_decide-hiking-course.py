# https://school.programmers.co.kr/learn/courses/30/lessons/118669
from collections import defaultdict
import numpy as np


def solution(n, paths, gates, summits):
    path_dict = defaultdict(dict)
    summit_dict = dict()
    for s in summits:
        summit_dict[s] = True
    answers = dict()
    stack = []

    for p in paths:
        s, e, c = p
        path_dict[s][e] = c
        path_dict[e][s] = c
    # print(path_dict)

    for g in gates:
        stack.append(g)
        answers[g] = 0
    # print(stack)

    answer_summit = None
    answer_cost = np.inf
    # 최종 정답을 따로 계산하지 않고, while안에서 계산하도록 코드를 수정하고
    # 현재 최소값보다 큰 경로는 탐색하지 않도록 조건문을 수정하는 것이 포인트.
    while len(stack) != 0:
        node = stack.pop()
        for next_node in path_dict[node]:
            new_cost = max(answers[node], path_dict[node][next_node])
            if next_node not in answers:
                answers[next_node] = np.inf
            if new_cost < answers[next_node] and new_cost <= answer_cost:
                answers[next_node] = new_cost
                if next_node not in summit_dict:
                    stack.append(next_node)
                else:
                    if answer_cost > answers[next_node]:
                        answer_summit = next_node
                        answer_cost = answers[next_node]
                    elif answer_cost == answers[next_node]:
                        if answer_summit > next_node:
                            answer_summit = next_node

    return [answer_summit, answer_cost]
