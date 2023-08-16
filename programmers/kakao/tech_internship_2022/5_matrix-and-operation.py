# https://school.programmers.co.kr/learn/courses/30/lessons/118670
from collections import deque


def solution(rc, operations):
    col_length = len(rc[0])
    row_length = len(rc)
    first_col = deque([rc[row_idx][0] for row_idx in range(row_length)])
    last_col = deque([rc[row_idx][col_length - 1] for row_idx in range(row_length)])
    inner_rows = deque([deque(rc[row_idx][1:col_length - 1]) for row_idx in range(row_length)])

    for operation in operations:
        if operation == 'ShiftRow':
            first_col.appendleft(first_col.pop())
            last_col.appendleft(last_col.pop())
            inner_rows.appendleft(inner_rows.pop())
        elif operation == 'Rotate':
            # col_length == 2인 케이스에서 inner_rows가 비어있을 수 있기 때문에,
            # append 해주고 pop을 해야, 효율성 4번 6번에서 에러가 안난다.
            inner_rows[0].appendleft(first_col.popleft())
            last_col.appendleft(inner_rows[0].pop())
            inner_rows[row_length - 1].append(last_col.pop())
            first_col.append(inner_rows[row_length - 1].popleft())

    answers = []
    for row_idx in range(row_length):
        answers.append([first_col[row_idx]] + list(inner_rows[row_idx]) + [last_col[row_idx]])
    return answers
