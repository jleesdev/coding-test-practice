# https://leetcode.com/problems/candy
# Runtime 145ms (81.34%)
# Memory 19.45mb (28.12%)


class Solution:
    def candy(self, ratings: List[int]) -> int:
        before_offer = 1
        n = len(ratings)
        left_offers = [1] * n
        right_offers = [1] * n

        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                left_offers[i + 1] = left_offers[i] + 1
            else:
                left_offers[i + 1] = 1

        for i in range(n - 1, 0, -1):
            if ratings[i] < ratings[i - 1]:
                right_offers[i - 1] = right_offers[i] + 1
            else:
                right_offers[i - 1] = 1

        # offers = [max(left_offers[i], right_offers[i]) for i in range(n)]
        # print(left_offers, right_offers, offers)
        # return sum(offers)

        answer = 0
        for i in range(n):
            answer += max(left_offers[i], right_offers[i])

        return answer
