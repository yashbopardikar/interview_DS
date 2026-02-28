class Solution():
    def lettercombination(self, digits, words):
        digit_map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        resp = []
        def backtracking(index, pattern, word):
            if pattern == word:
                resp.append(pattern[:])
                return
            for c in digit_map[digits[index]]:
                backtracking (index+1, pattern + c)

        for word in words:
            backtracking(0,"", word)
        return resp

sol = Solution()
print(sol.lettercombination("23"))