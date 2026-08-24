
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# Second Solution






# First Solution
# its like ["a"] : [["abc", add]] , ....

        result = {}

        for i in range(len(strs)):
            groupedStrs = "".join(sorted(strs[i]))

            if groupedStrs in result:
                result[groupedStrs].append(strs[i])
            else:
                result[groupedStrs] = [strs[i]]

        return list(result.values())

