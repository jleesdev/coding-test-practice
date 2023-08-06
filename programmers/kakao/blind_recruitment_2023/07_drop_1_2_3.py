# https://school.programmers.co.kr/learn/courses/30/lessons/150364


class Node:
    value = None
    childs = None
    way_idx = None

    def __init__(self, value):
        self.value = value
        self.childs = []
        self.way_idx = -1

    def __lt__(self, other):
        return self.value < other.value

    def add_child(self, child_node):
        self.childs.append(child_node)

    def sort_childs(self):
        self.childs.sort()

    def init_the_way(self):
        if len(self.childs) != 0:
            self.sort_childs()
            self.way_idx = 0

    def get_way_idx(self):
        curr_way_idx = self.way_idx
        if curr_way_idx != -1:
            self.way_idx = (self.way_idx + 1) % len(self.childs)
        return curr_way_idx


class GameTree:
    root_node = None
    count = None
    order = None

    def __init__(self, root_node, length, target):
        self.root_node = root_node
        self.target = target
        self.drop_count = 0
        self.count = []
        self.order = []
        for _ in range(length):
            self.count.append(0)
            self.order.append([])

    def is_valid(self):
        valids = [0] * len(self.count)
        for idx in range(len(self.count)):
            count, target = self.count[idx], self.target[idx]
            if count > target:
                return -1
            elif 3 * count >= target:
                valids[idx] = 1
            else:
                valids[idx] = 0
        return valids

    def drop_the_number(self):
        node = self.root_node
        curr_value = node.value
        way_idx = node.get_way_idx()

        while way_idx != -1:
            # print(curr_value, node.childs[way_idx].value)
            node = node.childs[way_idx]
            curr_value = node.value
            way_idx = node.get_way_idx()

        self.drop_count += 1
        self.count[curr_value - 1] += 1
        self.order[curr_value - 1].append(self.drop_count)
        # print(curr_value)

    def get_best_answer(self, count):
        answer = [0] * count
        for idx in range(len(self.target)):
            orders = self.order[idx]
            target = self.target[idx]
            count = self.count[idx]
            for order in orders:
                for candidate in range(1, 4):
                    tmp = target - candidate
                    if tmp <= (count - 1) * 3:
                        answer[order - 1] = candidate
                        count -= 1
                        target = tmp
                        break
            # print(answer)
        return answer


def solution(edges, target):
    existing_nodes = dict()
    for edge in edges:
        parent, child = int(edge[0]), int(edge[1])

        if parent not in existing_nodes:
            parent_node = Node(parent)
        else:
            parent_node = existing_nodes[parent]

        if child not in existing_nodes:
            child_node = Node(child)
        else:
            child_node = existing_nodes[child]

        parent_node.add_child(child_node)
        existing_nodes[parent] = parent_node
        existing_nodes[child] = child_node

    for key in existing_nodes:
        curr_node = existing_nodes[key]
        curr_node.init_the_way()
        # print(curr_node.value)
        # if curr_node.way is not None:
        #     print('way', curr_node.way.value)
        # for child in curr_node.childs:
        #     print(child.value, end=' ')
        # print()

    gametree = GameTree(existing_nodes[1], len(target), target)
    count = 0
    while True:
        gametree.drop_the_number()
        count += 1
        is_valid = gametree.is_valid()
        # print(gametree.__dict__, is_valid, count)
        if is_valid == -1:
            return [-1]
        elif sum(is_valid) == len(is_valid):
            break
    # print(gametree.__dict__, is_valid, count)
    answer = gametree.get_best_answer(count)
    return answer
