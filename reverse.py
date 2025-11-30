class solution:
    def reversewordsstring(self, s: str):

        def reverse(word:str):
            resp = ""
            for i in range(len(word)-1, -1, -1):
                resp = resp + word[i]
            return resp

        parts = s.split(" ")
        arr = []
        for part in parts:
            arr.append(reverse(part))
        print(arr)
        return " ".join(arr)




obj = solution()
print(obj.reversewordsstring("one  two three"))