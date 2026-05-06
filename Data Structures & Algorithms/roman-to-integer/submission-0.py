class Solution:
    def romanToInt(self, s):
        roman_map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV": 4, "IX": 9, "XL":40, "XC": 90, "CD": 400, "CM": 900}
        retval = 0
        print(s[:1])
        for index, char in enumerate(s):
            is_skip = False
            if index < len(s) - 1:
                is_skip = (char == 'I' and (s[index + 1] == "V" or s[index + 1] == "X")) or (char == 'X' and (s[index + 1] == "L" or s[index + 1] == "C")) or (char == 'C' and (s[index + 1] == "D" or s[index + 1] == "M"))
            if is_skip:
                print("in if")
                retval -= roman_map[char]
            else:
                print("in else")
                retval += roman_map[char]
        return retval