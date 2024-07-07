import sys
sys.setrecursionlimit(1 << 20)


class Node:
    def __init__(self, idx, word):
        self.idx = idx
        self.word = word
        self.next = {}
        self.state = 0


class Trie:
    def __init__(self):
        self.root_node = Node(idx=0, word=None)
        self.idx = 1
        self.node_list = [self.root_node]

    def add(self, word):
        self._add(word, 0, 0)

    def _add(self, word, idx, depth):
        parent_node = self.node_list[idx]
        if depth == len(word):
            parent_node.state += 1
            return
        else:
            if parent_node.next.get(word[depth]) is None:
                # Register Child Node
                child_node = Node(idx=self.idx, word=word[:depth+1])
                self.node_list.append(child_node)
                parent_node.next[word[depth]] = self.idx
                next_idx = parent_node.next[word[depth]]
                self.idx += 1

                # Add Nodes Recursively
                self._add(word, next_idx, depth + 1)

                # Update State
                parent_node.state += 1

            else:
                next_idx = parent_node.next[word[depth]]
                self._add(word, next_idx, depth + 1)
                parent_node.state += 1

    def search(self, word):
        return self._search(word, 0, 0)

    def _search(self, word, idx, depth):
        parent_node = self.node_list[idx]
        if parent_node.word == word or parent_node.state == 1:
            return depth
        next_char = word[depth]
        next_node = self.node_list[parent_node.next[next_char]]
        return self._search(word, next_node.idx, depth + 1)


def solution(words):
    trie = Trie()

    # learning
    for word in words:
        trie.add(word)

    # print("=====")
    # for item in trie.node_list:
    #     print(item.word, item.state)

    # Searching
    ret = 0
    for word in words:
        ret += trie.search(word)

    return ret


print(solution(["word", "war", "warrior", "world"]))
