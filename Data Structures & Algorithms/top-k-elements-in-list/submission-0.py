import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nmap = defaultdict(int)
        for n in nums:
            nmap[n] += 1

        unique_n = list(nmap.keys())
        heapq.heapify(unique_n)

        k_freq = heapq.nlargest(k, unique_n, key=lambda x: nmap[x])

        return k_freq
