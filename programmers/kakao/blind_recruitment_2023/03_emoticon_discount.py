# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product

def get_result(users, emoticons, discount_percentages):
    total_emoticon_price = 0
    emoticon_plus_count = 0
    for user in users:
        user_discount_threshold = user[0]
        user_price_threshold = user[1]
        user_price = 0
        for emoticon_price, discount_percentage in zip(emoticons, discount_percentages):
            if discount_percentage >= user_discount_threshold:
                user_price += (100-discount_percentage)*emoticon_price/100
        if user_price >= user_price_threshold:
            emoticon_plus_count += 1
        else:
            total_emoticon_price += user_price
    return [emoticon_plus_count, total_emoticon_price]

def solution(users, emoticons):
    answer = [0,0]
    for i in product([10,20,30,40], repeat=len(emoticons)):
        candidate = get_result(users, emoticons, i)
        if candidate[0] > answer[0] :
            answer = candidate
        elif candidate[0] == answer[0] and candidate[1] > answer[1]:
            answer = candidate
    # print(answer)
    return answer