# https://school.programmers.co.kr/learn/courses/30/lessons/150370
import datetime as dt
from dateutil.relativedelta import relativedelta


def solution(today, terms, privacies):
    today = dt.datetime.strptime(today, '%Y.%m.%d')
    answer = []

    rule = dict()
    for i, term in enumerate(terms):
        term = term.split(' ')
        kind, period = term[0], term[1]
        rule[kind] = int(period)

    for i, privacy in enumerate(privacies):
        privacy = privacy.split(' ')
        start_date = dt.datetime.strptime(privacy[0], '%Y.%m.%d')
        kind = privacy[1]

        due_date = start_date + relativedelta(months=rule[kind])
        # print(due_date, today)
        if due_date <= today:
            answer.append(i + 1)
    return answer
