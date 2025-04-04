class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_freq = max(counts.values())
        if max_freq > (len(s) + 1) // 2:
            return ""  # Not possible to reorganize
        heap = [(-count, char) for char, count in counts.items()]
        heapq.heapify(heap)
        
        result = []
        prev_count, prev_char = 0, ""

        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)

            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            prev_count = count + 1  # because count is negative
            prev_char = char

        return ''.join(result)
        

