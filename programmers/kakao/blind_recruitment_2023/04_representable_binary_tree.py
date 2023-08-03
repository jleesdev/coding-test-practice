# https://school.programmers.co.kr/learn/courses/30/lessons/150367
import math

def convert_to_binary(number):
    tmp = []

    # 십진수 -> 이진수 공식으로 이진수값을 리스트로 저장
    while True:
        remainder = number % 2
        number = number // 2
        tmp.append(remainder)

        if number < 2:
            if number != 0:
                tmp.append(number)
            break

    # 포화 이진트리를 만들기 위해 전체 길이를 계산
    log_tmp = int(math.log(len(tmp), 2))
    full_len = pow(2, log_tmp + 1) - 1

    # 부족한 만큼 0으로 리스트를 채움
    while len(tmp) < full_len:
        tmp.append(0)

    # 뒤집어서 본래 이진수의 모양으로 변환
    tmp.reverse()
    return tmp


def solution(numbers):
    answers = []
    for number in numbers:
        binary = convert_to_binary(number)
        root_node_idx = int((len(binary) + 1) / 2) - 1
        # print(binary, binary[root_node_idx], binary[1::2])

        # 일단 정답을 1로 두고, 불가한 케이스에 걸리면 0으로 변경
        answer = 1

        # root_node의 값이 0이면 불가
        if binary[root_node_idx] == 0:
            answer = 0
        else:
            # 부모가 되는 노드들만 탐색
            for idx in range(2, len(binary) + 1, 2):
                # print(idx-1)

                # 부모가 되는 노드의 값이 더미면, 자식 노드를 검사
                if binary[idx - 1] == 0:
                    tmp_idx = idx
                    # print(tmp_idx, end=', ')

                    # 자식 노드를 검사하기 위해 자식 노드와의 idx diff를 계산
                    diff = 0
                    while True:
                        if tmp_idx % 2 == 0:
                            diff += 1
                            tmp_idx = tmp_idx / 2
                        else:
                            break
                    diff = pow(2, diff - 1)
                    # print(diff)

                    # 부모 노드가 더미인데 자식 노드가 더미가 아니라면 불가
                    if binary[idx - 1 - diff] == 1 or binary[idx - 1 + diff] == 1:
                        answer = 0
        answers.append(answer)
    return answers