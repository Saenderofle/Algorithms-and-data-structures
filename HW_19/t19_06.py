import heapq

def calculate_min_negative(t, test_cases):
    results = []

    for case in test_cases:
        n, visitors = case
        visitors.sort()
        heap = []
        time = 0
        total_negative = 0
        index = 0

        while index < n or heap:
            if not heap:
                time = max(time, visitors[index][0])
            while index < n and visitors[index][0] <= time:
                r, w = visitors[index]
                heapq.heappush(heap, (-w, r))
                index += 1
            w_neg, r = heapq.heappop(heap)
            w = -w_neg
            total_negative += w * (time - r)
            time += 1

        results.append(total_negative)

    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    visitors = [tuple(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, visitors))

answers = calculate_min_negative(t, test_cases)
for ans in answers:
    print(ans)
