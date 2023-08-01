# https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution(cap, n, deliveries, pickups):
    answer = 0
    DP = n - 1  # Delivery Pointer
    PP = n - 1  # Pickup Pointer

    while DP >= 0 or PP >= 0:
        while DP >= 0 and deliveries[DP] == 0:
            DP -= 1
        while PP >= 0 and pickups[PP] == 0:
            PP -= 1

        SDP = DP
        SPP = PP
        SDCAP = 0
        SPCAP = 0
        while DP >= 0 and SDCAP + deliveries[DP] <= cap:
            SDCAP += deliveries[DP]
            deliveries[DP] = 0
            DP -= 1
        if DP >= 0:
            deliveries[DP] -= (cap - SDCAP)
        while PP >= 0 and SPCAP + pickups[PP] <= cap:
            SPCAP += pickups[PP]
            pickups[PP] = 0
            PP -= 1
        if PP >= 0:
            pickups[PP] -= (cap - SPCAP)

        answer += 2 * (max(SDP, SPP) + 1)
        # print(SDP, SPP)
        # print(DP, PP)
        # print(SDCAP, SPCAP)
        # print(deliveries, pickups)
        # print(answer)

    return answer