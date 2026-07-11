from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0

        def generate_lookup(word_list):
            wild_key_map = defaultdict(set)
            word_key_map = defaultdict(set)
            candidates = word_list + [beginWord]

            for word in candidates:
                res = []
                for i in range(len(word)):
                    wc = word[:i] + "*" + word[i + 1:]
                    res.append(wc)

                    wild_key_map[wc].add(word)

                word_key_map[word].update(res)

            return wild_key_map, word_key_map

        def bfs(start):
            queue = deque([(start, 1)])
            visited = set([start])

            while len(queue) > 0:
                word, length = queue.popleft()

                for wildcard in word_key_map[word]:
                    for nw in wild_key_map[wildcard]:
                        if nw == endWord:
                            return length + 1

                        if nw in visited:
                            continue

                        visited.add(nw)
                        queue.append((nw, length + 1))

            return 0 

        wild_key_map, word_key_map = generate_lookup(wordList)

        return bfs(beginWord)