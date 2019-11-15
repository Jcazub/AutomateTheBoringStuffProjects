# Quick Union class implemented in Python from memory


class QuickUnion:

    def __init__(self, number_of_objects: int):
        self._objects = [i for i in range(number_of_objects)]  # initialize objects
        self._component_size = [1] * number_of_objects

    def __find_root(self, p: int) -> int:
        while self._objects[p] != p:
            self._objects[p] = self._objects[self._objects[p]]  # single pass path compression
            p = self._objects[p]
        return p

    def connected(self, p: int, q: int):  # checks if either objects are in the same root
        return self.__find_root(p) == self.__find_root(q)

    def union(self, p: int, q: int):  # creates a connection between the objects
        pid = self.__find_root(p)
        qid = self.__find_root(q)

        if pid == qid:
            return

        pid_size = self._component_size[pid]
        qid_size = self._component_size[qid]

        if pid_size > qid_size:
            self._objects[qid] = pid
            self._component_size[pid] += self._component_size[qid]
        else:
            self._objects[pid] = qid
            self._component_size[qid] += self._component_size[pid]

    def __str__(self):
        return ", ".join(['{}:{}'.format(i, x) for i, x in enumerate(self._objects, 0)])


def main():
    qu = QuickUnion(10)

    qu.union(0, 1)
    qu.union(0, 3)
    qu.union(0, 5)

    qu.union(8, 9)
    qu.union(7, 9)

    qu.union(5, 9)
    qu.union(4, 7)

    print(str(qu))


if __name__ == "__main__":
    main()
