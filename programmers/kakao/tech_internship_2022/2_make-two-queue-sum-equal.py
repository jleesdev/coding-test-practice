# https://school.programmers.co.kr/learn/courses/30/lessons/118667
from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # never satisfy conditions
    total_sum = sum1 + sum2
    if total_sum % 2 != 0:
        return -1

    # find solution
    # m = len(queue1), n = len(queue2)
    # (not sure) 2m - 2 + n or 2n - 2 + m is the max of pop count
    # the max of pop count should be smaller than 2m + 2n
    total_len = (len(queue1) + len(queue2)) * 2
    max_num = int(total_sum / 2)
    pop_count = 0
    while pop_count <= total_len:
        if sum1 == sum2:
            # don't need to move anymore
            break
        elif sum1 < sum2:
            pop_num = queue2.popleft()
            queue1.append(pop_num)
            sum2 -= pop_num
            sum1 += pop_num
        else:
            pop_num = queue1.popleft()
            queue2.append(pop_num)
            sum1 -= pop_num
            sum2 += pop_num
        if pop_num > max_num:
            return -1
        pop_count += 1

    if pop_count > total_len:
        return -1
    return pop_count
