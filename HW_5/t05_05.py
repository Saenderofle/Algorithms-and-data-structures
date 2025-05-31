def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    try:
        N = int(next(it))
        M = int(next(it))
    except StopIteration:
        return

    stops = [None] * N
    travel = [0] * N
    total_workers = 0
    max_arrival = 0
    for i in range(N):
        t = int(next(it))
        travel[i] = t
        k = int(next(it))
        total_workers += k
        workers = [0] * k
        for j in range(k):
            val = int(next(it))
            workers[j] = val
        stops[i] = workers
        if k > 0 and workers[-1] > max_arrival:
            max_arrival = workers[-1]
    target = M if total_workers >= M else total_workers

    totalTravel = sum(travel)
    if target == 0:
        sys.stdout.write(str(totalTravel))
        return

    comp_stops = []
    comp_travel = []
    accum = 0
    for i in range(N):
        if not stops[i]:
            accum += travel[i]
        else:
            if accum:
                comp_stops.append([])
                comp_travel.append(accum + travel[i])
                accum = 0
            else:
                comp_stops.append(stops[i])
                comp_travel.append(travel[i])
    if accum:
        comp_stops.append([])
        comp_travel.append(accum)
    n = len(comp_stops)
    totalTravel_comp = sum(comp_travel)
    rem = [0] * (n + 1)
    rem[n] = 0
    for i in range(n - 1, -1, -1):
        rem[i] = comp_travel[i] + rem[i + 1]

    INF = 10**18

    def feasible(T):
        dp = [0] + [INF] * target
        for i in range(n):
            L = T - rem[i]
            newdp = [INF] * (target + 1)
            if i == 0:
                offset = 0
            else:
                offset = comp_travel[i - 1]
            st = comp_stops[i]
            k = len(st)
            for r in range(target + 1):
                cur = dp[r]
                if cur == INF:
                    continue
                A = cur + offset
                if A > L:
                    continue
                if A < newdp[r]:
                    newdp[r] = A
                if k == 0:
                    continue
                lo_b = 0
                hi_b = k
                while lo_b < hi_b:
                    mid = (lo_b + hi_b) >> 1
                    if st[mid] <= A:
                        lo_b = mid + 1
                    else:
                        hi_b = mid
                j = lo_b
                avail = target - r
                if avail > k:
                    avail = k
                local_st = st
                local_A = A
                local_newdp = newdp
                for x in range(1, avail + 1):
                    if x <= j:
                        cand = local_A
                    else:
                        cand = local_st[x - 1]
                    if cand > L:
                        break
                    idx = r + x
                    if cand < local_newdp[idx]:
                        local_newdp[idx] = cand
            dp = newdp
        final_time = dp[target] + comp_travel[n - 1]
        return final_time <= T

    lo = totalTravel_comp
    hi = totalTravel_comp + max_arrival
    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    sys.stdout.write(str(ans))

if __name__ == '__main__':
    solve()
