# https://leetcode.com/problems/gas-station
# Runtime 1108ms (71.45%)
# Memory 22.29mb (25.03%)


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # n == len(gas) == len(cost)
        n = len(gas)
        sum_of_lefts = 0
        start_idx = 0

        for i in range(n):
            left = gas[i] - cost[i]
            sum_of_lefts += left
            if left < 0:
                # setting start_idx decreases the runtime
                start_idx = i+1
        # no availabe answer
        if sum_of_lefts < 0:
            return -1

        for i in range(start_idx, start_idx+n):
            left = 0
            success = True
            for j in range(n):
                idx = (i + j) % n
                # divide gas addition and cost subtraction
                # no gas, then no journey
                left += gas[idx]
                if left <= 0:
                    success = False
                    break
                left -= cost[idx]
                if left < 0:
                    success = False
                    break
            if left >= 0 and success is True:
                # start_idx can over n.
                return i % n
        # no available answer, nevertheless searched all possible cases.
        return -1
