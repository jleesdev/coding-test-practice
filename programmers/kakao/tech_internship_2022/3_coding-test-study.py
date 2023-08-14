# https://school.programmers.co.kr/learn/courses/30/lessons/118668
import numpy as np


def solution(alp, cop, problems):
    # problems = np.array(problems)
    # max_alp, max_cop = max(problems[:, 0]), max(problems[:, 1])
    # -> test case #1 over time!! do not use numpy.
    max_alp, max_cop = 0, 0
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])

    answers = np.full((max_alp + 1, max_cop + 1), np.inf)
    cur_alp = min(max_alp, alp)
    cur_cop = min(max_cop, cop)
    answers[cur_alp, cur_cop] = 0
    for alp in range(cur_alp, max_alp + 1):
        for cop in range(cur_cop, max_cop + 1):
            if alp + 1 < max_alp + 1:
                answers[alp + 1, cop] = min(answers[alp + 1, cop], answers[alp, cop] + 1)
            if cop + 1 < max_cop + 1:
                answers[alp, cop + 1] = min(answers[alp, cop + 1], answers[alp, cop] + 1)

            for p in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = p
                if alp_req <= alp and cop_req <= cop:
                    next_alp = min(max_alp, alp + alp_rwd)
                    next_cop = min(max_cop, cop + cop_rwd)
                    answers[next_alp, next_cop] = min(answers[next_alp, next_cop], answers[alp, cop] + cost)
    answer = answers[max_alp, max_cop]
    return answer
