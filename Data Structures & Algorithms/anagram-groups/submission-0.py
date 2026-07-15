from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        result = []
        for word in strs:
            sorted_string = sorted(word)
            sorted_key = "".join(sorted_string)
            my_map[sorted_key].append(word)

        return list(my_map.values())

        