class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        output = ""
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                ans = ""
                while stack and stack[-1] != "[":
                    val = stack.pop()
                    ans = val + ans
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * ans)
        return "".join(stack)

        