class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:

        pattern_dict = {}
        str_dict = {}
        str_list = str.split(' ')
        if(not len(pattern) == len(str_list)):
            return False

        for i in range(len(pattern)):

            pattern_dict[pattern[i]] = pattern_dict.get(pattern[i], i)

            str_dict[str_list[i]] = str_dict.get(str_list[i], i)

            if(not pattern_dict[pattern[i]] == str_dict[str_list[i]]):
                return False
        return True
