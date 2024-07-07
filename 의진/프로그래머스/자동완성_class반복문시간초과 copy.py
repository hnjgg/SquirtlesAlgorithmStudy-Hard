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
        c_idx = 0
        for i in range(len(word)+1):
            parent_node = self.node_list[c_idx]

            if i == len(word):
                parent_node.state += 1
                break

            if parent_node.next.get(word[i]) is None:
                # Register Child Node
                child_node = Node(idx=self.idx, word=word[:i+1])
                self.node_list.append(child_node)
                parent_node.next[word[i]] = self.idx
                c_idx = parent_node.next[word[i]]
                parent_node.state += 1
                self.idx += 1

            else:
                c_idx = parent_node.next[word[i]]
                parent_node.state += 1

    def search(self, word):
        c_idx = 0
        for i in range(len(word)+1):
            parent_node = self.node_list[c_idx]
            if parent_node.word == word or parent_node.state == 1:
                return i
            next_char = word[i]
            c_idx = self.node_list[parent_node.next[next_char]].idx


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
