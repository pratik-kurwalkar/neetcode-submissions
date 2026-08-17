class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        for x in s:
            if x in key:
                stack.append(key[x])
                print(stack)
            elif x in key.values():
                if len(stack) == 0:
                    return False
                elif x != stack.pop():
                    return False
            else:
                pass
        return len(stack) == 0