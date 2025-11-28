from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        memory = []


        for token in tokens:
            if token in ["+","-","*","/"]:
                x = memory.pop()
                y = memory.pop()
                if token == "+":
                    memory.append(x+y)
                elif token == "-":
                    memory.append(x-y)
                elif token == "*":
                    memory.append(x*y)
                elif token == "/":
                    memory.append(int(f"{y/x:.0f}"))
            else:
                memory.append((int(token)))

        return memory[0]

