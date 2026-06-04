class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                r = stack.pop()
                l = stack.pop()

                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(l/r))

        return stack.pop()

        