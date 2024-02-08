List = list
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        elif len(strs) == 1: return strs[0]
        index = 0
        output = ""
        archor_word = strs[0]
        strs.pop(0)

        try:

            while True:

                for i in strs:
                    if i == "":
                        return output
                    if i[index] != archor_word[index]:
                        return output
                output+= i[index]
                index += 1
        except:
            return output


"""
Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

"""
x = Solution()
print(x.longestCommonPrefix(["flower","flow","flight"]))
print(x.longestCommonPrefix(["dog","racecar","car"]))
print(x.longestCommonPrefix(["","",""]))
print(x.longestCommonPrefix(["","b"]))