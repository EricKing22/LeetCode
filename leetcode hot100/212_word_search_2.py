from typing import List

class TreeNode():
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie():
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
        node.is_end_of_word = True


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        for word in words:
            trie.insert(word)

        self.result = set()
        self.rows, self.cols = len(board), len(board[0])
        self.visited = set()

        def dfs(r, c, node, path):

            if r < 0 or r > len(board) - 1 or c < 0 or c >len(board[0]) - 1 or (r,c) in self.visited:
                return

            char = board[r][c]

            if char not in node.children:
                return

            node = node.children[char]

            path += char

            if node.is_end_of_word:
                self.result.add(path)
                node.is_end_of_word = False

            self.visited.add((r, c))

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r, new_c = r + dr, c + dc
                dfs(new_r, new_c, node, path)

            self.visited.remove((r, c))

        for r in range(self.rows):
            for c in range(self.cols):
                dfs(r, c, trie.root, "")

        return list(self.result)