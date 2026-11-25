class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = ""
        stack = []
        for char in path + "/":
            if char == "/":
                if ans =="..":
                    if stack:
                        stack.pop()
                elif ans != "." and ans != "":
                    stack.append(ans)
                ans = ""
            else:
                ans += char
        return "/"+ "/".join(stack)
            