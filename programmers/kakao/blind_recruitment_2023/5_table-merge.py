# https://school.programmers.co.kr/learn/courses/30/lessons/150366
import numpy as np
from collections import defaultdict


class Table:
    values = None
    merges = None
    # value_idxs = None # 밸류-인덱스 역색인 구현하려던 흔적

    def __init__(self):
        self.values = np.full((51, 51), None)
        self.merges = defaultdict(list)
        # self.value_idxs = defaultdict(list)

    def get_value(self, r, c):
        if self.values[r][c] is None:
            return 'EMPTY'
        else:
            return self.values[r][c]

    def update_value(self, r, c, value):
        self.values[r][c] = value
        if (r, c) in self.merges:
            for cell in self.merges[(r, c)]:
                r, c = cell
                self.values[r][c] = value

    def find_update_value(self, value1, value2):
        for r in range(1, 51):
            for c in range(1, 51):
                value = self.get_value(r, c)
                if value == value1:
                    self.values[r][c] = value2

    def merge_cell(self, r1, c1, r2, c2):
        value1 = self.get_value(r1, c1)
        value2 = self.get_value(r2, c2)

        if value1 == 'EMPTY':
            value = value2
            self.update_value(r1, c1, value)
        else:
            value = value1
            self.update_value(r2, c2, value)

        merged_cells = [(r1, c1), (r2, c2)]
        merged_cells = merged_cells + self.merges[(r1, c1)] + self.merges[(r2, c2)]

        for cell in merged_cells:
            self.merges[cell] = list(set(merged_cells))

    def unmerge_cell(self, r, c):
        if (r, c) in self.merges:
            for cell in self.merges[(r, c)]:
                if cell != (r, c):
                    tmp_r, tmp_c = cell
                    self.values[tmp_r][tmp_c] = None
                    self.merges.pop(cell)
            self.merges.pop((r, c))


def solution(commands):
    table = Table()
    # print(table.values)

    answer = []
    for command in commands:
        command_list = command.split(" ")
        command = command_list[0]

        if command == 'UPDATE':
            if len(command_list) == 4:
                r = int(command_list[1])
                c = int(command_list[2])
                value = command_list[3]
                table.update_value(r, c, value)
            elif len(command_list) == 3:
                value1 = command_list[1]
                value2 = command_list[2]
                table.find_update_value(value1, value2)
        elif command == 'MERGE':
            r1 = int(command_list[1])
            c1 = int(command_list[2])
            r2 = int(command_list[3])
            c2 = int(command_list[4])
            table.merge_cell(r1, c1, r2, c2)
        elif command == 'UNMERGE':
            r = int(command_list[1])
            c = int(command_list[2])
            table.unmerge_cell(r, c)
        elif command == 'PRINT':
            r = int(command_list[1])
            c = int(command_list[2])
            answer.append(table.get_value(r, c))
        else:
            print("invalid command.")
        # print(command_list, table.values, table.merges) #, table.values)
    return answer
