# https://leetcode.com/problems/insert-delete-getrandom-o1
# Runtime 464ms (40.47%)
# Memory 63.75mb (45.94%)
import random


class RandomizedSet:
    random_set = None

    def __init__(self):
        self.random_set = dict()

    def insert(self, val: int) -> bool:
        if not val in self.random_set:
            self.random_set[val] = True
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        pop_value = self.random_set.pop(val, None)
        if pop_value is not None:
            return True
        else:
            return False

    def getRandom(self) -> int:
        rnd_idx = random.randrange(len(self.random_set))
        val = list(self.random_set.keys())[rnd_idx]
        return val

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
