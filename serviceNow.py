class Solution:
    def decode(self, s:str):
        ans = [0] * 26
        curr = []
        repeat = ""
        while s:
            ch = s.pop()
            if ch == "#":
                num2 = s.pop()
                num1 = s.pop()
                curr.append(num1+num2)
            elif ch == ")":
                while s and s[-1] != "(":
                    repeat += s.pop()
                repeat = repeat[::-1]
                s.pop()
            else:
                for i in range(int(repeat)):
                    curr.append(ch)
        print(curr)

sol = Solution()
sol.decode("1224#26#")













# 1223#1(2)