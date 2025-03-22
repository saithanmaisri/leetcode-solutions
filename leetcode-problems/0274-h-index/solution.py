class Solution:
    def hIndex(self, citations: list[int]) -> int:
        max_citation = max(citations)
        sorted_citation: list[int] = []
        h_index = 0

        counted_array = [0] * (max_citation + 1)

        for citation in citations:
            counted_array[citation] = counted_array[citation] + 1

        for index_i in range(len(counted_array)):
            while counted_array[index_i] > 0:
                sorted_citation.append(index_i)
                counted_array[index_i] = counted_array[index_i] - 1
        
        sorted_citation.reverse()

        for index_i in range(len(sorted_citation)):
            if sorted_citation[index_i] > index_i:
                h_index = h_index + 1

        return h_index
    
