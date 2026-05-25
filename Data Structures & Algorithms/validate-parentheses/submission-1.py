class Solution:
    def isValid(self, s: str) -> bool:
        bracks = {")":"(", "}":"{", "]":"["}

        collect = []

        for b in s:
            if b in bracks:
                if collect and collect[-1] == bracks[b]:
                    collect.pop()
                else:
                    return False
            else:
                collect.append(b)

        return True if not collect else False
