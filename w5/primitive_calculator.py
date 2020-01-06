# Uses python3
import sys

# def optimal_sequence(n):
#     sequence = []
#     while n >= 1:
#         sequence.append(n)
#         if n % 3 == 0:
#             n = n // 3
#         elif n % 2 == 0:
#             n = n // 2
#         else:
#             n = n - 1
#     return reversed(sequence)

def optimal_sequence(n):
    ancestors = [0] * (n + 1)
    ancestors[2] = 1
    lengths = [1] * (n + 1)
    lengths[2] =  1
    for i in range(3, n + 1):
        u = v = sys.maxsize
        if i % 3 == 0:
            u = lengths[i // 3]
        if n % 2 == 0:
            v = lengths[i // 2]
        w = lengths[i - 1]
        best = min(u, v, w)
        if best == u:
            lengths[i] = u + 1
            ancestors[i] = i // 3
        elif best == v:
            lengths[i] = v + 1
            ancestors[i] = i // 2
        else: # w
            lengths[i] = w + 1
            ancestors[i] = i - 1
    backwards = []
    backwards.append(n)
    j = n
    while j > 1:
        j = ancestors[j]
        backwards.append(j)
    return backwards.reverse  

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
