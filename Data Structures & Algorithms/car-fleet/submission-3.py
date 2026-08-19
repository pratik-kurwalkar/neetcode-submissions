class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positions = []
        stack = []
        for x, y in zip(position, speed):
            positions.append((x, y))
        positions.sort(reverse = True)
        # print(positions)
        for x, y in positions:
            time = (target - x) / y
            # print(time)
            if len(stack) == 0:
                stack.append(time)
            elif stack[-1] < time:
                stack.append(time)
            else:
                continue
        return len(stack)

        