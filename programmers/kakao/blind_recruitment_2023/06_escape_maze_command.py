# https://school.programmers.co.kr/learn/courses/30/lessons/150365


def move(cr, cc, command):
    if command == 'd':
        cr += 1
    elif command == 'u':
        cr -= 1
    elif command == 'l':
        cc -= 1
    elif command == 'r':
        cc += 1
    return cr, cc


def is_valid_move(n, m, cr, cc, r, c, k):
    x_diff = abs(r - cr)
    y_diff = abs(c - cc)
    total_diff = x_diff + y_diff
    is_valid = True

    if k - total_diff < 0:
        is_valid = False
    elif (k - total_diff) % 2 != 0:
        is_valid = False

    if cr < 1 or cr > n:
        is_valid = False
    if cc < 1 or cc > m:
        is_valid = False
    return is_valid


def solution(n, m, x, y, r, c, k):
    answer = ''
    cr, cc = x, y
    # print(cr, cc)
    if not is_valid_move(n, m, cr, cc, r, c, k):
        answer = 'impossible'
    else:
        while k != 0:
            for command in ['d', 'l', 'r', 'u']:
                next_cr, next_cc = move(cr, cc, command)
                is_valid = is_valid_move(n, m, next_cr, next_cc, r, c, k - 1)
                if is_valid:
                    cr, cc = next_cr, next_cc
                    answer += command
                    k -= 1
                    # print(cr, cc)
                    break
    return answer
