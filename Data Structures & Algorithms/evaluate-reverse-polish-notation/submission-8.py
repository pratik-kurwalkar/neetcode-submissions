class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operators = ["+", "-", "*", "/"]
        for x in tokens:
            if x not in operators:
                numbers.append(int(x))
            elif x == "+":
                numbers.append(numbers.pop() + numbers.pop())
            elif x == "*":
                numbers.append(numbers.pop() * numbers.pop())
            elif x == "-":
                numbers.append(-1 * (numbers.pop() - numbers.pop()))
            else:
                a = numbers.pop()
                b = numbers.pop()
                numbers.append(int(float(b)/a))
        return numbers.pop()       