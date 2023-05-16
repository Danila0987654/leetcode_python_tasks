# Task 13.Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def __init__(self, s: str):
        self.roman = s
        self.answer = 0

    def switchCase(self, roman):
        match roman:
            case "I":
                self.answer += 1
            case "V":
                self.answer += 5
            case "X":
                self.answer += 10
            case "L":
                self.answer += 50
            case "C":
                self.answer += 100
            case "D":
                self.answer += 500
            case "M":
                self.answer += 1000
            case "IV":
                self.answer += 4
            case "IX":
                self.answer += 9
            case "XL":
                self.answer += 40
            case "XC":
                self.answer += 90
            case "CD":
                self.answer += 400
            case "CM":
                self.answer += 900

    def romanToInt(self):
        length = len(self.roman)
        i = 0
        while i < length:
            was = False
            if i + 1 < length:
                if f"{self.roman[i]}{self.roman[i + 1]}" in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                    self.switchCase(f"{self.roman[i]}{self.roman[i + 1]}")
                    was = True
                    i += 1
                else:
                    self.switchCase(self.roman[i])
            elif i + 1 == length and not was:
                self.switchCase(self.roman[i])
            i += 1
        return self.answer


task_1 = Solution("IIIIVI")
task_2 = Solution("III")
task_3 = Solution("LVIII")
task_4 = Solution("MCMXCIV")

print(task_1.romanToInt())
print(task_2.romanToInt())
print(task_3.romanToInt())
print(task_4.romanToInt())
