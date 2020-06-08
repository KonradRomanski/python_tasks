def rec(h):
    stack = list()
    ma, i = 0, 0
    while i < len(h):
        if (len(stack) == 0) or (h[stack[-1]] <= h[i]):
            stack.append(i)
            i += 1
        else:
            t_stack = stack.pop()
            pow = (h[t_stack] * ((i - stack[-1] - 1) if len(stack) != 0 else i))
            ma = max(ma, pow)

    while len(stack) != 0:
        t_stack = stack.pop()
        pow = (h[t_stack] * ((i - stack[-1] - 1) if len(stack) != 0 else i))
        ma = max(ma, pow)
    return ma


n = int(input())
wy = []
for i in range(n):
    wy.append(int(input()))

print(rec(wy))
