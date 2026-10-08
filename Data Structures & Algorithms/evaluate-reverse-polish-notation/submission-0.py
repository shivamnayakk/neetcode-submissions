class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        str_operators = "+-*/"

        for token in tokens:

            if token not in str_operators:
                stack.append(int(token))

            else:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    result = a + b

                elif token == "-":
                    result = a - b

                elif token == "*":
                    result = a * b

                elif token == "/":
                    result = int(a / b)

                stack.append(result)

        return stack[-1]    

